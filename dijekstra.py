import sys 
class graph ():
 def __init__(self, vertices):
  self.v= vertices 
  self.graph=[[0 for column in range(vertices)] for row in range (vertices)]
 
 def printf(sefl, destance):
  print("vertix \t distance")
  for node in range (self.v):
   print(node, "\t ", distance[node])

 def min_distance(self, distance, pathset):
  min = sys.maxsize
  for i in range(self.v):
   if distance[i]< min and pathset[i]==False:
    min = distance[i]
    min_index = i 
 return min_index


 def dijkstra(self, source):
  distance = [sys.maxsize]*self.v
  distance[source]=0
  pathset=[False]*self.v
  for dist in range (self.v):
   x= self.min_distance(distance, pathset) 
   pathset [x]= True
  for y in range (self.v):
   if self.graph[x][y]>0 and pathset [y]== False and distance[y]>distance[x]+self.graph[x][y]:
    distance[y]= distance[x]+self.graph[x][y]

