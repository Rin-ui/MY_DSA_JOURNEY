# initialise all distance at distance infinity except source

# relax all e edges v-1 times:
#  if dist[u] + cost[uv] < d[v]
# then d[v] = cost[u] + cost[uv]
# else skip
# relax once more : if we find a new shortest path for any node then we have -ve edge cycle
# else we don't have

