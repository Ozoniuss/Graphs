import random
from Color_Console import *
from termcolor import colored
from activityNode import ActivityNode
class Graph:

    def __init__(self, no_of_vertices):
        self._dict_in = {}
        self._dict_out = {}
        self._dict_costs = {}
        self._no_of_vertices = no_of_vertices
        self._no_of_edges = 0
        for i in range (no_of_vertices):
            self._dict_in[i] = []
            self._dict_out[i] = []

    def __str__(self):
        output = ''
        first_line = str(self.getNoOfVertices()) + ' ' + str(self.getNoOfEdges())
        output += first_line + '\n'
        for vertex in self.getAllVertexes():
            targets = self.getOutboundNeighbours(vertex)
            for target in targets:
                cost = self.getEdgeCost(vertex, target)
                output += (str(vertex) + " " + str(target) + " " + str(cost) + '\n')
        return output

    def getNoOfVertices(self):
        #returns the number of vertices
        return self._no_of_vertices

    def getNoOfEdges(self):
        #returns the number of edges, Th(1)
        return self._no_of_edges

    def degIn(self, vertex):
        #returns the inbound degree of a vertex
        if self._dict_out.get(vertex) == None:
            raise Exception('Invalid vertex!')
        return len(self._dict_in[vertex])

    def degOut(self, vertex):
        #returns the outbound degree of a vertex
        if self._dict_out.get(vertex) == None:
            raise Exception('Invalid vertex!')
        return len(self._dict_out[vertex])

    def isEdge(self, vertex1, vertex2):
        #returns if there is an edge between vertex1 and vertex2(not directed), O(nr_of_vertices)
        if self._dict_out.get(vertex1) == None or self._dict_out.get(vertex2) == None:
            raise Exception('Invalid vertexes')
        if self._dict_costs.get((vertex1, vertex2)) == None and self._dict_costs.get((vertex2, vertex1)) == None:
            return False
        return True

    def getInboundNeighbours(self, vertex):   #returns the inbound neighbours of a vertex
        if self._dict_out.get(vertex) == None:
            raise Exception('Invalid vertex!')
        return self._dict_in[vertex]

    def getOutboundNeighbours(self, vertex):   #returns the outbound neighbours of a vertex
        if self._dict_out.get(vertex) == None:
            raise Exception('Invalid vertex!')
        return self._dict_out[vertex]

    def getEdgeCost(self, origin, target):
        #returns the cost of a given edge
        if self._dict_out.get(origin) == None or self._dict_out.get(target) == None:
            raise Exception('Invalid vertexes!')
        if self._dict_costs.get((origin, target)) == None:
            raise Exception('No edge between the vertexes!')
        return self._dict_costs[(origin,target)]

    def setEdgeCost(self, origin, target, cost):
        #sets the cost of a given edge
        if self._dict_out.get(origin) == None or self._dict_out.get(target) == None:
            raise Exception('Invalid vertexes!')
        if self._dict_costs.get((origin, target)) == None:
            raise Exception('No edge between the vertexes!')
        self._dict_costs[(origin,target)] = cost

    def addVertex(self, vertex):
        #adds a vertex to the graph
        if self._dict_out.get(vertex) != None:
            raise Exception('Invalid vertex!')
        self._no_of_vertices += 1
        self._dict_in[vertex] = []
        self._dict_out[vertex] = []

    def removeVertex(self, vertex):
        #removes a vertex from the graph
        if self._dict_out.get(vertex) == None:
            raise Exception('Invalid vertex!')
        self._no_of_vertices -= 1
        # for edge in self.getAllEdges():
        #         if edge[0] == vertex:
        #             self.removeEdge(edge[0], edge[1])
        #         if edge[1] == vertex and edge[1] != edge[0]:
        #             self.removeEdge(edge[0], edge[1])
        edges = []
        if vertex in self._dict_out[vertex]:
            self.removeEdge(vertex, vertex)
        for other_vertex in self._dict_in[vertex]:
            edges.append((other_vertex, vertex))
        for other_vertex in self._dict_out[vertex]:
            edges.append((vertex, other_vertex))
        for edge in edges:
            self.removeEdge(edge[0], edge[1])
        del self._dict_in[vertex]
        del self._dict_out[vertex]

    def getAllVertexes(self):
        #returns all vertexes
        return list(self._dict_out.keys())

    def getAllEdges(self):
        #returns all edges
        return list(self._dict_costs.keys())

    def addEdge(self, origin, target, cost):
        #adds an edge to the graph
        if self._dict_out.get(origin) == None or self._dict_out.get(target) == None:
            raise Exception('Invalid edge!')
        if self._dict_costs.get((origin, target)) != None:
            raise Exception('Existing edge!')
        self._dict_out[origin].append(target)
        self._dict_in[target].append(origin)
        self._dict_costs[(origin,target)] = cost
        self._no_of_edges += 1

    def removeEdge(self, origin, target):
        #removes an edge from the graph
        if self._dict_out.get(origin) == None or self._dict_out.get(target) == None:
            raise Exception('Invalid edge!')
        if self._dict_costs.get((origin, target)) == None:
            raise Exception('Inexisting edge!')
        self._dict_out[origin].remove(target)
        self._dict_in[target].remove(origin)
        del self._dict_costs[(origin,target)]
        self._no_of_edges -= 1


    def getCopyOfGraph(self):
        #returns a copy of the graph
        copy = Graph(self._no_of_vertices)
        copy._no_of_edges = self._no_of_edges
        for vertex in list(self._dict_in.keys()):
            copy._dict_in[vertex] = self.getInboundNeighbours(vertex).copy()
        for vertex in list(self._dict_out.keys()):
            copy._dict_out[vertex] = self.getOutboundNeighbours(vertex).copy()
        copy._dict_costs = self._dict_costs

        return copy

###### inherited activity graph

class ActivityGraph(Graph):
    def __init__(self, no_of_vertices):
        super().__init__(no_of_vertices)
        self.dictActivities = {}
        for i in range(no_of_vertices):
            self.dictActivities[i] = ActivityNode()

    def getActivityNode(self, vertex):
        return self.dictActivities[vertex]

    def printActivityNode(self, vertex):
        node = self.getActivityNode(vertex)
        print(str(node.earliestStart) + " " + str(vertex) + " " + str(node.earliestEnd))
        print(str(node.latestStart) + " " + str(node.duration) + " " + str(node.latestEnd))

    def toStringActivityNode(self, vertex):
        output = ""
        node = self.getActivityNode(vertex)
        output = str(node.earliestStart) + " " + str(vertex) + " " + str(node.earliestEnd)+'\n'+ str(node.latestStart) + " " + str(node.duration) + " " + str(node.latestEnd)
        return output

    def setEarliestStart(self, vertex, time):
        self.dictActivities[vertex].earliestStart = time

    def setEarliestEnd(self, vertex, time):
        self.dictActivities[vertex].earliestEnd = time

    def setDuration(self, vertex, time):
        self.dictActivities[vertex].duration = time

    def setLatestStart(self, vertex, time):
        self.dictActivities[vertex].latestStart = time

    def setLatestEnd(self, vertex, time):
        self.dictActivities[vertex].latestEnd = time
#### external functions ##############


############         file input/output


#g = readFromActivitiesAndPrerequisites("activities")
#print(g)
################## random graph


######################

##3 and 4





#g = readFromActivitiesAndPrerequisites("files/activities")
#act = findActivitiesEarliestTime(0,g,set(),[])
#findActivitiesLatestTime(8,g,set(),[])
#for a in act:
    #g.printActivityNode(a)
    #print()



#g = readGrahFromFile("manual execution")
#g = readFromActivitiesAndPrerequisites("activities")
#print(topologicalSortDFS(g))

#printAllPathsNoDagDFS(0,g,[],[])




















































# class Tree:
#     def __init__(self, Root):
#         self._Children = {}
#         self._Parent = {}
#         self._Root = Root
#         self._Children[Root] = []
#         self._Parent[Root] = None
#
#     def NodeExists(self, Node):
#         return Node in self._Parent
#
#     def GetChildren(self, Node):
#         return self._Children[Node]
#
#     def GetParent(self, Node):
#         return self._Parent[Node]
#
#     def AddChild(self, Parent, Node):
#         self._Parent[Node] = Parent
#         self._Children[Parent].append(Node)
#         self._Children[Node] = []
#
#     def GetRoot(self):
#         return self._Root
#
#
# def GenerateTreeFromGraph(Graph, Root):
#     tree = Tree(Root)
#     queue = [Root]
#     while len(queue) > 0:
#         Node = queue.pop(0)
#         for Vertex in Graph.parseNout(Node):
#             if (tree.NodeExists(Vertex) == False):
#                 tree.AddChild(Node, Vertex)
#             queue.append(Vertex)
#     return tree
#
# def DisplayTree(tree, root = None, depth = 0):
#     if (root == None):
#         root = tree.GetRoot()
#     output = ""
#     for i in range(depth):
#         output += "  "
#     print(output, root)
#     children = tree.GetChildren(root)
#     for child in children:
#         DisplayTree(tree, child, depth + 1)
#
# def GetPath(tree, source, end):
#     path = []
#     path.append(end)
#     parent = Tree.GetParent(end)
#     while parent != source and parent != None:
#         path.append(parent)
#         parent = tree.GetParent(parent)
#     if (parent != source):
#         print("No path")
#     else:
#         path.append(parent)
#         path.reverse()
#         print(path)

