from Gen.JavaParserListener import *
from Gen.JavaParser import JavaParser
from networkx import DiGraph
import networkx as nx


class EjioguMetricsListener(JavaParserListener):
    def __init__(self):
        # Initialize an empty directed graph
        self.graph = DiGraph()
        # Keep track of the last node id to create unique ids for graph nodes
        self.last_id = 0
        # Dictionary to map a parser rule context to node id
        self.context_to_node_id = {}

    def get_unique_node_id(self, ctx):
        if ctx not in self.context_to_node_id:
            self.context_to_node_id[ctx] = self.last_id
            self.last_id += 1
        return self.context_to_node_id[ctx]

    def enterEveryRule(self, ctx):
        # Get a unique id for the current context
        current_node_id = self.get_unique_node_id(ctx)

        # If this node has a parent, connect them
        if ctx.parentCtx:
            parent_id = self.get_unique_node_id(ctx.parentCtx)
            self.graph.add_edge(parent_id, current_node_id)

    def calculate_metrics(self):
        # Assumes that the root of the graph is node with id 0
        H = nx.dag_longest_path_length(self.graph)
        # Twin number of the root, assumes root has an id of 0
        Rt = self.graph.out_degree(0)

        # Calculate Monadicity
        leaves = [node for node in self.graph.nodes() if self.graph.out_degree(node) == 0]
        M = len(leaves)

        # Calculate structural complexity
        Sc = H * Rt * M

        # Software size
        S = len(self.graph.nodes) - 1
        print("---------------------------------------------------------------------\nEjiogu’s Software Metrics \n--------------------------------------------------------------------- ")
        print(f"H: the height of the deepest nested node : {H}")
        print(f"Rt: the Twin number of the root: {Rt}")
        print(f"M: the Monadicity {M}")
        print(f"Sc = H × Rt × M")
        print(f"Sc: Structural Complexity: {Sc}")
        print(f"S = total umber of nodes − 1")
        print(f"S: Software Size: {S}")

