from sys import stdin
import json

def bfs(g:list, i:int, j:int):
    if not (0<=i<len(g) and 0<=j<len(g)): return False
    queue= [i]
    visited= set()

    while queue:
        i= queue.pop(0)
        visited.add(i)

        for k in g[i]:
            if k==j: return True
            if k not in visited: queue.append(k)
    
    return False


def main():
    cantidadDeEntradas = int(stdin.readline().strip())
    for i in range(cantidadDeEntradas):
        grafo = json.loads(stdin.readline().strip())
        nodosInicial = stdin.readline().strip()
        nodos = nodosInicial.split(",")
        for i in range(len(nodos)): 
            nodos[i] = int(nodos[i])
        print(bfs(grafo,nodos[0], nodos[1]))


if __name__ == '__main__':
    main()