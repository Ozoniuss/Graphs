from fileInputOutput import *
from algorithms import *
import networkx as nx
import matplotlib.pyplot as plt
import time

def print_menu():
    print("Choose one of the operations below:")
    print("1.Create a random graph.")
    print("2.Read a graph from a file.")
    print("3.Write the graph to the file.")
    print("4.Print the number of vertices,")
    print("5.Print the number of edges.")
    print("6.Print the inbound degree of a vertex.")
    print("7.Print the outbound degree of a vertex.")
    print("8.Print the inbound neighbours of a vertex.")
    print("9.Print the outbound neighbours of a vertex.")
    print("10.Print the cost of an edge.")
    print("11.Set the cost of an edge.")
    print("12.Add a vertex to the graph.")
    print("13.Remove a vertex from the graph.")
    print("14.Print the list of vertexes.")
    print("15.Add an edge to the graph.")
    print("16.Remove an edge from the graph.")
    print("17.Is edge?")
    print("18.Print all edges.")
    print("19.Random Graph with given number of vertices and edges.")
    print("20.Shortest path between 2 vertices.")
    print("21.Dijkstra Algorithm for shortest path in a weighted graph between 2 vertices.")
    print("22.Topological sort / verify if graph is DAG")
    print("p.Print the graph.(debug)")


def run_menu():
    print_menu()
    store_graph = randomGraph(5)

    option = None
    while(True):
        option = input('Choose your option:')
        if option == "exit":
            return
        if option == "1":
            nr_of_vertices = input("Number of vertices:")
            t = time.time()
            store_graph = randomGraph(int(nr_of_vertices))
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "2":
            file = input('file name:')
            t = time.time()
            store_graph = readGrahFromFile(file)
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "3":
            file = input('file name:')
            t = time.time()
            writeGraphToFile(file, store_graph)
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "4":
            t = time.time()
            print(store_graph.getNoOfVertices())
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "5":
            t = time.time()
            print(store_graph.getNoOfEdges())
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "6":
            vertex = input('vertex:')
            t = time.time()
            try:
                print(store_graph.degIn(int(vertex)))
            except Exception as e:
                print(e)
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "7":
            vertex = input('vertex:')
            t = time.time()
            try:
                print(store_graph.degOut(int(vertex)))
            except Exception as e:
                print(e)
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "8":
            vertex = input('vertex:')
            t = time.time()
            try:
                print(store_graph.getInboundNeighbours(int(vertex)))
            except Exception as e:
                print(e)
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "9":
            vertex = input('vertex:')
            t = time.time()
            try:
                print(store_graph.getOutboundNeighbours(int(vertex)))
            except Exception as e:
                print(e)
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "10":
            origin = input('origin:')
            target = input('target:')
            t = time.time()
            try:
                print(store_graph.getEdgeCost(int(origin), int(target)))
            except Exception as e:
                print(e)
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "11":
            origin = input('origin:')
            target = input('target:')
            cost = input('cost:')
            t = time.time()
            try:
                store_graph.setEdgeCost(int(origin), int(target), int(cost))
                print('Cost set!')
            except Exception as e:
                print(e)
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "12":
            vertex = input('vertex:')
            t = time.time()
            try:
                store_graph.addVertex(int(vertex))
                print('Vertex added!')
            except Exception as e:
                print(e)
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "13":
            vertex = input('vertex:')
            t = time.time()
            try:
                store_graph.removeVertex(int(vertex))
                print('Vertex removed!')
            except Exception as e:
                print(e)
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "14":
            t = time.time()
            print(store_graph.getAllVertexes())
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "15":
            origin = input('origin:')
            target = input('target:')
            cost = input('cost:')
            t = time.time()
            try:
                store_graph.addEdge(int(origin), int(target), int(cost))
                print('Edge added!')
            except Exception as e:
                print(e)
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "16":
            origin = input('origin:')
            target = input('target:')
            t = time.time()
            try:
                store_graph.removeEdge(int(origin), int(target))
                print('Edge removed!')
            except Exception as e:
                print(e)
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "17":
            vertex1 = input("vertex:")
            vertex2 = input("vertex:")
            t = time.time()
            try:
                print(store_graph.isEdge(int(vertex1), int(vertex2)))
            except Exception as e:
                print(e)
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "18":
            t = time.time()
            print(store_graph.getAllEdges())
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "19":
            vertices = input("Nr of vertices:")
            edges = input("Nr of edges:")
            t = time.time()
            try:
                store_graph = randomGraph2(int(vertices), int(edges))
            except Exception as e:
                print(e)
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == '20':
            source = input("vertex:")
            target = input("vertex:")
            t = time.time()
            path = lowestLenghtPathBetweenVerticesBacwardsBFS(store_graph, int(source), int(target))
            res = ''
            if path == None:
                print('No path')
                print("time elapsed: {:.2f}s".format(time.time() - t))
            else:
                for node in path:
                    res = res + str(node) + ','
                res = res + ' lenght:' + str(len(path) - 1)
                print(res)
                print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == '21':
            source = input("vertex:")
            target = input("vertex:")
            if source.isdigit() == False or target.isdigit() == False:
                print("Invalid vertices!")
            elif int(source) not in store_graph.getAllVertexes() or int(target) not in store_graph.getAllVertexes()\
                    or (int(source) == int(target)):
                print("Invalid vertices!")
            else:
                t = time.time()
                d, path = dijkstraAlgorithm(store_graph, int(source), int(target))
                if (d == None and path == None):
                    print('No path exist between the 2 vertices.')
                    print("time elapsed: {:.2f}s".format(time.time() - t))
                else:
                    print(d[int(target)])
                    print(path)
                    print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == '22':
            t = time.time()
            print(topologicalSortDFS(store_graph))
            print("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "p":
            t = time.time()
            output = ''
            first_line = str(store_graph.getNoOfVertices()) + ' ' + str(store_graph.getNoOfEdges())
            output += first_line + '\n'
            for vertex in store_graph.getAllVertexes():
                targets = store_graph.getOutboundNeighbours(vertex)
                for target in targets:
                    cost = store_graph.getEdgeCost(vertex, target)
                    output += (str(vertex) + " " + str(target) + " " + str(cost) + '\n')
            print(output)
            print ("time elapsed: {:.2f}s".format(time.time() - t))
        if option == "plot":
            g = nx.DiGraph()
            for vertex in store_graph.getAllVertexes():
                g.add_node(vertex)
            for vertex in store_graph.getAllVertexes():
                targets = store_graph.getOutboundNeighbours(vertex)
                for target in targets:
                    g.add_edge(vertex, target, weight = store_graph.getEdgeCost(vertex,target))
            pos = nx.circular_layout(g)
            weights = nx.get_edge_attributes(g, "weight")
            nx.draw_networkx(g, pos, with_labels= True, node_size = 100)
            nx.draw_networkx_edge_labels(g, pos, edge_labels=weights, directed = True)
            plt.show()

        if option == "a":
            vertex = input()
            t = time.time()
            print(accessibleFromVertex(store_graph, int(vertex)))
            print("time elapsed: {:.2f}s".format(time.time() - t))


        if option == "s":
            print_menu()

