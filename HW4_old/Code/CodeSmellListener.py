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

    def logGraph(self):
        print("nodes= ",list(self.graph.nodes(data=True)))
        print("edges= ",list(self.graph.edges(data=True)))


    def exitCompilationUnit(self, ctx:JavaParser.CompilationUnitContext):
        # print("final:::::=======================================:::::")
        # self.logGraph()


        cycles = list(nx.simple_cycles(self.graph))
        for cycle in cycles:
            print(cycle)



    def enterNormalClassDeclaration(self, ctx:JavaParser.NormalClassDeclarationContext):
        name = ctx.typeIdentifier().getText()
        self.addnode(name)
        if ctx.classImplements():
            interface_extends = ctx.classImplements().getChild(1)
            extends = [interface_extends.getChild(i).getText() for i in range(0, interface_extends.getChildCount(), 2)]
            self.addnode(extends)
            self.addedge([(extend, name) for extend in extends])
        if ctx.classExtends():
            class_extends = ctx.classExtends().getChild(1).getText()
            self.addnode(class_extends)
            self.addedge([(class_extends, name)])

        if ctx.classBody():
            class_body = ctx.classBody()
            # print("aasdasdasd:  ", class_body.getText())
            for i in range(1, class_body.getChildCount() - 1):
                body = class_body.getChild(i)
                if body.classMemberDeclaration():
                    if body.classMemberDeclaration().fieldDeclaration():
                        if body.classMemberDeclaration().fieldDeclaration().unannType().unannReferenceType():
                            type_var = body.classMemberDeclaration().fieldDeclaration().unannType().getText()
                            self.addnode(type_var)
                            self.addedge([(name, type_var)])


    def enterNormalInterfaceDeclaration(self, ctx:JavaParser.NormalInterfaceDeclarationContext):
        name = ctx.typeIdentifier().getText()
        self.addnode(name)
        if ctx.interfaceExtends():
            interface_extends = ctx.interfaceExtends().getChild(1)
            extends = [interface_extends.getChild(i).getText() for i in range(0,interface_extends.getChildCount(),2)]
            self.addnode(extends)
            self.addedge([(extend,name) for extend in extends])
        # self.logGraph()

