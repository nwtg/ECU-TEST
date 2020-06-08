# -*- coding: utf-8 -*-

'''
Created on 20.11.2014

@author: Philipp
'''

import os
import shutil
import unittest
import tempfile

from mockito import mock, when

try:
    # FakeApiModules importieren, damit alte Pfade gefunden werden
    import tts.core.application.FakeApiModules  # @UnusedImport
except ImportError:
    # FakeApiModules erst ab ECU-TEST 8.1 verfügbar
    pass
from .UploadManager import UploadManager


class UploadManagerTest(unittest.TestCase):

    def setUp(self):
        self._oldTempDir = tempfile.gettempdir()
        unittest.TestCase.setUp(self)
        import gettext
        gettext.NullTranslations().install()
        if os.getenv(u"COMPUTERNAME", u"").lower() in (u"tt-ddvs06", u"tt-ddvs19"):
            with tempfile._once_lock:
                if not os.path.isdir(r"D:\temp"):
                    os.mkdir(r"D:\temp")
                tempfile.tempdir = r"D:\temp"

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        with tempfile._once_lock:
            tempfile.tempdir = self._oldTempDir
            shutil.rmtree(r"D:\temp", ignore_errors=True)

    def testUrlWithContextPath(self):
        reportApiMock = mock()
        um = UploadManager(reportApiMock, u"1.5.1", u'file-upload', u"BigFile.zip", u"DummyPath",
                           useHttps=True, contextPath=u"test-guide")
        self.assertEqual(um.GetTargetUrl(),
                          u"https://127.0.0.1:8085/test-guide/api/upload-file?apiVersion=1.5.1&authKey=&projectId=1&async=true")

    def testStatusUrlWithContextPath(self):
        reportApiMock = mock()
        um = UploadManager(reportApiMock, u"1.5.1", u'file-upload', u"BigFile.zip", u"DummyPath",
                           useHttps=True, contextPath=u"test-guide")
        self.assertEqual(um._GetStatusUrl(u"/api/upload-file/status/42"),
                          u"https://127.0.0.1:8085/test-guide/api/upload-file/status/42?authKey=")

    def testStatusUrlWithoutContextPath(self):
        reportApiMock = mock()
        um = UploadManager(reportApiMock, u"1.5.1", u'file-upload', u"BigFile.zip", u"DummyPath",
                           useHttps=True)
        self.assertEqual(um._GetStatusUrl(u"/api/upload-file/status/42"),
                          u"https://127.0.0.1:8085/api/upload-file/status/42?authKey=")

    def testHttpsUrl(self):
        reportApiMock = mock()
        um = UploadManager(reportApiMock, u"1.5.1", u'file-upload', u"BigFile.zip", u"DummyPath",
                           useHttps=True)
        self.assertEqual(um.GetTargetUrl(),
                          u"https://127.0.0.1:8085/api/upload-file?apiVersion=1.5.1&authKey=&projectId=1&async=true")

    def testDefaultHttpUrl(self):
        reportApiMock = mock()
        um = UploadManager(reportApiMock, u"1.5.1", u'file-upload', u"BigFile.zip", u"DummyPath")
        self.assertEqual(um.GetTargetUrl(),
                          u"http://127.0.0.1:8085/api/upload-file?apiVersion=1.5.1&authKey=&projectId=1&async=true")

    def testHttpAuthKeyUrl(self):
        # ARRANGE
        authKey = u"egBnG8EOnkGttaW0yEkon%2B%2BzSh7RUCW5Id6ze8gnjrTayPKEkOhxq1pmx4Pgj8chH35ZnCniSwwYscK%2Boej8aqOU0zE4skvFnCtdkitP4o4zrrP2Xy%2BIm7C6XBuju7XQ8KHstUyLagzSY3QKKhbBlz1gPll%2FFINg%2BX%2BXjeoas2ftpI8%2FW%2FhfuQPqaFavstq1uxKeDg0U2h8cJsLvDxKj4FeQCqBaPdOwDduQJgwZzW7vZc43tTp%2BmJdRqAuRveYqPo1zWpX%2FinL2JHnft2g4nV0OLpPJ0zpBUwk%2BKiVunww%3D"
        reportApiMock = mock()
        when(reportApiMock).GetSetting(u'uploadAuthenticationKey').thenReturn(authKey)
        # ACT
        um = UploadManager(reportApiMock, u"1.5.1", u'file-upload', u"BigFile.zip", u"DummyPath")
        # ASSERT
        self.assertEqual(um.GetTargetUrl(),
                          (u"http://127.0.0.1:8085/api/upload-file"
                           u"?apiVersion=1.5.1&authKey={0}&projectId=1&async=true").format(authKey))

    def testBigFileUpload(self):
        '''
        Prüfung das kein MemoryError beim Upload von großen Dateien erfolgt.
        '''
        # ARRANGE
        reportApiMock = mock()
        when(reportApiMock).GetReportDir().thenReturn(tempfile.gettempdir())

        fileTemp = tempfile.NamedTemporaryFile(prefix=u"bigUploadFile", delete=False)
        try:
            # Beispieldatei mit > 1000MB erzeugen
            with open(fileTemp.name, u"wb") as out:
                out.seek((1024 * 1024 * 1024) - 1)
                out.write(b'\0')

            um = UploadManager(reportApiMock, u"1.5.1", u'file-upload',
                               u"BigFile.zip", fileTemp.name, url=u"localhostInvalidUrl")

            # ACT
            try:
                # ASSERT
                # Es darf kein Memory Error auftreten beim Upload.
                self.assertTrue(not um.StartUpload(),
                                u"Upload von falscher URL darf nicht möglich sein.")
            except MemoryError:
                self.fail(u"MemoryError ist aufgetreten.")

        finally:
            fileTemp.close()
            os.remove(fileTemp.name)


if __name__ == "__main__":
    unittest.main()
