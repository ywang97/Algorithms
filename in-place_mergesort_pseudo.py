def Merge(A, a1, a2, b1, b2, w): # merge subarray A[a1: a2] and A[b1: b2]
    # working area starts at index w
    i, j, k = a1, b1, w
    while i<a2 and j<b2: 
        if A[i]<A[j]:
            swap (A, i, k) # swap the smaller with some element in the working area
            i += 1
        else:
            swap (A, j, k)
            j += 1
        k += 1

    # swap back elements to working area
    i, j, k = a1, b1, w
    while i<a2:
        swap (A, i, k)
        i += 1, k += 1
    while j<b2:
        swap (A, j, k)
        j += 1, k += 1

    
