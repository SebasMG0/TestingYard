from collections import deque

def isBipartite(g:list):
    s= [True for _ in range(len(g))] # Se utilizan true y false como representación de los conjuntos 0 y 1
    vd= [False for _ in range(len(g))] # Lista de "Asignados"
    q= deque([0]) # Cola para aplicar bfs
    vd[0]= True # Asignar el valor inicial

    while q:
        v= q.popleft() # Vértice

        for e in g[v]:
            isAsigned= vd[e[0]]
            if isAsigned and s[e[0]] == s[v]: # Si el vertice destino ya fue asignado y en la iteración actual debe cambiarse
                return False
            elif not isAsigned:
                q.append(e[0]) # Añadir a la cola
                s[e[0]]= not s[v] # Su asignación será el conjunto al que no pertenece su padre
                vd[e[0]]= True # Marcar el nodo destino como asignado

    return True


g1=[
    [(1, 4), (2, 3)],
    [(0, 5)],
    [(0, 12), (4, 6)],
    [(4, 5)],
    [(3, 2), (2, 2)]
]
print(isBipartite(g1))

g2= [
    [(1, 2), (3, 5)],
    [(2, 4), (3, 5)],
    [(5, 2)],
    [(4, 3)],
    [(5, 4)],
    []
]
print(isBipartite(g2))
