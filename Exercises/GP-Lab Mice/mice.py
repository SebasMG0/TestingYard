from sys import stdin, stdout
from queue import PriorityQueue

def dijsktra_queue(g:list, po:int):
    # Definición de estructuras
    w= [float("inf")]*len(g) # Pesos
    s= [False]*len(g) # Visitados
    q= PriorityQueue() #Cola de prioridad: (peso, vértice)

    # Estado inicial de las estructuras
    w[po]= 0
    q.put((0, po))

    while not q.empty():
        v= q.get() # v= (peso, vértice)
        if s[v[1]]: continue # Si el vértice ya fue visitado continuamos con la siguiente iteración
        s[v[1]]= True # Marcar el vértice como visitado

        for e in g[v[1]]: # e= (vértice, peso)
            # Relajar el vértice
            lw= v[0]+ e[1] # Peso para llegar al vértice
            if w[e[0]]> lw: # Si el peso actual registrado es mayor al encontrado en la iteración
                w[e[0]]= lw # Reemplazar por el peso encontrado

                if not s[e[0]]: #Si el eje lleva a un vértice que no ha sido visitado
                    q.put( (w[e[0]], e[0]) ) # Añadir el vértice a la cola
    return w


if __name__ == "__main__":

    cases= int(stdin.readline().strip())
    stdin.readline()

    for _ in range(cases):
        n= int(stdin.readline().strip())
        e= int(stdin.readline().strip())
        t= int(stdin.readline().strip())
        c= int(stdin.readline().strip())

        g= [[] for _ in range (n)] # Inicialización del grafo como una lista de adyacencia (Los nodos comienzan desde 0)

        for _ in range(c):
            l= stdin.readline().strip().split()
            g[int(l[0])-1].append((int(l[1])-1, int(l[2]))) # Se añaden las conexiones a la lista de adyacencia

        r=0
        for i in range(n):
            if dijsktra_queue(g, i)[e-1]<= t: r+=1 #Ejecutar Dijsktra para cada vértice y sumar 1 al resultado si aplica

        stdout.write(str(r)+"\n\n")
        stdin.readline()
