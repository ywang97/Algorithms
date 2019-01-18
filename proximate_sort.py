def proximate_sort(A, k):
    ''' 
    Return an array containing the elements of 
    input tuple A appearing in sorted order.
    Input:  k | an integer < len(A)
            A | a k-proximate tuple
    '''
    ##################
    # YOUR CODE HERE #
    ##################
    def parent(i):
        p=(i-1)//2
        return p if 0<i else i
    def left(i,n):
        l=2*i+1
        return l if l<n else i
    def right(i,n):
        r=2*i+2
        return r if r<n else i
    def min_heapify_up(A,n,c):
        p=parent(c)
        if A[p]>A[c]:
            A[c],A[p]=A[p],A[c]
            min_heapify_up(A,n,p)
    def min_heapify_down(A,n,p):
        l,r=left(p,n),right(p,n)
        c=l if A[l]<A[r] else r
        if A[c]<A[p]:
            A[c],A[p]=A[p],A[c]
            min_heapify_down(A,n,c)
    def build_min_heap(A,n):
        for i in range(n//2, -1,-1):
            min_heapify_down(A,n,i)
    def insert(A,v):
        A.append(v)
        min_heapify_up(A,len(A),len(A)-1)
    def remove_min(A):
        A[0],A[len(A)-1]=A[len(A)-1],A[0]
        result=A.pop()
        if len(A)>1:
            min_heapify_down(A,len(A),0)
        return result
    def merge(L,R):
        l=0
        r=0
        while l<len(L) or r<len(R):
            if l<len(L) and (r>=len(R) or L[l]<=R[r]):
                yield L[l]
                l+=1
            else:
                yield R[r]
                r+=1
    def merge_sort(A,i=0,j=None):
        if j is None:
            j=len(A)
        if j-i==1:
            return [A[i]]
        m=(i+j)//2
        L=merge_sort(A,i,m)
        R=merge_sort(A,m,j)
        return list(merge(L,R))
    ln=len(A)
    if 2**k>100*ln:
        return merge_sort(A)
    sort=[]
    heap=list(A[:k+1])
    build_min_heap(heap,k+1)
    for i in range(ln):
        sort.append(remove_min(heap))
        if i+k+1<ln:
            insert(heap,A[i+k+1])
    return sort
