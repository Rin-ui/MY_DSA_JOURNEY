def build_adj_matrix(arr):
    n = len(arr)
    max_node = max(max(u,v) for u,v in arr)+1
    M = [[0]*max_node for _ in range(max_node)]
    for u,v in arr:
        # for directed graph
        M[u][v]=1
    print('adjucency matrix')
    for row in M:
        print(M)

