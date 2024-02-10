from Gen.JavaParser import *
import networkx as nx
import math

class node :
    def __int__(self):
        self.number = 0
        self.next = None
        self.next_divert = None

class graph:
    def __init__(self):
        self.nodes = []
        # self.edges = {}
        self.edges_numbers = 0
        self.current_node = None
        self.last_node_numbers = 0

    def create_node_for_while(self):
        first = node()
        second = node()
        third = node()
        if self.current_node == None:
            self.current_node = first
        else:
            self.current_node.next = first
            self.edges_numbers = self.edges_numbers + 1
        #----------
        first.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        first.next = second
        self.edges_numbers = self.edges_numbers + 1
        self.nodes.append(first)
        #----------
        second.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        second.next_divert = third
        self.edges_numbers = self.edges_numbers + 1
        self.nodes.append(second)
        #----------
        third.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        third.next = first
        self.edges_numbers = self.edges_numbers + 1
        self.nodes.append(third)
        #----------
        second.next = None
        self.current_node = second
    def create_node_if_else(self):
        first = node()
        second = node()
        third = node()
        if self.current_node == None:
            self.current_node = first
        else:
            self.current_node.next = first
            self.edges_numbers = self.edges_numbers + 1
        #----------
        first.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        first.next = second
        self.edges_numbers = self.edges_numbers + 1
        self.nodes.append(first)
        first.next_divert = third
        self.edges_numbers = self.edges_numbers + 1
        #----------
        second.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        second.next = None
        self.nodes.append(second)
        #----------
        third.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        third.next = second
        self.edges_numbers = self.edges_numbers + 1
        self.nodes.append(third)
        #----------
        self.current_node = second

    def create_node_assignement(self):
        first = node()
        if self.current_node == None:
            self.current_node = first
        else:
            self.current_node.next = first
            self.edges_numbers = self.edges_numbers + 1
        #----------
        first.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        first.next = None
        self.nodes.append(first)
        #----------
        self.current_node = first







class CustomListener(ParseTreeListener):
    def __init__(self):
        self.graph = nx.DiGraph()
        self.n1_uniquieoperators = 0
        self.n2_uniqueoperands = 0
        self.N1_operators = 0
        self.N2_operands = 0
        self.operators = {}
        self.operands = {}
        self.graphh = graph()
        self.graphh.current_node = None
        self.line_count = 0

    def add_to_operators(self, operator):
        if operator in self.operators:
            self.operators[operator] = self.operators[operator] + 1
        else:
            self.operators[operator] = 1
    def add_to_operands(self, operand):
        if operand in self.operands:
            self.operands[operand] = self.operands[operand] + 1
        else:
            self.operands[operand] = 1


    def exitAdditiveExpression(self, ctx:JavaParser.AdditiveExpressionContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            middle = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()
            self.add_to_operands(left)
            self.add_to_operators(middle)
            self.add_to_operands(right)


    def exitMultiplicativeExpression(self, ctx:JavaParser.MultiplicativeExpressionContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            middle = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()
            self.add_to_operands(left)
            self.add_to_operators(middle)
            self.add_to_operands(right)

    def exitVariableDeclarator(self, ctx:JavaParser.VariableDeclaratorContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            middle = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()
            self.add_to_operands(left)
            self.add_to_operators(middle)
            self.add_to_operands(right)
        # -----
        self.graphh.create_node_assignement()

    def exitLocalVariableDeclaration(self, ctx:JavaParser.LocalVariableDeclarationContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            right = ctx.getChild(1).getText()
            self.add_to_operators(left)
            self.add_to_operands(right)
    def exitIfThenStatement(self, ctx:JavaParser.IfThenStatementContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            iff = ctx.getChild(0).getText()
            self.add_to_operators(iff)
        #----------
        self.graphh.create_node_if_else()


    def exitRelationalExpression(self, ctx:JavaParser.RelationalExpressionContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            middle = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()
            self.add_to_operands(left)
            self.add_to_operators(middle)
            self.add_to_operands(right)

    def exitAssignment(self, ctx:JavaParser.AssignmentContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            middle = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()
            self.add_to_operands(left)
            self.add_to_operators(middle)
            self.add_to_operands(right)

    def exitMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            right = ctx.getChild(1).getText()
            self.add_to_operators(left)
            self.add_to_operators(right)
    def exitMethodHeader(self, ctx:JavaParser.MethodHeaderContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            self.add_to_operators(left)
    def exitMethodDeclarator(self, ctx:JavaParser.MethodDeclaratorContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            left = ctx.getChild(0).getText()
            self.add_to_operands(left)
    def exitBasicForStatement(self, ctx:JavaParser.BasicForStatementContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            forr = ctx.getChild(0).getText()
            self.add_to_operators(forr)

        #---------
        self.graphh.create_node_for_while()
    def exitWhileStatement(self, ctx:JavaParser.WhileStatementContext):
        self.graphh.create_node_for_while()

    def exitPostIncrementExpression(self, ctx:JavaParser.PostIncrementExpressionContext):
        if ctx.getChildCount() == 1:
            pass
        if (ctx.getChildCount() > 1):
            id = ctx.getChild(0).getText()
            right = ctx.getChild(1).getText()
            self.add_to_operands(id)
            self.add_to_operators(right)


    def exitCompilationUnit(self, ctx: JavaParser.CompilationUnitContext):
        start_line = ctx.start.line
        stop_line = ctx.stop.line

        # Calculate the number of lines
        lines_in_context = stop_line - start_line + 1
        self.line_count += lines_in_context
        print(f"Lines of Code Unit : {lines_in_context}")
        print("---------------------------------------------------------------------\nHalstead’s Software Metrics \n--------------------------------------------------------------------- ")
        # print(self.operators)
        print(f"The operators table is : {self.operators}")
        # print(self.operands)
        print(f"The operands table is : {self.operands}")
        self.n1_uniquieoperators = len(self.operators)
        self.n2_uniqueoperands = len(self.operands)
        print(f"n1 = {self.n1_uniquieoperators}")
        print(f"n2 = {self.n2_uniqueoperands}")
        # for i in self.operators:
        #     operators_sum = operators_sum + i
        # for i in self.operands:
        #     operands_sum = operands_sum + i
        self.N1_operators = sum(self.operators.values())
        self.N2_operands = sum(self.operands.values())
        print(f"N1 = {self.N1_operators}")
        print(f"N2 = {self.N2_operands}")
        print(f"Program vocabulary = {self.n1_uniquieoperators + self.n2_uniqueoperands}")
        print(f"Vocabulary = {self.N1_operators + self.N2_operands}")
        print(f"Program length = {self.N1_operators + self.N2_operands}")
        print(f"Length = {self.N1_operators + self.N2_operands}")
        print(f"Calculated program length = {self.n1_uniquieoperators * math.log(self.n1_uniquieoperators,2) + self.n2_uniqueoperands * math.log(self.n2_uniqueoperands,2)}")
        print(f"The formula for Voulume is : Volume = (N1 + N2) * log2(n1 + n2)")
        print(f"Volume = {(self.N1_operators + self.N2_operands) * (math.log(self.n1_uniquieoperators + self.n2_uniqueoperands,2))}")
        print(f"The formula for Difficulty is : (n1/2) * (N2/n2)")
        print(f"Difficulty = {(self.n1_uniquieoperators/2) * (self.N2_operands/self.n2_uniqueoperands)}")
        print(f"The formula for Effort is : Effort = Difficulty * Volume")
        print(f"Effort = {(self.n1_uniquieoperators/2) * (self.N2_operands/self.n2_uniqueoperands) * ((self.N1_operators + self.N2_operands) * (math.log(self.n1_uniquieoperators + self.n2_uniqueoperands,2)))}")
        print(f"The formula for Time is : Time = Effort / 18")
        print(f"Time = {(self.n1_uniquieoperators/2) * (self.N2_operands/self.n2_uniqueoperands) * ((self.N1_operators + self.N2_operands) * (math.log(self.n1_uniquieoperators + self.n2_uniqueoperands,2))) / 18}")
        print(f"The formula for Size is : Size = Effort / 3000")
        print(f"Size = {(self.n1_uniquieoperators/2) * (self.N2_operands/self.n2_uniqueoperands) * ((self.N1_operators + self.N2_operands) * (math.log(self.n1_uniquieoperators + self.n2_uniqueoperands,2))) / 3000}")
        # print("---------------------------------------------------------------------\nMcCabe’s Cyclomatic complexity metrics")
        # print(f"Number of nodes = {self.graphh.last_node_numbers}")
        # print(f"Number of edges = {self.graphh.edges_numbers}")
        # print(f"Number of proper sub graphs = {self.graphh.last_node_numbers - self.graphh.edges_numbers + 2}")
        # print(f"The formula for calculating the cyclomatic complexity = The number of edges - The number of nodes + 2")
        # print(f"Cyclomatic complexity = {self.graphh.edges_numbers - self.graphh.last_node_numbers + 2}")
        # print(f"The essential complexity proposed by McCable = The cyclomatic complexity - The number of proper sub graphs")
        # print(f"Essential complexity = {self.graphh.edges_numbers - self.graphh.last_node_numbers + 2 - (self.graphh.last_node_numbers - self.graphh.edges_numbers + 2)}")
        print("---------------------------------------------------------------------")
        print("---------------------------------------------------------------------\n\n")




    def flexbility_factcor(self):
        print("The Software Quality Factor is: *Flexibility*")
        print(f"The Cyclomatic Complexity Metric is: {self.graphh.edges_numbers - self.graphh.last_node_numbers + 2} ")
        print(f"The Lines of Code Metric is: {self.line_count}")
        halsted_volume = (self.N1_operators + self.N2_operands) * (
            math.log(self.n1_uniquieoperators + self.n2_uniqueoperands, 2))
        Cyclomatic = self.graphh.edges_numbers - self.graphh.last_node_numbers + 2
        print(f"The Maintainability Index (MI) Metric is: {171 - 5.2 * math.log(halsted_volume , 2) - 0.23 * Cyclomatic - math.log(self.line_count, 2) }")
        print(
            f"The McCabe's Cyclomatic Complexity (MCC): {self.graphh.edges_numbers - self.graphh.last_node_numbers + 2}")
        print("---------------------------------------------------------------------")
        print("---------------------------------------------------------------------\n\n")


    def complexity_factor(self):
        halsted_volume = (self.N1_operators + self.N2_operands) * (
            math.log(self.n1_uniquieoperators + self.n2_uniqueoperands, 2))
        Cyclomatic = self.graphh.edges_numbers - self.graphh.last_node_numbers + 2

        print("The Software Quality Factor is: *Complexity*")
        print(f"The Cyclomatic Complexity Metric is: {self.graphh.edges_numbers - self.graphh.last_node_numbers + 2} ")
        print(f"The Halsted Volume Metric is: {halsted_volume}")
        print(
            f"The McCabe's Cyclomatic Complexity (MCC): {self.graphh.edges_numbers - self.graphh.last_node_numbers + 2}")
        print(
            f"The Maintainability Index (MI) Metric is: {171 - 5.2 * math.log(halsted_volume, 2) - 0.23 * Cyclomatic - math.log(self.line_count, 2)}")
        print(f"The Lines of Code Metric is: {self.line_count}")
        print("---------------------------------------------------------------------")
        print("---------------------------------------------------------------------\n\n")







