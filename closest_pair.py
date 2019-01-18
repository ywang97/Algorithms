
def squared_distance(p, q):
    '''Returns the squared distance between points p and q'''
    (px, py), (qx, qy) = p, q
    return (px - qx)**2 + (py - qy)**2

def closest_pair(points):
    ''' 
    Input:  points | tuple of at least 2 points of the form (x, y)
    Output: smallest squared distance between any pair of points
    '''
    ##################
    # YOUR CODE HERE #
    ##################

    #sort x, sort y
    #find closest

    
    def bruteforce(po):
        mi=squared_distance(po[0],po[1])
        ln=len(po)
        if ln==2:
            return mi
        for i in range(ln-1):
            for j in range(i+1,ln):
                
                d=squared_distance(po[i],po[j])
                   
                if d<mi:
                    mi=d
        
        return mi

    def split(xl,yl,dist):
        lnx=len(xl)
        mx=xl[lnx//2][0]
        strip=[x for x in yl if (mx-dist)<=x[0]<=(mx+dist)]
        shortest=dist
        ln=len(strip)
        for i in range(ln-1):
            for j in range(i+1,min(i+7,ln)):
                p,q=strip[i],strip[j]
                dd=squared_distance(p,q)
                if dd<shortest:
                    shortest=dd
        return shortest
                
    def cp(x_sort,y_sort):
        xlen=len(x_sort)
        if xlen<=3:
            return bruteforce(x_sort)
        mid=int(xlen//2)
        ax=x_sort[:mid]
        bx=x_sort[mid:]
        midx=x_sort[mid][0]
        ay=list()
        by=list()
        for i in y_sort:
            if i[0]<=midx:
                ay.append(i)
            else:
                by.append(i)
        dl = cp(ax,ay)
        dr = cp(bx,by)
        delta=min(dl,dr)
        across=split(x_sort,y_sort,delta)
        return min(delta,across)

    ax=sorted(points,key=lambda x:x[0])
    ay=sorted(points,key=lambda y:y[1])
    
    out=cp(ax,ay)
    
    return out

