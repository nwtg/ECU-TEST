# -*- coding: utf-8 -*-

'''
Created on 27.10.2014

@author: Philipp
'''

import os
from lxml import etree


class Config(object):
    '''
    Klasse kapselt die ReportApi-Konfigurationsaufrufe.
    Dies ist notwendig, da bei einem AutoUpdate nicht
    die neuen ReportApi Konfigurationen im Moment des AutoUpdates zur Verfügung stehen und beim
    Aufruf von GetSetting kann über diesen Wrapper der Default-Wert ermittelt werden.
    '''

    def __init__(self):
        '''
        Konstruktor.
        '''

    @staticmethod
    def Cast2Int(value, default=0):
        '''
        Nimmt einen Cast von einem String zu einem Integer vor.
        Wenn ein Cast nicht möglich ist, wird der Default-Wert zurückgegeben.
        @param value: Wert der zu einem Integer gecastet werden soll.
        @type value: str
        @param default: der Default-Wert welcher zurückgegeben werden soll, wenn ein Cast nicht
                        möglich ist.
        @type default: int
        @return: ermittelter Wert
        @rtype: int
        '''
        try:
            return int(value)
        except ValueError:
            return default
        except TypeError:
            return default

    @staticmethod
    def GetSetting(reportApi, name):
        '''
        Ermittelt zunächst in der ReportApi den jeweiligen Setting-Wert, ist die Setting unbekannt,
        dann wird versucht der Default-Wert aus der aktuellen config.xml zu lesen.
        @param reportApi: ReportApi, aus welcher der Wert für die Setting zurückgegeben werden soll
        @type reportApi: tts.core.report.parser.ReportApi
        @param name: Name der Setting
        @type name: str
        @return: gefundener Default-Wert oder None
        @rtype: str, boolean, integer oder None
        '''
        reportApiValue = reportApi.GetSetting(name)

        # Wenn unbekannt, dann versuchen aus der aktuellen config.xml zu ermitteln.
        if reportApiValue is None:
            return Config.__GetDefaultValue(name)

        return reportApiValue

    @staticmethod
    def __GetDefaultValue(name):
        '''
        Ermittelt zu der übergebenen Settings (name) den Default-Wert.
        @param name: Name der Settings in der config.xml, aus welcher der Default-Wert ermittelt
                     werden soll.
        @type name: str
        @return: gefundener Default-Wert oder None
        @rtype: str, boolean, integer oder None
        '''
        # beiliegende config.xml einlesen für XPath
        atxDir = os.path.dirname(os.path.realpath(__file__))
        doc = etree.parse(os.path.join(atxDir, u'config.xml'))

        # Default-Wert der Setting via XPath ermitteln
        values = doc.xpath(u"//SETTING[@name='{0}']/attribute::default".format(name))

        # Wenn Setting unbekannt, dann None zurückgeben als Default-Wert
        if len(values) == 0:
            return None

        # Ersten gefundenen Wert zurückgeben
        return values[0]
