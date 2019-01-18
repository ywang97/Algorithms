def build_time(source_files, transformations, target_file):
    """
    Return milliseconds needed to build the target file, assuming 
    files not dependent on each other can be processed simultaneously.
    Input:      source | list of source file names
            transforms | list of transformations of form
                       | ([input_files], output_file, transform_time)
                target | name of target file to build
    """
    graph=dict()
    for (inp,out,m) in transformations:
        for v in inp:
            if v not in graph:
                graph[v]=dict()
            if out not in graph:
                graph[out]={v:-m}
            else:
                graph[out][v]=-m
    def topological_sort(Adj):
        parent = dict() # DFS tree
        order = []
        def visit(u):
            for v in Adj[u]:
                if v not in parent:
                    parent[v] = u
                    visit(v)
            order.append(u)
        for v in Adj: # try all sources
            if v not in parent:
                parent[v] = v
                visit(v)
        order.reverse()
        return order
    def dag_sssp(Adj, s):
        parent = dict() # shortest-path tree
        parent[s] = s # s is root
        d = dict()
        for v in Adj:
            d[v]=float('inf') # d[v] = δ(s,v)
        d[s] = 0 # δ(s,s) = 0
        def relax(u, v):
            if d[v] > d[u] + Adj[u][v]:
                d[v] = d[u] + Adj[u][v]
                parent[v] = u
        for u in topological_sort(Adj):
            
            for v in Adj[u]:
                relax(u,v)
        return d
    times=dag_sssp(graph,target_file)
    min_sofar=0
    for v in source_files:
        if times[v]<min_sofar:
            min_sofar=times[v]
    return -min_sofar
