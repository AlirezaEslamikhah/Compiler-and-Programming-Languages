import math
from antlr4 import *
from Gen.JavaParserListener import *
from Gen.JavaParser import *
from Code.CustomAlirezaListener import CustomListener


class ReadabilityMetricListener(JavaParserListener):
    def __init__(self, parse_tree):
        self.line_count = 0
        self.graph_listener = CustomListener(print_option=False)
        walker = ParseTreeWalker()
        walker.walk(self.graph_listener, parse_tree)

    def exitCompilationUnit(self, ctx: JavaParser.CompilationUnitContext):
        start_line = ctx.start.line
        stop_line = ctx.stop.line

        # Calculate the number of lines
        lines_in_context = stop_line - start_line + 1
        self.line_count += lines_in_context
        print(
            "-------------------------\nReadability’s Software Metrics \n-----------------------------")
        # Walston & Felix ratio formula of document pages as: D = 49 * L, where:
        # D = Number of pages of document and L = Number of 1000 lines of code
        L = self.line_count / 1000

        D = 49 * (L ** 1.01)

        print(f'Metrics\'s formula: D = 49 * (L ** 1.01)')
        print(f'Number of code lines = {self.line_count}')
        print(f'L: Number of 1000 lines of code = {L}')
        print(f'D: Number of pages of the document = {D}')

    def testability_factor(self):
        # calculate Cyclomatic Complexity(V(G)): V(G) = E - N + 2 * P
        # graph_listener = CustomListener()

        E = self.graph_listener.graphh.edges_numbers
        N = len(self.graph_listener.graphh.nodes)
        P = 1  # for a single program
        V = E - N + 2 * P

        print('---------------------------------------------------')
        print("The First Software Quality Factor is *Testability*")
        print(f'Cyclomatic Complexity of code = {V}')

        # calculate the LOC metric
        LOC = self.line_count
        print(f'Number of Lines in the code = {LOC}')

    def integrity_factor(self):
        # calculate Dependency Cyclomatic Complexity(V(G)): V(G) = E / N + 1
        # graph_listener = CustomListener()
        E = self.graph_listener.graphh.edges_numbers
        N = len(self.graph_listener.graphh.nodes)
        DCC = E / N + 1

        print('---------------------------------------------------')
        print("The Second Software Quality Factor is *Integrity*")
        print(f'Dependency Cyclomatic Complexity of code = {DCC}')

        # calculate Maintainability Index (MI):
        # MI = 171 − 5.2 × ln(Halstead Volume) − 0.23 × (Cyclomatic Complexity) − 16.2 × ln(LOC)
        halstead_volume = (self.graph_listener.N1_operators + self.graph_listener.N2_operands) * (
            math.log(self.graph_listener.n1_uniquieoperators + self.graph_listener.n2_uniqueoperands, 2))

        CC = self.graph_listener.graphh.edges_numbers - self.graph_listener.graphh.last_node_numbers + 2

        MI = 171 - 5.2 * math.log(halstead_volume, 2) - 0.23 * CC - math.log(self.line_count, 2)

        print(f"The Maintainability Index (MI) Metric is: {MI}")

