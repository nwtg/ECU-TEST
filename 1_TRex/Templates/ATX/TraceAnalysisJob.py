# -*- coding: utf-8 -*-

"""
Created on 15.08.2014

Erzeugt aus dem übergebenen TraceAnalyse-Job die ATX Struktur im Speicher.

:author: Christoph Groß <christoph.gross@tracetronic.de>
"""

import os
import tempfile

# ImageEntity wird in einem isinstance()-Ausdruck benutzt. Daher funktioniert FakeApiModules
# nicht.
try:
    # ab ECU-TEST 8.1
    from tts.core.report.db.ImageEntity import ImageEntity
except ImportError:
    # bis ECU-TEST 8.0
    from lib.report.db.ImageEntity import ImageEntity

from log import EPrint

from .Config import Config
from .Node import Node
from .Utils import (FilterSUCCESS, GetReviewsForReportItem, UpdateRefOnReviews)


class TraceAnalysisJob(object):
    """
    Konvertiert ein ECU-TEST TraceAnalyse-Job in ein ATX TestCase.
    """
    def __init__(self, job, refPath, report):
        """
        Konstruktor.
        :param job: Der zu konvertierende Job.
        :type job: AnalysisJobItem
        :param refPath: Ref Pfad des Packages
        :type refPath: str
        :param report: Durchgereichtes ReportApi Objekt.
        :type report: ReportApi
        """
        self.__report = report
        self.__refPath = refPath
        self.__traceAnalyseSteps = {}
        self.__reviews = []
        self.__plots = {}
        self.__createTestSteps = Config.GetSetting(report, u'includePkgTestSteps') == u"True"

        self.__convertedJob = self.__ConvertJob(job)

    def GetConvertedJob(self):
        """
        Gibt den konvertierten Analyse-Job zurück.
        :return: Der konvertierte Job.
        :rtype: dict
        """
        return self.__convertedJob

    def GetTestStepPlots(self):
        """
        :return: die Test-Step ATX-RefPaths mit der Datei-Liste der Plots, welche in diesem
                 Test-Step erstellt wurden.
        :rtype: dict
        """
        return self.__plots

    def GetReviews(self, reportRefPath):
        """
        Gibt die Reviews des Packages zurück.
        :param reportRefPath: REF Pfad zum Report TestCase
        :type reportRefPath: str
        :return: Liste der Reviews
        :rtype: List->Review
        """
        return UpdateRefOnReviews(self.__reviews, reportRefPath)

    def __CreateReviewsForTraceStep(self, traceStep):
        """
        Ermittelt alle Nachbewertungen zu dem TraceStep und erzeugt für jede ein Review Objekt.
        :param traceStep: TraceStep, zu dem Nachbewertungen erfasst werden
        :type traceStep: ReportItem
        """
        self.__reviews.extend(GetReviewsForReportItem(self.__report, traceStep))

    def __ConvertJob(self, job):
        """
        Führt die Konvertierung aus.
        :param job: Der zu konvertierende Job.
        :type job: AnalysisJobItem
        :return: Liste mit TestSteps
        :rtype: list
        """
        tmpDir = tempfile.mkdtemp(prefix=u'plotArchive_')

        # initial node, taking all depth=0 nodes
        rootNode = None

        if self.__createTestSteps:
            for traceItem in job.IterTraceItems():
                """
                @type traceItem: lib.report.db.ReportItem.ReportItem
                """
                reportId = int(traceItem.GetReportItemId())
                result = FilterSUCCESS(traceItem.GetResult())
                name = traceItem.GetActivity()
                execLevel = traceItem.GetExecLevel()

                # Falls noch kein Root-Knoten vorhanden ist wird er angelegt (erster valider
                # Iterationsschritt)
                if not rootNode:
                    # root Knoten bekommt als SHORT-NAME den Ref Pfad seines TestCases
                    # -> wird im else von Node.getRefPath() abgerufen
                    rootNode = Node(execLevel - 1, {u'SHORT-NAME': self.__refPath})

                plots = self.__GetPlotFilesForTestStep(tmpDir, reportId, traceItem)

                # CATEGORY für die Plots/Images in den ATX TEST-STEPS festlegen
                args = {u'id': reportId,
                        u'verdict': result,
                        u'longName': name,
                        u'category': u"TRACE_ANALYSIS_PLOT" if len(plots) > 0 else False}
                createdTestStep = self.__CreateTestStep(args)

                rootNode.AddNode(execLevel, createdTestStep)
                self.__CreateReviewsForTraceStep(traceItem)

                self.__ComputePlotRefPaths(plots, rootNode, createdTestStep[u'SHORT-NAME'])

        if rootNode:
            stepLists = rootNode.GetList()
            if len(stepLists[u'testSteps']) > 0:
                if stepLists[u'testSteps'][0][u'@type'] == u'TEST-STEP':
                    # Die Traceanalyse wurde nicht ausgeführt, aber erstellt
                    # Daher eine "leere" Traceanalyse erzeugen
                    # --> TestStepFolder ohne Kinder
                    stepLists[u'testSteps'][0][u'@type'] = u'TEST-STEP-FOLDER'
                    stepLists[u'testSteps'][0][u'*TEST-STEPS'] = []
                    stepLists[u'reportSteps'][0][u'@type'] = u'TEST-STEP-FOLDER'
                    stepLists[u'reportSteps'][0][u'*TEST-STEPS'] = []
                    del stepLists[u'reportSteps'][0][u'ORIGIN-REF']

            return stepLists

        return False

    def __ComputePlotRefPaths(self, plots, rootNode, stepShortName):
        """
        Ermittelt zu den übergebenen Plots und dem TEST-STEP die Zuweisung der Dateien über den
        RefPath der TEST-STEPS.
        :param plots: Liste der Plot-Dateien, welche im TEST-STEP gefunden wurden.
        :type plots: list
        :param rootNode: Root-Node, welcher durchsucht werden solle
        :type rootNode: Node
        :param stepShortName: eindeutiger TEST-STEP Shortname zu welchem die Plots gesucht werden
                              sollen
        :type stepShortName: str
        """
        if len(plots) > 0:

            def GetRefTestStepPath(steps):
                """
                Ermittelt den RefPath des gesuchten TEST-STEP-Shortnames.
                :param steps: Liste mit den enthaltenen TEST-STEPS auf der Ebene
                :type steps: list
                :return: None oder den Ref-Path des TEST-STEPS.
                :rtype: str
                """
                result = None
                for eachStep in steps:
                    if eachStep[u'SHORT-NAME'] == stepShortName:
                        result = eachStep[u'ORIGIN-REF'][u'#']
                        break
                    else:
                        result = GetRefTestStepPath(eachStep.get(u'*TEST-STEPS', []))
                return result

            refPath = GetRefTestStepPath(rootNode.GetList()[u'reportSteps'])
            if refPath is None:
                EPrint(u'Compute ORIGIN TEST-STEP RefPath failed!')
            else:
                if refPath not in self.__plots:
                    self.__plots[refPath] = []
                self.__plots[refPath].extend(plots)

    def __GetPlotFilesForTestStep(self, tmpDir, reportId, traceItem):
        """
        Ermittelt ob in dem aktuellen TestStep Plots enthalten sind und wenn ja, werden
        diese als Liste mit Pfadzugriff zurückgegeben.
        :param tmpDir: Verzeichnis, in welchem die Plots erstellt werden sollen.
        :type tmpDir: str
        :param reportId: eindeutige ID des TEST-STEPS, welches für die Erzeugung des Verzeichnisses
                         für die Ploterstellung verwendet wird.
        :type reportId: int
        :param traceItem: aktuelles ReportItem der TraceAnalyse.
        :type traceItem: tts.core.report.db.ReportItem.ReportItem
        :return: Liste der Pfade zu den Plots, welche zu diesem TestStep gehören.
        :rtype: list
        """
        result = []
        if traceItem.HasEntities():
            for each in traceItem.IterEntities():
                if isinstance(each, ImageEntity):
                    plotDir = os.path.join(tmpDir, u"{0}".format(reportId))
                    if not os.path.exists(plotDir):
                        os.mkdir(plotDir)
                    result.append(each.ToFile(plotDir))
        return result

    def __CreateTestStep(self, args):
        """
        Erzeugt aus den übergebenen Argumenten das TestStep Dict.
        :param args: Parameter für einen TestStep.
        :type args: dict
        :return: TestStep Objekt.
        :rtype: dict
        """
        default = {u'language': u'DE'}
        params = dict(list(default.items()) + list(args.items()))
        ret = {
            u'SHORT-NAME': u'step_{0}'.format(params[u'id']),
            u'LONG-NAME': {
                u'L-4': {
                    u'@L': params[u'language'],
                    u'#': params[u'longName'],
                }
            },
            u'CATEGORY': False,
            u'VERDICT': params[u'verdict'],
        }

        if u'category' in params:
            ret[u'CATEGORY'] = params[u'category']

        return ret
