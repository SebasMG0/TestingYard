def kruskal(g:list, po:int):
    f= [] # Forest o conjunto de árboles -> En principio un arbol por cada vértice
    q= [] # Lista con los ejes del grafo: (a, b, peso)
    t= [] # Árbol de recubrimiento mínimo


    for i in range (len(g)): # Obtener los ejes del grafo y añdirlos a q
        f.append({i})
        for j in range(len(g[i])):
            q.append((i, g[i][j][0], g[i][j][1]))

    q.sort(key= lambda edge: edge[2]) # Ejes ordenados por pesos: a, b, peso

    for i in range(len(q)): # Recorrido por todos los ejes
        s= findSetIndex(f, q[i][0], q[i][1]) # s: índice_conjunto(a), índice_conjunto(b)
        if s[0]!= s[1]: # Si los vértices están en conjuntos diferentes
            t.append(q[i]) # Añadir como eje perteneciente al árbol
            joinSets(f, s[0], s[1])
    return t if len(t)==len(g)-1 else False # Retorna el arbol; si no hay, False

def findSetIndex(f:list, po:int, pf:int):
    o, l= -1, -1 # Índices para los vértices
    for i in range(len(f)): # Para cada conjunto definido
        if po in f[i]:
            o= i
        if pf in f[i]:
            l= i
        if o>=0 and l>=0:
            break
    return o, l

def joinSets(f:list, s0, s1):
    f[s0]= f[s0] | f[s1]
    f[s1].clear()

g1=[
    [(1, 4), (2, 3)],
    [(0, 5)],
    [(4, 5)],
    [(0, 12), (4, 6)],
    [(3, 2), (2, 2)]
]
print(kruskal(g1, 0))
