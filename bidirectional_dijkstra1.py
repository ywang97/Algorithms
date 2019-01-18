def bidirectional_dijkstra(Adj, w, s, t):
    """
    Return a list of vertices forming a shortest path from s to t 
    Vertices are all integers in range(len(Adj))
    Input:  Adj: undirected graph, Adj[v] is list of vertices adjacent to v
              w: weight dictionary, w[(u,v)] is integer weight of edge (u,v)
              s: source vertex
              t: target vertex
    """
    if s==t:
        return [s]
    
    def dij(A, w, s, t):
        d1=[float('inf') for _ in A]
        d2=[float('inf') for _ in A]
        parent1 = [None for _ in A]
        parent2 = [None for _ in A]
        d1[s], parent1[s]=0, s
        d2[t], parent2[t]=0, t
        Q1=PriorityQueue()
        Q2=PriorityQueue()
        total=(s, d1[s]+d2[s])
        for v in range(len(A)):
            Q1.insert(v, d1[v])
            Q2.insert(v, d2[v])
        for _ in range(len(A)):
            u1=Q1.extract_min()
            u2=Q2.extract_min()
            if d1[u1]>total[1]/2 or d2[u2]>total[1]/2:
                break
            if d1[u1]>d2[u2]:
                u=u2
                d=d2
                queue=Q2
                parent=parent2
            else:
                u=u1
                d=d1
                queue=Q1
                parent=parent1
            for v in A[u]:
                relax(A, w, d, parent, u, v)
                queue.decrease_key(v, d[v])
                if d1[v]+d2[v]<total[1]:
                    total=(v, d1[v]+d2[v])
                
        return total[0], parent1, parent2
    
    touch, p1, p2 = dij(Adj, w, s, t)
    par=touch
    s_path=[par]
    while par!=s:
        par=p1[par]
        s_path.append(par)
        
    path=s_path[::-1]
    
    while touch!=t:
        touch=p2[touch]
        path.append(touch)
        
    return path

def relax(A, w, d, parent, u, v):
    if d[v] > d[u] + w[(u, v)]:
        d[v] = d[u] + w[(u, v)]
        parent[v] = u

class Item:
    def __init__(self, label, key):
        self.label, self.key = label, key

class PriorityQueue:                      # Binary Heap Implementation
    def __init__(self):                   # stores keys with unique labels
        self.A = []
        self.label2idx = {}

    def min_heapify_up(self, c):            
        if c == 0: return
        p = (c - 1) // 2
        if self.A[p].key > self.A[c].key:   
            self.A[c], self.A[p] = self.A[p], self.A[c]         
            self.label2idx[self.A[c].label] = c
            self.label2idx[self.A[p].label] = p
            self.min_heapify_up(p)         

    def min_heapify_down(self, p):          
        if p >= len(self.A): return
        l = 2 * p + 1
        r = 2 * p + 2
        if l >= len(self.A): l = p
        if r >= len(self.A): r = p
        c = l if self.A[r].key > self.A[l].key else r 
        if self.A[p].key > self.A[c].key:             
            self.A[c], self.A[p] = self.A[p], self.A[c]         
            self.label2idx[self.A[c].label] = c
            self.label2idx[self.A[p].label] = p
            self.min_heapify_down(c)       

    def insert(self, label, key):         # insert labeled key
        self.A.append(Item(label, key))
        idx = len(self.A) - 1
        self.label2idx[self.A[idx].label] = idx
        self.min_heapify_up(idx)

    def find_min(self):                   # return minimum key
        return self.A[0].key

    def extract_min(self):                # remove a label with minimum key
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        self.label2idx[self.A[0].label] = 0
        del self.label2idx[self.A[-1].label]
        min_label = self.A.pop().label
        self.min_heapify_down(0)
        return min_label

    def decrease_key(self, label, key):   # decrease key of a given label
        if label in self.label2idx:
            idx = self.label2idx[label]
            if key < self.A[idx].key:
                self.A[idx].key = key
                self.min_heapify_up(idx)
