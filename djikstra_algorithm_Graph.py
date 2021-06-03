import sys 
def dijkstra(graph,source):
    visited=[False] * len(graph)
    distance= [sys.maxsize] * len(graph)
    distance[source] = 0
    
    def find_Next_Node():
        nextNode=None
        minim=sys.maxsize
        for i in range(len(distance)):
            if distance[i] < minim and visited[i]== False:
                minim= distance[i]
                nextNode = i
        return nextNode
    for i in range(len(graph)):
        nextNode= find_Next_Node()
        visited[nextNode]=True 
        for j in range(len(graph)):
            if graph[nextNode][j]!=0 and visited[j] == False and distance[j] > distance[nextNode] + graph[nextNode][j]:
                distance[j] =  distance[nextNode] + graph[nextNode][j]
    print(distance)
            



graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

dijkstra(graph,0)