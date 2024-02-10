from Gen.JavaParserListener import JavaParserListener
import numpy as np


def hasArguments(ctx):
    # Check if the method has a formal parameter list
    methodHeader = ctx.methodHeader().methodDeclarator().formalParameterList()
    if methodHeader:
        return True
    return False


def hasReturnStatement(ctx):
    # Check if the method has a return statement
    block = ctx.methodBody().block()
    if block:
        for blockStatement in block.blockStatements().blockStatement():
            statement = blockStatement.statement()
            if statement:
                stmtWithoutTrailingSubstmt = statement.statementWithoutTrailingSubstatement()
                if stmtWithoutTrailingSubstmt and stmtWithoutTrailingSubstmt.returnStatement():
                    return True
    return False


class Albrecht(JavaParserListener):
    def __init__(self):
        self.Metrics = {
            'EI': 0,  # External Input
            'EO': 0,  # External Output
            'EQ': 0,  # External Inquiries
            'ILF': 0,  # Internal Logical File
            'EIF': 0  # External Interface File
        }
        self.EI = 0
        self.Weights = {
            'EI': {'low': 3, 'average': 4, 'high': 6},  # External Input
            'EO': {'low': 4, 'average': 5, 'high': 7},  # External Output
            'EQ': {'low': 3, 'average': 4, 'high': 6},  # External Inquiries
            'ILF': {'low': 5, 'average': 7, 'high': 10},  # Internal Logical File
            'EIF': {'low': 7, 'average': 10, 'high': 15}  # External Interface File
        }
        self.FC = self.FP = 0

        keys = ["Data Communication", "Distributed Function", "Heavily Used",
                "Configuration", "Transaction Rate", "Online Data Entry",
                "End User Efficiency", "Online Update", "Complex Processing",
                "Reusability", "Installation Ease", "Operational Ease",
                "Multiple Sites", "Facilitation of Change"]

        value = np.random.uniform(0, 5, 14)

        self.VAF = 0.65 + 0.01 * np.sum(value)

        self.c = dict(zip(keys, value))

    def calculateFC(self):
        self.FC = 0
        for key in self.Metrics:
            for weight in self.Weights[key]:
                self.FC += self.Weights[key][weight] * self.Metrics[key]

    def calculateFP(self):
        self.calculateFC()
        self.FP = self.FC * self.VAF
        print("---------------------------------------------------------------------")
        print("|{:^67}|".format('Albrecht’s Function Points Metrics'))
        print("---------------------------------------------------------------------")
        print("|{:^10}|{:^56}|".format('Metric', 'Number of Component'))
        print("---------------------------------------------------------------------")
        for key, value in self.Metrics.items():
            print("|{:^10}|{:^56}|".format(key, value))
        print("---------------------------------------------------------------------")
        print("|{:^67}|".format('General System Characteristics'))
        print("---------------------------------------------------------------------")
        print("|{:^36}|{:^30}|".format('Feature', 'Scale'))
        print("---------------------------------------------------------------------")
        for feature, value in self.c.items():
            print("|{:^36}|{:^30}|".format(feature, value))
        print("---------------------------------------------------------------------")
        print("|{:^36}|{:^30}|".format('Value Adjustments Factor (VAF)', self.VAF))
        print("|{:^36}|{:^30}|".format('Function Counts (FC)', self.FC))
        print("|{:^36}|{:^30}|".format('Function Points (FP)', self.FP))
        print("---------------------------------------------------------------------")

    def enterFormalParameter(self, ctx):
        # Count the number of input parameters as External Inputs (EIs)
        self.Metrics['EI'] += 1

    def enterNormalClassDeclaration(self, ctx):
        # Count the number of fields in the class as Internal Logical Files (ILFs)
        self.Metrics['ILF'] += 1

    def enterNormalInterfaceDeclaration(self, ctx):
        # Count the number of methods in the interface as External Interfaces (EIFs)
        self.Metrics['EIF'] += 1

    def enterPackageName(self, ctx):
        # Count the number of method invocations as External Outputs (EOs)
        if ctx.getText() == 'out':
            self.Metrics['EO'] += 1
        elif ctx.getText() == 'in':
            self.Metrics['EI'] += 1

    def enterMethodDeclaration(self, ctx):
        # Check if the method has arguments and a return statement
        if hasArguments(ctx) and hasReturnStatement(ctx):
            self.Metrics['EQ'] += 1
        elif hasReturnStatement(ctx):
            self.Metrics['EO'] += 1
