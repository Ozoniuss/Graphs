from Graph import Graph, readGrahFromFile, writeGraphToFile, randomGraph, randomGraph2, accessibleFromVertex, lowestLenghtPathBetweenVerticesBacwardsBFS, dijkstraAlgorithm
import re

class Ui:
    def __init__(self):
        self.__graph = Graph(0)
        self.__options = {'algorithm backwards bfs <x, y>':self.__ui_backwards_bfs,
                          'random graph <x>':self.__ui_random_graph,
                          'random graph <v, e>':self.__ui_random_graph_with_edges,
                          }

    def run(self):
        self.print_menu()
        option = input("command: ")

    def __ui_backwards_bfs(self, source, target):
        pass

    def __ui_dijkstra_shortest_path(self, source, target):
        pass

    def __ui_random_graph(self, nr_of_vertices):
        pass

    def __ui_random_graph_with_edges(self):
        pass
    def __ui_read_from_file(self, filepath):
        pass
    def __ui_write_to_file(self, filepath):
        pass
    def __ui_add_edge(self, source, target):
        pass
    def __ui_add_vertex(self, vertex):
        pass
    def __ui_is_edge(self, source, target):
        pass
    @staticmethod
    def print_menu():
        print("Use one of the commands listed below:")
        print("\n===================== algorithms =====================\n")
        print("algorithm backwards bfs <x, y> ---------- returns the shortest bath between 2 given vertices using a backwards bfs algorithm")
        print("algorithm dijkstra <x, y> --------------- returns the minimum cost path between 2 given vertices using a dijkstra algorithm ")
        print("\n======================= files =======================\n")
        print("read from file <filename> -------- reads a graph from a given file")
        print("write to file <filename> --------- writes a graph to a given file")
        print("\n======================= debug =======================\n")
        print("p.Print the graph.(debug)")
        print("\n================ stored graph options ================\n")
        print("add <source, target> ------------- adds an edge to the stored graph")
        print("add <vertex> --------------------- adds a vertex to the graph")
        print("is edge <source, target> --------- returns true if given edge is part of the stored graph, false otherwise")
        print("remove <source, target> ---------- removes an edge from the stored graph")
        print("remove <vertex> ------------------ removes a vertex from the graph")
        print("set cost <source, target> -------- sets the cost of a given edge")
        print("show cost <source, target> ------- prints the cost of a given edge")
        print("show edges ----------------------- prints all edges")
        print("show inbound degree <x> ---------- prints the inbound degree of vertex x")
        print("show inbound neighbours ---------- prints the inbound neighbours of a vertex")
        print("show number of edges ------------- prints the number of edges")
        print("show number of vertices ---------- prints the number of vertices of the stored graph")
        print("show outbound degree <x> --------- prints the outbound degree ov vertex x")
        print("show outbound neighbours --------- prints the outbound neighbours of a vertex")
        print("show vertices -------------------- prints vertices of the stored graph")
        print("\n==================== random graph ====================\n")
        print("random graph <v, e> -------------- creates a random graph with given number of vertices and edges")
        print("random graph <x> ----------------- creates random graph with x vertices")

    @staticmethod
    def processCommand(command):
        pass


u = Ui()
