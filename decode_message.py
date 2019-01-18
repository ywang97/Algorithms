def decode_message(A):
    """
    Return the first half of the longest palindrome subsequence of string A
    """
    n = len(A)
    if n==0:
        return ''
    L = [[0 for i in range(n)] for j in range(n)]
    pointer = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        L[i][i] = 1
        pointer[i][i] = (True, i, i)
    for ln in range(2, n+1):
        for i in range(n-ln+1):
            j = i+ln-1
            if A[i] == A[j]:
                if ln == 2:
                    L[i][j] = 2
                    pointer[i][j] = (True, i, j)
                else:
                    L[i][j] = L[i+1][j-1]+2
                    pointer[i][j] = (True, i+1, j-1)
            else:
                if L[i][j-1] > L[i+1][j]:
                    L[i][j] = L[i][j-1]
                    pointer[i][j] = (False, i, j-1)
                else:
                    L[i][j] = L[i+1][j]
                    pointer[i][j] = (False, i+1, j)
    i, j = 0, n-1
    out = ''
    while True:
        boolean, nex_i, nex_j = pointer[i][j]
        if boolean:
            out+=A[j]
        if j-i == 1 or i==j:
            break
        i, j = nex_i, nex_j      
    return out

