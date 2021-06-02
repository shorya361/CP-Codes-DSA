import sys
def travellingSalesMan(startingPoint, graph):
    def route_cost(source, routes):
        if len(routes)==0:
            return graph[source][startingPoint]
        
        # print('at ', source,' going to visit:', routes)
        cost= sys.maxsize
        for i in routes:
                # print(i,routes,source)
                new_route = routes.copy()
                new_route.remove(i)
                till_here=graph[source][i]
                next_cost=route_cost(i,new_route)
                newCost=till_here + next_cost
                # print('from ',i,' we receive ',newCost)
                cost = min( cost , newCost )
        # print('----------------')
        return cost        

    path_route=[]
    for i in range(len(graph)):
        if i !=startingPoint:
            path_route.append(i)
            
    FinalCost = sys.maxsize
    for i in path_route:
        sample= path_route.copy()
        sample.remove(i)
        # print(i,sample,path_route)
        eachPathCost=route_cost(i,sample)
        # print('from ',startingPoint,'to',i,": ",eachPathCost+ graph[startingPoint][i],sample)
        # print(graph[startingPoint][i]+ eachPathCost)
        # print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
        FinalCost= min(FinalCost,eachPathCost + graph[startingPoint][i] )
    print(FinalCost)
    

graph=[
    [0,10,15,20],
    [5,0,9,10],
    [6,13,0,12],
    [8,8,9,0]
    ]
travellingSalesMan(0,graph)