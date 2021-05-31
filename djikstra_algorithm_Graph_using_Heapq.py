import heapq
import sys

# def calculate_distances(graph, starting_vertex):
#     distances = {vertex: sys.maxsize  for vertex in graph}
#     distances[starting_vertex] = 0
#     for i in distances:
#         print(i,'\t',distances[i])
#     pq = [(0, starting_vertex)]

#     while len(pq) > 0:
#         current_distance, current_vertex = heapq.heappop(pq)

#         # Nodes can get added to the priority queue multiple times. We only
#         # process a vertex the first time we remove it from the priority queue.
#         if current_distance > distances[current_vertex]:
#             continue

#         for neighbor, weight in graph[current_vertex].items():
#             distance = current_distance + weight

#             # Only consider this new path if it's better than any path we've
#             # already found.
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(pq, (distance, neighbor))

#     return distances


# example_graph = {
#     'U': {'V': 2, 'W': 5, 'X': 1},
#     'V': {'U': 2, 'X': 2, 'W': 3},
#     'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
#     'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
#     'Y': {'X': 1, 'W': 1, 'Z': 1},
#     'Z': {'W': 5, 'Y': 1},
# }
# print(calculate_distances(example_graph, 'X'))
# # => {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}




def dijkstra(graph,starting_vertex):
    distance=[sys.maxsize for i in range(len(graph))]
    distance[starting_vertex]=0
    pq=[(0,starting_vertex)]
    heapq.heapify(pq)
    while(len(pq)!=0):
        dist,vertex=heapq.heappop(pq)
        # print( dist,vertex)
        # print(pq)
        for i in range(len(graph)):
            if graph[vertex][i] >0 :
                # print()
                new_distance= graph[vertex][i] + dist
                if  new_distance < distance[i]:
                    heapq.heappush(pq,(new_distance,i))
                    distance[i]=new_distance
        # print(distance)
        # print('new heap:',pq)
    print(distance)
my_graph= [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		[4, 0, 8, 0, 0, 0, 0, 11, 0],
		[0, 8, 0, 7, 0, 4, 0, 0, 2],
		[0, 0, 7, 0, 9, 14, 0, 0, 0],
		[0, 0, 0, 9, 0, 10, 0, 0, 0],
		[0, 0, 4, 14, 10, 0, 2, 0, 0],
		[0, 0, 0, 0, 0, 2, 0, 1, 6],
		[8, 11, 0, 0, 0, 0, 1, 0, 7],
		[0, 0, 2, 0, 0, 0, 6, 7, 0]
		]
dijkstra(my_graph,0)
# 0        11
# 1        12
# 2        4
# 3        11
# 4        10
# 5        0
# 6        2
# 7        3
# 8        6