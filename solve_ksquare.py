def is_solved(config):
    "Return whether input config is solved"
    k=len(config)
    for r in range(k):
        for c in range(k):
            if config[r][c]!=r*k+c+1:
                return False
    return True 

def move(config, mv):
    "Return a new configuration made by moving config by move mv"
    k = len(config)
    (s, i) = mv         # s in ("row", "col") and i in range(k)
    c=[]
    for row in config:
        temp=list(row)
        c.append(temp)
    if s=='row':
        temp=[-x for x in c[i]][::-1]
        c[i]=temp
    elif s=='col':
        temp=[]
        for row in c:
            temp.append(row[i])
        temp=[-x for x in temp][::-1]
        for x in range(len(temp)):
            c[x][i]=temp[x]
    return tuple([tuple(row) for row in c])

def solve_ksquare(config):
    "Return a list of moves that solves config"
    k=len(config)
    def backtrace(con,parent,end,seq=None):
        if seq is None:
            seq=[]
        if con==end:
            return seq[::-1]
        nex=parent[con]
        seq.append(nex[1])
        return backtrace(nex[0],parent,end,seq)
    def helper(nex_level,graph=None,parent=None,checked=None):
        if parent is None:
            parent=dict()
        if graph is None:
            graph=dict()
        if checked is None:
            checked=set()
        if len(nex_level)==0:
            return 'ERROR'
        new_level=set()
        for each in nex_level:
            checked.add(each)
            if is_solved(each):
                return backtrace(each,parent,config)
            for i in range(k):
                r=('row',i)
                new_con=move(each,r)
                graph[new_con]=r
                if new_con not in parent:
                    parent[new_con]=(each,r)
                new_level.add(new_con)
                c=('col',i)
                new_con=move(each,c)
                graph[new_con]=c
                if new_con not in parent:
                    parent[new_con]=(each,c)
                new_level.add(new_con)
        return helper(new_level,graph,parent,checked)
        
    return helper({config})

##c2=move(C1, ("col", 2))
##print(solve_ksquare(c2))
##c3=move(c2,('row',3))
##print(solve_ksquare(c3))
##c4=move(c3,('col',0))
##print(solve_ksquare(c4))
##c5=move(c2,('col',1))
##print(solve_ksquare(c5))
