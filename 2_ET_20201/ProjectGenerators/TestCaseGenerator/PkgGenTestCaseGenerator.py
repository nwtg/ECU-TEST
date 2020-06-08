# -*- coding: utf-8 -*-

import openpyxl
import os
import re


try:
    from lib.project.PackageGenerator import PackageGenerator
except ImportError:
    from PackageGenerator import PackageGenerator


class PkgGenTestCaseGenerator(PackageGenerator):

    ID = 'f6b6bd00-8b65-43dc-8f15-2c06f43afefe'
    NAME = 'Test Case Generator'
    DESCRIPTION = 'Reads an Excel file and generates test cases'
    SERIALIZE = {'filename': ('FILENAME', 'string', r''),
                 'sheetname': ('SHEETNAME', 'string', '')}

    def __init__(self):
        self.filename = r''
        self.sheetname = 'test cases'

        self._testCases = []

        self.objectApi = None

    def SetFilename(self, name):
        self.filename = name

    def GetFilename(self):
        return self.filename

    def GetAbsoluteFilename(self):
        return os.path.join(self.api.GetSetting('workspacePath'), self.filename)

    def GetDialog(self):
        from .DlgFileSelect import DlgFileSelect
        return DlgFileSelect(None, self, self.api.GetSetting('workspacePath'))

    def PreGeneration(self):
        wb = openpyxl.load_workbook(self.GetAbsoluteFilename())
        sheet = wb[self.sheetname]

        for row in sheet.iter_rows():
            _id, _type, name, actions, expectedResult = [cell.value for cell in row]

            if _type == "Test Case":
                curTestCase = TestCase(_id, name)
                self._testCases.append(curTestCase)
            elif _type == "Precondition":
                testStep = TestStep(_id, actions, expectedResult)
                curTestCase.precondition = testStep
            elif _type == "Test Step":
                testStep = TestStep(_id, actions, expectedResult)
                curTestCase.testSteps.append(testStep)
            elif _type == "Postcondition":
                testStep = TestStep(_id, actions, expectedResult)
                curTestCase.postcondition = testStep

    def GenerationIterator(self):
        # generate test cases
        for testCase in self._testCases:
            yield self._GenerateTestCase(testCase)

        self.objectApi = None

    def _GenerateTestCase(self, testCase):
        # cycle data and package generator object
        cd = self.CreateCycleData()
        self.objectApi = cd.objectApi

        # set package name
        cd.SetName("%s %s" % (testCase.id, testCase.name))

        if testCase.HasPrecondition():
            precondition = self.objectApi.PackageApi.TestStepApi.CreateTsPreconditionBlock()
            cd.packageInstance.AppendTestStep(precondition)
            self.GenerateTestStep(precondition, testCase.precondition)

        if testCase.HasTestSteps():
            actionBlock = self.objectApi.PackageApi.TestStepApi.CreateTsBlock()
            actionBlock.SetActionColumnText('Action')
            cd.packageInstance.AppendTestStep(actionBlock)

            for testStep in testCase.testSteps:
                self.GenerateTestStep(actionBlock, testStep)

        if testCase.HasPostcondition():
            postcondition = cd.objectApi.PackageApi.TestStepApi.CreateTsPostconditionBlock()
            cd.packageInstance.AppendTestStep(postcondition)
            self.GenerateTestStep(postcondition, testCase.postcondition)

        return cd

    def GenerateTestStep(self, parent, testStep):
        block = self.objectApi.PackageApi.TestStepApi.CreateTsBlock()

        if testStep.expectation:
            block.SetValueColumnText(testStep.expectation)
        block.SetActionColumnText(testStep.GetActionColumnText())

        parent.AppendTestStep(block)

        # generate action steps
        for actionString in [a for a in testStep.action.split('\n') if a]:
            if "=" in actionString:
                referenceName, value = actionString.split("=")
                block.AppendTestStep(self.__GenerateTsWrite(referenceName, value))
            elif "Wait" in actionString:
                block.AppendTestStep(self.__GenerateTsWait(actionString))
            else:
                block.AppendTestStep(self.__GenerateTsToDo(actionString))

        # generate expectation steps
        for expectation in [e for e in testStep.expectation.split('\n') if e]:
            tsRead = self.__GenerateTsRead(expectation)
            if tsRead is not None:
                block.AppendTestStep(tsRead)

        return block

    def __GenerateTsWrite(self, referenceName, value):
        unit = ''

        # check if value has unit
        # TODO: currently only integers allowed
        matchObj = re.match(r"(\d+)(\D+)", value)
        if matchObj is not None:
            value = int(matchObj.group(1))
            unit = matchObj.group(2)

        genericMappingItem = self.objectApi.PackageApi.MappingApi.CreateGenericMappingItem(
            referenceName=referenceName)
        testStep = self.objectApi.PackageApi.TestStepApi.CreateTsWrite(genericMappingItem)
        testStep.SetUnit(unit, "z")
        testStep.SetValue(value)
        return testStep

    def __GenerateTsWait(self, actionString):
        matchObj = re.match(r"Wait (\d+) (\D+)", actionString)

        value = '0'
        unit = 'ms'

        if matchObj is not None:
            value = int(matchObj.group(1))
            unit = matchObj.group(2)

        testStep = self.objectApi.PackageApi.TestStepApi.CreateTsWait()
        testStep.SetDelay(value, unit)
        return testStep

    def __GenerateTsToDo(self, actionString):
        newTestStep = self.objectApi.PackageApi.TestStepApi.CreateTsToDo()
        newTestStep.SetComment(
            "Test step '%s' could not be generated automatically." % actionString)
        return newTestStep

    def __GenerateTsRead(self, actionString):
        testStep = None

        matchObj = re.match(r'(\w+)(>=|<=|>|<|=|==)(\d+)\s*([a-z]+)?\s*(?:\(within (.+?) \D+\))?',
                            actionString)
        if matchObj:
            referenceName, relation, value, unit, waitUntilTimeout = matchObj.groups()

            if relation == '=':
                relation = '=='

            mappingItem = self.objectApi.PackageApi.MappingApi.CreateGenericMappingItem(
                referenceName=referenceName)
            testStep = self.objectApi.PackageApi.TestStepApi.CreateTsRead(mappingItem)
            testStep.SetExpectationExpression('value{}{}'.format(relation, value))

            if unit is not None:
                testStep.SetUnit(unit)

            if waitUntilTimeout is not None:
                testStep.SetTimeOptionWaitUntilTrue(waitUntilTimeout)

        return testStep

    def PostGeneration(self):
        pass


class TestCase(object):
    def __init__(self, identifier, name):
        self.id = identifier
        self.name = name
        self.precondition = None
        self.testSteps = []
        self.postcondition = None

    def HasPrecondition(self):
        return self.precondition is not None

    def HasTestSteps(self):
        return len(self.testSteps) > 0

    def HasPostcondition(self):
        return self.postcondition is not None


class TestStep(object):
    def __init__(self, identifier, action, expectation):
        self.id = identifier
        self.action = action or ''
        self.expectation = expectation or ''

    def GetActionColumnText(self):
        return '{}: {}'.format(self.id, self.action if self.action else self.expectation)
