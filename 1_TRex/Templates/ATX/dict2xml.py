# -*- coding: utf-8 -*-

'''
Created on 07.02.2014

@author: Christoph Groß <christoph.gross@tracetronic.de>
'''
import sys

from lxml import etree
from collections import OrderedDict

from log import EPrint

if sys.version_info < (3,):
    str = unicode


class dict2xml(object):
    '''
    Erzeugt aus dem übergebenen Dictonary oder Liste ein entsprechendes XML Dokument.
    '''

    def __init__(self, reportTrfFile, version, data, pretty_print=False):
        '''
        Konstruktor.
        @param reportTrfFile: Pfad der TRF-Datei, welche gearde verarbeitet wird, dies ist wichtig
                              im Fehlerfall, damit eine Zuweisung möglich ist.
        @type reportTrfFile: str
        @param version: Version des Generators und gleichzeitig die unterstützte API-Version.
        @type version: str
        @param data: zu serialisierendes Daten-Objekt.
        @type data: dict oder list
        @param pretty_print: Formatierte Ausgabe.
        @type pretty_print: boolean
        '''
        self.__reportTrfFile = reportTrfFile
        self.__version = version
        self.__data = data
        self.__pretty_print = pretty_print

    def CreateXmlFile(self, xmlFilePath):
        '''
        Erstellt auf Grundlages des übergebenen Pfades eine ATX-XML Datei auf Grundlage der
        im Konstruktor angegebenen Daten.
        @param xmlFilePath: Pfad
        @type xmlFilePath: str
        '''
        with open(xmlFilePath, u'wb') as file_handler:
            file_handler.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
            et = etree.ElementTree(self.__GetXmlRoot(self.__data))
            et.write(file_handler)

    def GetXmlString(self):
        '''
        Gibt das serialisierte XML Dokument zurück.
        @return: XML Dokument.
        @rtype: str
        '''
        return self.__Serialize(self.__data, self.__pretty_print)

    def __Serialize(self, data, pretty_print):
        '''
        Serialisiert das Objekt.
        @param data: zu serialisierendes Daten-Objekt.
        @type data: dict oder list
        @param pretty_print: Formatierte Ausgabe.
        @type pretty_print: boolean
        @return: XML Dokument.
        @rtype: str
        '''
        root = self.__GetXmlRoot(data)
        return u'<?xml version="1.0" encoding="UTF-8"?>\n' + (
            etree.tostring(root, pretty_print=pretty_print, encoding=u'UTF-8'))

    def __GetXmlRoot(self, data):
        '''
        Erstellt den Root-Knoten der ATX-XML und hängt die Daten unterhalb des Root-Knotens an.
        @param data: Daten, welche als XML rausgeschrieben werden sollen.
        @type data: dict oder list
        @return: Root-Konten des ATX-XML Dokumentes
        @rtype: etree.Element
        '''
        try:
            root = etree.Element(u'ATX', nsmap={
                u'xsi': u'http://www.w3.org/2001/XMLSchema-instance',
                None: u'http://www.asam.net/schema/ATX/r1.0'})
            root.append(etree.Comment(u"Generator version: {0}".format(self.__version)))
            self.__AddElements(root, data)
        except BaseException as ex:
            import traceback
            traceback.print_exc()
            EPrint(u"Error on: {0}: {1}".format(self.__reportTrfFile, ex))
        return root

    def __AddElements(self, parent, data):
        '''
        Fügt ein XML Element zum Parent hinzu.
        @param parent: Parent Objekt des Knotens.
        @type parent: etree.Element
        @param data: Daten-Objekt des Knotens.
        @type data: dict oder list oder str oder int oder boolean
        '''
        dType = type(data)
        if dType == dict or dType == OrderedDict:
            for k, v in data.items():
                if v is None:
                    continue
                if k[0] == u'@':  # Attribut des Knotens
                    parent.set(k[1:], v)
                elif k == u'#':  # Text Value des Knotens
                    parent.text = etree.CDATA(str(v))
                elif k[0] == u'*':  # Knoten ist eine Liste
                    self.__AddElements(parent, v)
                else:
                    child = etree.SubElement(parent, k)
                    self.__AddElements(child, v)
        elif dType == list:
            for each in data:
                child = etree.SubElement(parent, each.pop(u'@type'))
                self.__AddElements(child, each)
        elif dType is type(None):
            pass
        else:
            parent.text = etree.CDATA(str(data))
