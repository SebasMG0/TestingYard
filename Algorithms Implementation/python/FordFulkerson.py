from sys import stdin, stdout
from collections import deque

# g: Red de flujo, s:Nodo Inicial, f:Nodo Final
def dfs(g:list, s:int, f:int):
    q= deque([s]) # Pila para los nodos a visitar
    vd= [False]*len(g) # Lista de visitados
    p= [-1]*len(g) # Lista en la que se almacena el "Padre" de cada nodo

    while q: # Mientras hayan nodos por visitar
        n= q.popleft() # Nodo actual
        vd[n]= True # Marcar como visitado

        e= g[n] # Ejes del nodo n
        for i in range(len(e)):
            if e[i]==0 or vd[i] : continue # Continue si el nodo ya fue visitado o su capacidad es 0

            p[i]= n # Actualiza el padre del nodo
            if i== f: # Nodo final alcanzado
                return getPath(p, s, f) # Convertir la lista de padres en el camino que se siguió

            q.append(i) # Añadir el nodo a la cola
    return False

# g: Red de flujo, s:Nodo Inicial, f:Nodo Final
def bfs(g:list, s:int, f: int):
    q= deque([s]) # Pila para los nodos a visitar
    vd= [False]*len(g) # Lista de visitados
    p= [-1]*len(g) # Lista en la que se almacena el "Padre" de cada nodo

    while q: # Mientras hayan nodos por visitar
        n= q.pop() # Nodo actual
        vd[n]= True # Marcar como visitado

        e= g[n] # Ejes del nodo n
        for i in range(len(e)):
            if e[i]==0 or vd[i] : continue # Continue si el nodo ya fue visitado o su capacidad es 0

            p[i]= n # Actualiza el padre del nodo
            if i== f: # Nodo final alcanzado
                return getPath(p, s, f) # Convertir la lista de padres en el camino que se siguió

            q.append(i) # Añadir el nodo a la cola
    return False

# p:Lista de padres , s:Nodo Inicial, f:Nodo Final
def getPath(p:list, s:int, f:int):
    path= deque([f])
    i= f
    while i != s: # Mientras no se haya alcanzado el nodo incial
        path.appendleft(p[i]) # Añada al principio el padre del nodo actual
        i= p[i] # Ahora el nodo a revisar es el padre
    return path # Cola con los nodos del camino de expansión en orden

# g: Red de flujo, p: Cola/lista de padres
def getMin(g:list, p:list):
    m= float("inf")
    c= 0
    while c<len(p)-1:
        m= min(m, g[p[c]][p[c+1]])
        c+=1
    return m

# g: grafo de la red de flujo, s:Nodo Inicial, f:Nodo Final, pathFuntion: dfs o bfs
def fordFulkerson(g:list, s:int, f:int, pathFunction):
    p= pathFunction(g, s, f) # Nodos del camino de expansión o falso si no hay más

    while p:
        m= getMin(g, p) # Cuello de botella
        c= 0
        while c<len(p)-1: # Se itera por cada eje del camino
            i= p[c]
            j= p[c+1]

            g[i][j] -= m # Disminución de la capacidad
            g[j][i] += m # Aumento del flujo

            c+=1
        p= pathFunction(g, s, f)
    return sum(g[f])

if __name__== "__main__":
    c= int( stdin.readline().strip() ) # Casos de prueba

    for _ in range (c):
        v= int( stdin.readline().strip() ) # Vértices
        e= int( stdin.readline().strip() ) # Ejes

        g= [[0]*v for _ in range(v)] # Inicialización de la red de flujo

        for _ in range (e):
            l= stdin.readline().split()
            g[int(l[0])][int(l[1])]= int(l[2])

        # Como último parámetro la función recibe la referencia a la función que hallará los caminos de expansión
        # En este caso las funciones tienen por nombre: bfs o dfs
        stdout.write(str(fordFulkerson(g, 0, v-1, bfs)))
        stdout.write("\n")
