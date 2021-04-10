from Graph import *
from PriorityQueue import PriorityQueue
###### random graphs ###################
def randomGraph(numberOfVertices):
    #generates a random graph with given number of vertices
    random_graph = Graph(numberOfVertices)
    for vertex in random_graph.getAllVertexes():
        random_no_of_outbound_neighbours = random.randint(0,numberOfVertices)
        random_outbound_neighbours = random.sample(random_graph.getAllVertexes(),random_no_of_outbound_neighbours)
        if random_no_of_outbound_neighbours != 0:
            random_outbound_neighbours.sort()
        for target in random_outbound_neighbours:
            random_cost = random.randint(0,1000)
            random_graph.addEdge(vertex, target, random_cost)
            #random_graph.setEdgeCost(vertex, target, random_cost)
    return random_graph

def randomUndirectedGraph(numberOfVertices):
    random_graph = Graph(numberOfVertices)
    possible_edges = []
    for i in range(numberOfVertices - 1):
        for j in range(i+1, numberOfVertices):
            possible_edges.append((i,j))
    l = len(possible_edges)
    no_edges = random.randint(1,l)
    sample = random.sample(possible_edges, no_edges)
    for edge in sample:
        random_graph.addEdge(edge[0], edge[1],0)
        random_graph.addEdge(edge[1],edge[0],0)
    return random_graph


def randomGraph2(number_of_vertices, number_of_edges):
    #generates a random graph with given number of vertexes and edges
    if number_of_edges > number_of_vertices * number_of_vertices:
        raise Exception('Too many edges!')
    random_graph = Graph(number_of_vertices)
    edge_list = []
    for i in range(number_of_vertices):
        for j in range(number_of_vertices):
            edge_list.append((i,j))
    graph_edges = random.sample(edge_list, number_of_edges)
    for edge in graph_edges:
        random_graph.addEdge(edge[0], edge[1], random.randint(1, 1000))
    return random_graph


def accessibleFromVertex(graph, vertex):
    #returns the set of vertices of the graph that are accessible from the given vertex
    accessible = set()
    accessible.add(vertex)
    l = [vertex]
    while len(l) > 0:
        x = l[0]
        l = l[1:]
        for y in graph.getOutboundNeighbours(x):
            if y not in accessible:
                accessible.add(y)
                l.append(y)
    return accessible

def lowestLenghtPathBetweenVerticesBacwardsBFS(graph, source, target):
    path = []
    marks = {} # dictionary to mark visited vertexes
    for vertex in graph.getAllVertexes():
        marks[vertex] = -1 #unvisited, visited - any positive number
    marks[target] = 0 #mark as visited
    found = 0
    queue = [target]
    while found == 0 and len(queue) != 0:
        x = queue[0]
        queue = queue[1:]
        for y in graph.getInboundNeighbours(x):
            if marks[y] == -1:
                queue.append(y)
                marks[y] = x #mark it with its source vertex so that we can print it
            if y == source:
                found = 1
                break
    if found == 0:
        return None
    path.append(source)
    path_point = source
    while(path_point != target):
        path.append(marks[path_point])
        path_point = marks[path_point]
    return path


def dijkstraAlgorithm(graph, source, target): #finds the minimum cost path betwenn 2 vertices using a forward dijkstra algorithm approach
    fathers = {source:source}
    distances = {source:0}  #dict to store distances
    p_queue = PriorityQueue()
    for vertex in graph.getOutboundNeighbours(source):
        priority = graph.getEdgeCost(source, vertex)
        p_queue.add(vertex, priority)
        fathers[vertex] = source

    while(p_queue.isEmpty() == False):
        current_vertex, distance_to_current = p_queue.pop()
        distances[current_vertex] = distance_to_current
        if current_vertex == target:
            break
        for next_vertex in graph.getOutboundNeighbours(current_vertex):
            if next_vertex not in distances:
                if p_queue.contains(next_vertex) == False:
                    priority = distance_to_current + graph.getEdgeCost(current_vertex, next_vertex) ##add the new accesible vertex to the queue
                    p_queue.add(next_vertex, priority)
                    fathers[next_vertex] = current_vertex
                else:
                    if p_queue.getObjPriority(next_vertex) > distance_to_current + graph.getEdgeCost(current_vertex, next_vertex): ##perform relaxation
                        priority = distance_to_current + graph.getEdgeCost(current_vertex, next_vertex)
                        p_queue.add(next_vertex, priority)
                        fathers[next_vertex] = current_vertex
    if target not in distances:
        return None, None
    path = []
    current = target
    while(current != source):
        path.append(current)
        current = fathers[current]
    path.append(source)
    path.reverse()
    return distances, path

###topsort
def topologicalSortDFS(graph):   #performs topological sort using tanjan algorithm
    visitedSet = set()
    stack = []
    for vertex in graph.getAllVertexes():
        if vertex in visitedSet:
            continue
        valid = topSortmarkingDFS(vertex, visitedSet, stack, graph)
        if valid == False:
            return "Graph is not DAG!"
    stack.reverse()
    return stack

def topSortmarkingDFS(vertex, visitedSet, stack, graph):
    visitedSet.add(vertex)
    for child in graph.getOutboundNeighbours(vertex):
        if child in stack:
            continue
        if child in visitedSet:
            continue
        topSortmarkingDFS(child, visitedSet, stack, graph)
    for v in graph.getInboundNeighbours(vertex):
        if v in stack:
            return False
    stack.append(vertex)
#####topsort

##activities
# def findActivitiesEarliestTime(currentNode, graph, list_of_activities, stackFrame):
#     list_of_activities.add(currentNode)
#     stackFrame.append(currentNode)
#     for nextNode in graph.getOutboundNeighbours(currentNode):
#         previousActivityNode = graph.getActivityNode(currentNode)
#         activityNode = graph.getActivityNode(nextNode)
#         if activityNode.earliestStart <= previousActivityNode.earliestEnd:
#             graph.setEarliestStart(nextNode, previousActivityNode.earliestEnd)
#             graph.setEarliestEnd(nextNode, previousActivityNode.earliestEnd + activityNode.duration)
#         if len(graph.getOutboundNeighbours(nextNode)) == 0:
#             list_of_activities.add(nextNode)
#             stackFrame.append(nextNode)
#             #print(stackFrame)
#             stackFrame.pop(-1)
#         else:
#             findActivitiesEarliestTime(nextNode, graph, list_of_activities, stackFrame)
#             stackFrame.pop(-1)
#     return list_of_activities
#
# def findActivitiesLatestTime(currentNode, graph, list_of_activities, stackFrame):
#     list_of_activities.add(currentNode)
#     stackFrame.append(currentNode)
#     for nextNode in graph.getInboundNeighbours(currentNode):
#         previousActivityNode = graph.getActivityNode(currentNode)
#         activityNode = graph.getActivityNode(nextNode)
#         if activityNode.latestEnd >= previousActivityNode.latestStart or activityNode.latestEnd == 0:
#             graph.setLatestEnd(nextNode, previousActivityNode.latestStart)
#             graph.setLatestStart(nextNode, previousActivityNode.latestStart - activityNode.duration)
#         if len(graph.getInboundNeighbours(nextNode)) == 0:
#             list_of_activities.add(nextNode)
#             stackFrame.append(nextNode)
#             #print(stackFrame)
#             stackFrame.pop(-1)
#         else:
#             findActivitiesLatestTime(nextNode, graph, list_of_activities, stackFrame)
#             stackFrame.pop(-1)
#     return list_of_activities

# def planActivities(graph):
#     list_of_activities = set()
#     stackframe = []
#     current_node = 0
#     findActivitiesEarliestTime(current_node, graph, list_of_activities, stackframe)
#     list_of_activities.clear()
#     stackframe.clear()
#
#     current_node = len(graph.getAllVertexes())-1
#     graph.setLatestStart(current_node, graph.getActivityNode(current_node).earliestStart)
#     graph.setLatestEnd(current_node, graph.getActivityNode(current_node).earliestStart)
#     findActivitiesLatestTime(current_node, graph, list_of_activities, stackframe)
# ##activities

def findActivitiesEarliestTime(graph, sorted_nodes):
    #sorted_nodes = topologicalSortDFS(graph) #begins from 0, ends with last
    for node in sorted_nodes:
        actNode = graph.getActivityNode(node)
        for predecessor in graph.getInboundNeighbours(node):
            predNode = graph.getActivityNode(predecessor)
            if actNode.earliestStart <= predNode.earliestEnd:
                graph.setEarliestStart(node, predNode.earliestEnd)
                graph.setEarliestEnd(node, predNode.earliestEnd + actNode.duration)

def findActivitiesLatestTime(graph, sorted_nodes):
    #sorted_nodes = topologicalSortDFS(graph) #begins from 0, ends with last
    #sorted_nodes.reverse()
    for node in sorted_nodes:
        actNode = graph.getActivityNode(node)
        for successor in graph.getOutboundNeighbours(node):
            predNode = graph.getActivityNode(successor)
            if actNode.latestEnd >= predNode.latestStart or actNode.latestEnd == 0:
                graph.setLatestEnd(node, predNode.latestStart)
                graph.setLatestStart(node, predNode.latestStart - actNode.duration)

def planActivities(graph):
    sorted_nodes = topologicalSortDFS(graph)
    findActivitiesEarliestTime(graph, sorted_nodes)
    sorted_nodes.reverse()
    graph.setLatestStart(len(sorted_nodes) - 1, graph.getActivityNode(len(sorted_nodes) - 1).earliestStart)
    graph.setLatestEnd(len(sorted_nodes) - 1, graph.getActivityNode(len(sorted_nodes) - 1).earliestStart)
    findActivitiesLatestTime(graph, sorted_nodes)

def printAllPathsNoDagDFS(currentNode, graph, visited_nodes,stackFrame):
    #prints all paths of a DAG using a dfs approach
    visited_nodes.append(currentNode)
    stackFrame.append(currentNode)
    for nextNode in graph.getOutboundNeighbours(currentNode):
        #if nextNode in visited_nodes:
            #continue
        if len(graph.getOutboundNeighbours(nextNode)) == 0:
            stackFrame.append(nextNode)
            #print(stackFrame)
            stackFrame.pop(-1)
        else:
            printAllPathsNoDagDFS(nextNode, graph,visited_nodes,stackFrame)
            stackFrame.pop(-1)


def vertexCoverApproximation(graph):
    cover = set()
    neighboursCopy = dict()
    edgesCopy = dict()
    for vertex in graph.getAllVertexes():
        neighboursCopy[vertex] = []
        for neighbour in graph.getOutboundNeighbours(vertex):
            neighboursCopy[vertex].append(neighbour)    #make a copy of the neighbours, both inbound and outbound since they are the same
    edges = graph.getAllEdges().copy()
    for i in range (len(edges)-1,-1,-1):
        edgesCopy[edges[i]] = 1    #hash to store the edges for great efficiency
    while(len(edgesCopy) > 0):
        edge = edgesCopy.popitem()  #remove the last edge added to the hash
        vertex1 = edge[0][0]
        vertex2 = edge[0][1]
        edgesCopy.pop((vertex2,vertex1))
        cover.add(vertex1)
        cover.add(vertex2)
        for neighbour in neighboursCopy[vertex1]:
            if (edgesCopy.get((vertex1,neighbour))!=None): #existing edge between vertex and neighbour
                edgesCopy.pop((vertex1,neighbour))
                edgesCopy.pop((neighbour,vertex1))
        for neighbour in neighboursCopy[vertex2]:
            if (edgesCopy.get((vertex2,neighbour))!=None): #existing edge between vertex and neighbour
                edgesCopy.pop((vertex2,neighbour))
                edgesCopy.pop((neighbour,vertex2))
        del neighboursCopy[vertex1]
        del neighboursCopy[vertex2]
    return cover

def vertexCoverBruteForce(graph):
    allSubsets = generate_subsets(graph.getNoOfVertices())

    neighboursCopy = dict()
    edgesCopy = dict()
    for vertex in graph.getAllVertexes():
        neighboursCopy[vertex] = []
        for neighbour in graph.getOutboundNeighbours(vertex):
            neighboursCopy[vertex].append(neighbour)    #make a copy of the neighbours, both inbound and outbound since they are the same
    edges = graph.getAllEdges().copy()
    for i in range (len(edges)-1,-1,-1):
        edgesCopy[edges[i]] = 1    #hash to store the edges for great efficiency

    for cover in allSubsets:
        coveredEdges = set()
        for vertex in cover:
            for neighbour in neighboursCopy[vertex]:
                coveredEdges.add((vertex,neighbour))
                coveredEdges.add((neighbour,vertex))
        if len(coveredEdges) == graph.getNoOfEdges():
            return cover

def vertexCoverBruteForceUsingAproximation(graph):
    allSubsets = generate_subsets(graph.getNoOfVertices())

    neighboursCopy = dict()
    edgesCopy = dict()
    for vertex in graph.getAllVertexes():
        neighboursCopy[vertex] = []
        for neighbour in graph.getOutboundNeighbours(vertex):
            neighboursCopy[vertex].append(neighbour)    #make a copy of the neighbours, both inbound and outbound since they are the same
    edges = graph.getAllEdges().copy()
    for i in range (len(edges)-1,-1,-1):
        edgesCopy[edges[i]] = 1    #hash to store the edges for great efficiency

    approximation = len(vertexCoverApproximation(graph))

    for cover in allSubsets:
        if (len(cover) >= approximation//2):
            coveredEdges = set()
            for vertex in cover:
                for neighbour in neighboursCopy[vertex]:
                    coveredEdges.add((vertex,neighbour))
                    coveredEdges.add((neighbour,vertex))
            if len(coveredEdges) == graph.getNoOfEdges():
                return cover

##auxiliary
def generate_subsets(n):
    rez = []
    q = []
    for i in range(n):
        rez.append([i])
        q.append([i])
    for i in range (n):
        temp = []
        while (len(q) != 0):
            el = q.pop(0)
            for i in range(el[-1] + 1, n):
                copy = el.copy()
                copy.append(i)
                temp.append(copy)
                rez.append(copy)
        q = temp
    return rez

def generate_optimal_subsets(n,k): #all subsets of size k+1
    rez = []
    q = []
    for i in range(n):
        rez.append([i])
        q.append([i])
    for i in range(k):
        temp = []
        while (len(q) != 0):
            el = q.pop(0)
            for i in range(el[-1] + 1, n):
                copy = el.copy()
                copy.append(i)
                temp.append(copy)
        q = temp
    return q

