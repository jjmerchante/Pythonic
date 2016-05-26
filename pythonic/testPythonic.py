import pythonic
import unittest
import tests


def readFile(fileName):
    code = ''
    with open(fileName, 'rt') as file:
        code = file.read()
    return code;


class individualPythonicTests(unittest.TestCase):
    def testfindLargeTry(self):
        code = readFile("tests/largeTry.py")
        result = pythonic.findLargeTry(code)
        self.assertEqual(len(result), 1)

    def testfindDecorators(self):
        code = readFile("tests/decorators.py")
        result = pythonic.findDecorators(code)
        self.assertEqual(len(result), 1)

    def testfindMagicMethods(self):
        code = readFile("tests/magicMethods.py")
        result = pythonic.findMagicMethods(code)
        self.assertEqual(len(result), 3)

    def testfindGenerators(self):
        code = readFile("tests/generator.py")
        result = pythonic.findGenerators(code)
        self.assertEqual(len(result), 1)

    def testfindListCompr(self):
        code = readFile("tests/listComprehension.py")
        result = pythonic.findListCompr(code)
        self.assertEqual(len(result), 1)

    def testfindMain(self):
        code = readFile("tests/testmain.py")
        result = pythonic.findMain(code)
        self.assertEqual(len(result), 1)

    def testcheckBadLoopCollect(self):
        code = readFile("tests/badLoopCollection.py")
        result = pythonic.checkBadLoopCollect(code)
        self.assertEqual(len(result), 1)

    def testcheckNotRange(self):
        code = readFile("tests/badrange.py")
        result = pythonic.checkNotRange(code)
        self.assertEqual(len(result), 1)

    def testfindCallFunctEqual(self):
        code = readFile("tests/callFunctKeywords.py")
        result = pythonic.findCallFunctEqual(code)
        self.assertEqual(len(result), 2)

    def testfindNamedtuple(self):
        code = readFile("tests/collectionsTest.py")
        result = pythonic.findNamedtuple(code)
        self.assertEqual(len(result), 2)

    def testfindUpdateVariables1Line(self):
        code = readFile("tests/updateVariables1Line.py")
        result = pythonic.findUpdateVariables1Line(code)
        self.assertEqual(len(result), 2)

    def testfindYield(self):
        code = readFile("tests/yieldUse.py")
        result = pythonic.findYield(code)
        self.assertEqual(len(result), 1)

    def testfindWith(self):
        code = readFile("tests/withUse.py")
        result = pythonic.findWith(code)
        self.assertEqual(len(result), 1)

    def testfindLambda(self):
        code = readFile("tests/lambdaUse.py")
        result = pythonic.findLambda(code)
        self.assertEqual(len(result), 1)

    def testfindNestedFunctions(self):
        code = readFile("tests/nestedFunctions.py")
        result = pythonic.findNestedFunctions(code)
        self.assertEqual(len(result), 1)

    def testfindAssert(self):
        code = readFile("tests/assertUse.py")
        result = pythonic.findAssert(code)
        self.assertEqual(len(result), 1)

    def testfindFinally(self):
        code = readFile("tests/largeTry.py")
        result = pythonic.findFinally(code)
        self.assertEqual(len(result), 1)

    def testfindUseMapFilterReduce(self):
        code = readFile("tests/filter_map_reduce.py")
        mapfiltReduc = pythonic.findUseMapFilterReduce(code)
        for idiom in mapfiltReduc:
            self.assertEqual(len(idiom), 1)

    def testfindDocstring(self):
        code = readFile('tests/docString.py')
        result = pythonic.findDocstring(code)
        self.assertEqual(len(result), 9)

    def testfindDeque(self):
        code = readFile('tests/collectionsTest.py')
        result = pythonic.findDeque(code)
        self.assertEqual(len(result), 2)

    def testfindDefaultDict(self):
        code = readFile('tests/collectionsTest.py')
        result = pythonic.findDefaultDict(code)
        self.assertEqual(len(result), 2)

    def testfindOrderedDict(self):
        code = readFile('tests/collectionsTest.py')
        result = pythonic.findOrderedDict(code)
        self.assertEqual(len(result), 2)


# Test a file obtained from Facebook's github
class IdiomTests1(unittest.TestCase):
    def setUp(self):
        self.code = ""
        with open('tests/web.py', 'rt') as f1:
            self.code = f1.read()

    def testfindLargeTry(self):
        result = pythonic.findLargeTry(self.code)
        self.assertEqual(len(result), 3)

    def testfindDecorators(self):
        result = pythonic.findDecorators(self.code)
        self.assertEqual(len(result), 21)

    def testfindMagicMethods(self):
        result = pythonic.findMagicMethods(self.code)
        self.assertEqual(len(result), 3)

    def testfindGenerators(self):
        result = pythonic.findGenerators(self.code)
        self.assertEqual(len(result), 10)

    def testfindListCompr(self):
        result = pythonic.findListCompr(self.code)
        self.assertEqual(len(result), 4)

    def testfindMain(self):
        result = pythonic.findMain(self.code)
        self.assertEqual(len(result), 0)

    def testcheckBadLoopCollect(self):
        result = pythonic.checkBadLoopCollect(self.code)
        self.assertEqual(len(result), 0)

    def testcheckNotRange(self):
        result = pythonic.checkNotRange(self.code)
        self.assertEqual(len(result), 0)

    def testfindCallFunctEqual(self):
        result = pythonic.findCallFunctEqual(self.code)
        self.assertEqual(len(result), 43)

    def testfindNamedtuple(self):
        result = pythonic.findNamedtuple(self.code)
        self.assertEqual(len(result), 0)

    def testfindUpdateVariables1Line(self):
        result = pythonic.findUpdateVariables1Line(self.code)
        self.assertEqual(len(result), 1)

    def testfindYield(self):
        result = pythonic.findYield(self.code)
        self.assertEqual(len(result), 5)

    def testfindWith (self):
        result = pythonic.findWith(self.code)
        self.assertEqual(len(result), 6)

    def testfindLambda (self):
        result = pythonic.findLambda(self.code)
        self.assertEqual(len(result), 3)

    def testfindNestedFunctions (self):
        result = pythonic.findNestedFunctions(self.code)
        self.assertEqual(len(result), 4)

    def testfindAssert (self):
        result = pythonic.findAssert(self.code)
        self.assertEqual(len(result), 13)

    def testfindFinally (self):
        result = pythonic.findFinally(self.code)
        self.assertEqual(len(result), 0)

    def testfindUseMapFilterReduce(self):
        mapfiltReduc = pythonic.findUseMapFilterReduce(self.code)
        for idiom in mapfiltReduc:
            self.assertEqual(len(idiom), 0)

    def testfindDocstring(self):
        result = pythonic.findDocstring(self.code)
        self.assertEqual(len(result), 115)

    def testfindDeque(self):
        result = pythonic.findDeque(self.code)
        self.assertEqual(len(result), 0)

    def testfindDefaultDict(self):
        result = pythonic.findDefaultDict(self.code)
        self.assertEqual(len(result), 0)

    def testfindOrderedDict(self):
        result = pythonic.findOrderedDict(self.code)
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
