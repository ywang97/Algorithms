def search_sorted_2D_array(A, v):
    
    '''
    Return tuple (x, y) such that A[y][x] == v, or None.
    Input:  A | Array of equal length arrays of integers 
              |     representing the rows of a 2D array
              |     where A[y][x] >= A[y - 1][x] and
              |           A[y][x] >= A[y][x - 1] 
              |     for all (x, y) in range.
            v | An integer to search for in A.
    '''
    n = len(A)
    m = len(A[0])
    def find_s(A,v,x=0,y=n-1):
        if x >= m or y < 0:
            return None
        s = A[y][x]
        if s < v:
            x+=1
            return find_s(A,v,x,y)
        elif s > v:
            y-=1
            return find_s(A,v,x,y)
        elif s == v:
            return (x,y)
    return find_s(A,v)
