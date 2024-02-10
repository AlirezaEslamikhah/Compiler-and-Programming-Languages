from Gen.JavaParser import *
import networkx as nx
import math
import time


class node:
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
        # ----------
        first.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        first.next = second
        self.edges_numbers = self.edges_numbers + 1
        self.nodes.append(first)
        # ----------
        second.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        second.next_divert = third
        self.edges_numbers = self.edges_numbers + 1
        self.nodes.append(second)
        # ----------
        third.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        third.next = first
        self.edges_numbers = self.edges_numbers + 1
        self.nodes.append(third)
        # ----------
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
        # ----------
        first.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        first.next = second
        self.edges_numbers = self.edges_numbers + 1
        self.nodes.append(first)
        first.next_divert = third
        self.edges_numbers = self.edges_numbers + 1
        # ----------
        second.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        second.next = None
        self.nodes.append(second)
        # ----------
        third.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        third.next = second
        self.edges_numbers = self.edges_numbers + 1
        self.nodes.append(third)
        # ----------
        self.current_node = second

    def create_node_assignement(self):
        first = node()
        if self.current_node == None:
            self.current_node = first
        else:
            self.current_node.next = first
            self.edges_numbers = self.edges_numbers + 1
        # ----------
        first.number = self.last_node_numbers + 1
        self.last_node_numbers = self.last_node_numbers + 1
        first.next = None
        self.nodes.append(first)
        # ----------
        self.current_node = first


class HenryMetricListener(ParseTreeListener):
    def __init__(self):
        self.graph = nx.DiGraph()
        # IFC Henry's
        self.Fan = 0
        self.Fout = 0
        self.IFC = 0
        self.inMethod = False
        self.variables = []
        self.eachIFC = {}
        self.starttime = 0
        self.endtime = 0
        #### Ejiogus
        self.maxDepth = 0
        self.currentDepth = 0
        self.twinNumber = 0
        self.monadicity = 0
        self.totalNodes = 0

    def enterVariableDeclarator(self, ctx: JavaParser.VariableDeclaratorContext):
        if self.inMethod == True:
            self.variables.append(ctx.variableDeclaratorId().Identifier())
            self.Fan = self.Fan + 1

    def enterFormalParameter(self, ctx: JavaParser.FormalParameterContext):
        self.variables.append(ctx.variableDeclaratorId().Identifier())
        self.Fan = self.Fan + 1
        self.Fout = self.Fout + 1

    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        self.inMethod = True

    def exitMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        self.inMethod = False
        start_line = ctx.start.line
        stop_line = ctx.stop.line
        # Calculate the number of lines
        lines_in_context = stop_line - start_line + 1
        me_ifc = lines_in_context * math.pow((self.Fan * self.Fout), 2)
        self.IFC = self.IFC + me_ifc
        self.eachIFC[ctx.methodHeader().methodDeclarator().Identifier()] = me_ifc
        self.Fan = 0
        self.Fout = 0
        self.variables = []

        # Enter a parse tree produced by JavaParser#leftHandSide.

    def enterLeftHandSide(self, ctx: JavaParser.LeftHandSideContext):
        if ctx.expressionName().Identifier() not in self.variables:
            self.Fout = self.Fout + 1

    def enterEveryRule(self, ctx):
        self.totalNodes += 1
        self.currentDepth += 1

        # Update max depth if needed
        self.maxDepth = max(self.maxDepth, self.currentDepth)

        # Check if the current node is monadic
        if not ctx.children or len(ctx.children) == 1:
            self.monadicity += 1

        # Calculate twin number for non-root nodes
        if self.currentDepth > 0:
            parent = ctx.parentCtx
            if parent is not None:
                self.twinNumber = max(self.twinNumber, parent.getChildCount())

    def exitEveryRule(self, ctx):
        self.currentDepth -= 1

    def exitCompilationUnit(self, ctx: JavaParser.CompilationUnitContext):
        self.starttime = time.time()

    def exitCompilationUnit(self, ctx: JavaParser.CompilationUnitContext):
        start_line = ctx.start.line
        stop_line = ctx.stop.line
        # Calculate the number of lines
        lines_in_context = stop_line - start_line + 1
        print(
            "---------------------------------------------------------------------\nHenry and Kafura’s Information Software Metrics \n--------------------------------------------------------------------- ")
        # print(self.operators)
        print(f"the number of procedures : {len(self.eachIFC)}")
        print(f"the formula for IFC is : Length * (Fin * Fout)^2")
        print("print the each procedure IFC :")
        for key, value in self.eachIFC.items():
            print(f'{key}: {value}')
        # print(self.operands)
        print(f"the total IFC is : {self.IFC}")
        print(
            "---------------------------------------------------------------------\nEjiogus’s Software Metrics \n--------------------------------------------------------------------- ")
        S = self.maxDepth * self.twinNumber * self.monadicity
        softwareSize = self.totalNodes - 1
        print(f'Structural Complexity (S): {S}')
        print(f'Software Size: {softwareSize}')
        print(f'Height of Deepest Node (H): {self.maxDepth}')
        print(f'Twin Number of the Root (Rt): {self.twinNumber}')
        print(f'Monadicity (M): {self.monadicity}')
        print(f'Total Number of Nodes: {self.totalNodes}')
        print("************** modifiability ****************")
        print("related metrics :")
        print(f'Structural Complexity (S): {S}')
        print(f"IFC : {self.IFC}")
        print(f'Software Size: {softwareSize}')
        print(f'Height of Deepest Node (H): {self.maxDepth}')
        print(f"Lines of code is :{lines_in_context}")
        print("************** usability ****************")
        print(f"IFC : {self.IFC}")
        print(f'Structural Complexity (S): {S}')
        print(f'Software Size: {softwareSize}')
        print(f'Height of Deepest Node (H): {self.maxDepth}')
        print(f'Total Number of Nodes: {self.totalNodes}')
