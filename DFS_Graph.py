#Depth First Search for a Graph using recursive method

def DFS(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            DFS(visited, graph, neighbour)




graph = { "A" : ["B","C","D"], "B": ["E"], "C": ["D","E"], "D": [],'E':[]}
visited = set()
print("Following is Depth First Traversal (starting from vertex A)")
(DFS(visited, graph, "A"))