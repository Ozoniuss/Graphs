from Graph import *

def readGrahFromFile(file):
    #reads a graph from a file
    with open(file, 'r') as f:
        lines = f.readlines()
        first_line = lines[0]
        parts = first_line.split()
        graph = Graph(int(parts[0]))
        lines.remove(first_line)
        if len(lines) == 0:
            return graph
        for line in lines:
            parts = line.split()
            origin = int(parts[0])
            target = int(parts[1])
            cost = int(parts[2])

            graph.addEdge(origin, target, cost)

    return graph



def writeGraphToFile(file, graph):
    #writes a graph to a file
    with open(file, 'w') as f:
        first_line = str(graph.getNoOfVertices()) + ' ' + str(graph.getNoOfEdges())
        f.write(first_line+'\n')
        for vertex in graph.getAllVertexes():
            targets = graph.getOutboundNeighbours(vertex)
            for target in targets:
                cost = graph.getEdgeCost(vertex, target)
                f.write(str(vertex) + " " + str(target) + " " + str(cost) + '\n')

def readFromActivitiesAndPrerequisites(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        graph = ActivityGraph(len(lines) + 2)
        non_end_vertices = set()
        for i in range(1,len(lines)+1):
            non_end_vertices.add(i)
        for line in lines:
            parts = line.split()
            vertex = parts[0]
            duration = parts[1]
            graph.setDuration(int(vertex), int(duration))
            for predecessor in parts[2:]:
                graph.addEdge(int(predecessor),int(vertex),0)
                if int(predecessor) in non_end_vertices:
                    non_end_vertices.remove(int(predecessor))
            if len(parts[2:]) == 0: #no predecessor
                graph.addEdge(0,int(vertex),0)
        for final_vertices in non_end_vertices:
            graph.addEdge(final_vertices,len(lines) + 1, 0)
    return graph
