import sys
import PHP
sys.path.insert(0, "../..")

class TestingC:
    def __init__(self):
       #self.option = option;
       print("=========================================================")
       print("||                     Testing                         ||")
       print("=========================================================")

    #def showCases(self):

    def runTest_B(self):
        if sys.version_info[0] >= 3:
            raw_input = input

        testCases = ['variableDef.txt',
                     'loop_Def_ wrongGrammar.txt',
                     'string_Var_Constant_NotAllowed.txt']

        numCase = 0
        for caseScript in testCases:
            try:
                print("=================================")
                print("Case --> ", caseScript )
                f = open (caseScript,'r')
                fileContent = f.read()
                test = PHP.Lexer(fileContent)
                test.runLexA()
                numCase = numCase + 1
                print("Status -->")
                #pass
                #print("Test pass")
            except Exception as e:
                   print("ERROR !!")
            else:
                print("Test Pass !!")

    def runTest_A(self):
        if sys.version_info[0] >= 3:
            raw_input = input

        testCases = ['commentCase.txt',
                     'multiLineComment_Case.txt',
                     'variableDefCase.txt',
                     'constant_Case.txt',
                     'string_case.txt',
                     'dataTypes_Case.txt',
                     'loop&Conditions_Case.txt',
                     'imput&output_Case.txt',
                     'All_The_Instructions.txt']

        numCase = 0
        for caseScript in testCases:
            try:
                print("=================================")
                print("Case --> ", caseScript )
                f = open (caseScript,'r')
                fileContent = f.read()
                test = PHP.Lexer(fileContent)
                test.runLexA()
                numCase = numCase + 1
                print("Status -->")
                #pass
                #print("Test pass")
            except Exception as e:
                   print("ERROR :(")

            else:
                print("Test Pass !!")

        #return fileContent

testing = TestingC();
testing.runTest_A();
testing.runTest_B();
