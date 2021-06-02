#To find minimum cost in spanning tree in a weight graph
#spanning tree: number of vertices : v then edges: v-1
# uses greedy approach
import sys
def prims(source):
    def findMinimumVertex():
        minimum=sys.maxsize
        result=None
        for i in range(len(distance)):
            if distance[i]< minimum and maxSet[i]==False:
                minimum=distance[i]
                result=i
        # print(distance)
        # print()
        print(result,distance,parent,maxSet)
        return result

    distance=[sys.maxsize for i in range(len(graph))]
    distance[source]=0
    maxSet=[False for i in range(len(distance))]
    parent=[-1 for i in range(len(distance))]
    
    for i in range(len(graph)-1):
        next_source= findMinimumVertex() 

        maxSet[next_source]=True
        for j in range(len(graph)):
            if graph[next_source][j]!=0 and maxSet[j]!=True and graph[next_source][j]< distance[j]:
                distance[j]=graph[next_source][j]
                parent[j]=next_source

   
    for i in range(1,len(graph)):
        print(parent[i],' -> ',i,'::>',distance[i])

graph=[
    [0,4,6,0,0,0],
    [4,0,6,3,4,0],
    [6,6,0,1,0,0],
    [0,3,1,0,2,3],
    [0,4,0,2,0,7],
    [0,0,0,3,7,0]
    ]
   
prims(0)