from collections import deque

# g: Grafo, s:Nodo Inicial, f:Nodo Final
def bfs(g:list, s:int, f: int):
    q= deque([s]) # Cola para los nodos a visitar
    vd= [False]*len(g) # Lista de visitados
    p= [-1]*len(g) # Lista en la que se almacena el "Padre" de cada nodo

    while q: # Mientras hayan nodos por visitar
        n= q.pop() # Nodo actual
        vd[n]= True # Marcar como visitado

        for e in g[n]: # Para cada eje del nodo actual
            if vd[e[0]] or e[1]==0: continue # Continue si el nodo ya fue visitado o su capacidad es 0

            p[e[0]]= n # Actualiza el padre del nodo
            if e[0]== f: # Nodo final alcanzado
                return getPath(p, s, f) # Convertir la lista de padres en el camino que se siguió

            q.append(e[0]) # Añadir el nodo a la cola
    return False
