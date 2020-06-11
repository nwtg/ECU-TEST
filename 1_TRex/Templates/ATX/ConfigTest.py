# -*- coding: utf-8 -*-

'''
Created on 27.10.2014

@author: Philipp
'''

import unittest
from mockito import mock, when

from .Config import Config


class ConfigTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetUnknownSetting(self):
        '''
        Prüft das bei unbekannten Settings (auch in der config.xml) ein None zurückgegeben wird.
        '''
        # ARRANGE
        settingName = u'unknownSetting'
        reportApiMock = mock()
        when(reportApiMock).GetSetting(settingName).thenReturn(None)

        # ACT
        value = Config.GetSetting(reportApiMock, settingName)

        # ASSERT
        self.assertEqual(None, value,
                         (u"Der Settingswert sollte None lauten für unbekannt Settings."))

    def testGetValidSetting(self):
        '''
        Prüft ob bei valider Setting diese auch korrekt zurückgegeben wird.
        '''
        # ARRANGE
        settingName = u'serverPort'
        expectedValue = 8085
        reportApiMock = mock()
        when(reportApiMock).GetSetting(settingName).thenReturn(expectedValue)

        # ACT
        value = Config.GetSetting(reportApiMock, settingName)
        # ASSERT
        self.assertEqual(expectedValue, value,
                         (u"Der Settingswert sollte {0} lauten.").format(expectedValue))

    def testGetValidButUnknownReportApiSetting(self):
        '''
        Prüft das aus der config.xml der Default-Wert für eine gültige Settings in der config.xml
        aber noch nicht bekannte Settings in der ReportApi (Problem AutoUpdate) ermittelt wird.
        '''
        # ARRANGE
        settingName = u'serverURL'
        reportApiMock = mock()
        when(reportApiMock).GetSetting(settingName).thenReturn(None)

        # ACT
        value = Config.GetSetting(reportApiMock, settingName)
        # ASSERT
        self.assertEqual(u"127.0.0.1", value,
                         (u"Der Defaultwert der noch nicht bekannten Settings sollte aus der "
                          u"config.xml ausgelesen werden."))

if __name__ == "__main__":
    unittest.main()
