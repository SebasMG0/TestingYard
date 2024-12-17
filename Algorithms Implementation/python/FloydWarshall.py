def fwar(g:list):
    for middle in range(len(g)):
        for initial in range(len(g)):
            for out in range(len(g)):
                g[initial][out]= min(g[initial][out], g[initial][middle]+g[middle][out])
    return g

def toMatrix(g:list):
    m= [[float("inf")]*len(g) for _ in range (len(g))]
    for v in range(len(g)):
        for e in g[v]:
            m[v][e[0]]= e[1]
        m[v][v]= 0
    return m

g1=[
    [(1, 4), (2, 3)],
    [(0, 5)],
    [(4, 5)],
    [(0, 12), (4, 6)],
    [(3, 2), (2, 2)]
]
print(fwar(toMatrix(g1)))
