from menu import *
#run_menu()

# g = readFromActivitiesAndPrerequisites("manual execution")
# print(g)
# print(topologicalSortDFS(g))
# planActivities(g)
# for node in g.getAllVertexes():
#     output = g.toStringActivityNode(node)
#     if node == 0 or node == len(g.getAllVertexes())-1:
#         print(output)
#         print()
#         continue
#     if g.getActivityNode(node).earliestStart == g.getActivityNode(node).latestStart:
#         print(colored(output, 'red'))
#         print()
#         continue
#     print(output)
#     print()

# g = readGrahFromFile("file.txt")
# print(vertexCoverApproximation(g))

g = readGrahFromFile("files/VertexCoverEx1")
#g = randomUndirectedGraph(18)
print(g)
t = time.time()
print(vertexCoverApproximation(g))
print("time elapsed: {:.2f}s".format(time.time() - t))
t = time.time()
print(vertexCoverBruteForce(g))
print("time elapsed: {:.2f}s".format(time.time() - t))
t = time.time()
print(vertexCoverBruteForceUsingAproximation(g))
print("time elapsed: {:.2f}s".format(time.time() - t))