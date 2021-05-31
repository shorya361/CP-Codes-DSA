def krushkal(graph):
    my_sorted_graph=[]
    for i in range(len(graph)):
        for j in range(i,len(graph)):
            if graph[i][j]!=0:
                my_sorted_graph.append((graph[i][j],[i,j]))
    my_sorted_graph.sort()
    myMaxSet=[False for i in range(len(graph))]
    parent=[-1 for i in range(len(graph))]
    for i in my_sorted_graph:
        source=i[1][0]
        destination=i[1][1]
        if not myMaxSet[source]==myMaxSet[destination]==True :
            parent[destination]=source
            myMaxSet[source]=True
            myMaxSet[destination]=True
            print(source,'---',destination,'::',graph[source][destination])

graph=[
    [0,4,6,0,0,0],
    [4,0,6,3,4,0],
    [6,6,0,1,0,0],
    [0,3,1,0,2,3],
    [0,4,0,2,0,7],
    [0,0,0,3,7,0]
    ]
krushkal(graph)