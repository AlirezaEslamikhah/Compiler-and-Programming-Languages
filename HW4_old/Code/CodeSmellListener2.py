from gen.JavaParser import *
import networkx as nx
import matplotlib.pyplot as plt
class CodeSmellListener(ParseTreeListener):
    def __init__(self):
        self.graph = nx.DiGraph()

    def addnode(self,node):
        if not isinstance(node,list):
            if not node in self.graph:
                self.graph.add_node(node)
        else:
            for single_node in node:
                self.addnode(single_node)
        # print(list(self.graph.nodes(data=True)))
    def addedge(self,edge):
        if isinstance(edge,list):
            self.graph.add_edges_from(edge)
        else:
            self.graph.add_edge(edge)



    def exitCompilationUnit(self, ctx:JavaParser.CompilationUnitContext):
        # print("final:::::=======================================:::::")
        # self.logGraph()


        cycles = list(nx.simple_cycles(self.graph))
        for cycle in cycles:
            print(cycle)



    def enterClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
        name = ctx.identifier().getText()
        self.addnode(name)

        if ctx.classBody():
            class_body = ctx.classBody()
            for i in range(1, class_body.getChildCount() - 1):
                body = class_body.getChild(i)
                if body.memberDeclaration():
                    if body.memberDeclaration().fieldDeclaration():
                        if body.memberDeclaration().fieldDeclaration().typeType().classOrInterfaceType():
                            type_var = body.memberDeclaration().fieldDeclaration().typeType().getText()
                            self.addnode(type_var)
                            self.addedge([(name, type_var)])




