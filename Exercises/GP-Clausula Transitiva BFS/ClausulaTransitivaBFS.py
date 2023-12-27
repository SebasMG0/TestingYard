from sys import stdin
import json

def BFSListaAdyacencia(grafo : list, nodos: list ) -> bool:
    estaElCamino = False
    nodoInicio = nodos[0]
    nodoObjetivo = nodos[1]
    visitados = set()
    cola = []

    if (nodoInicio >= len(grafo) or nodoObjetivo >= len(grafo)):
        return False

    cola.append(nodoInicio)
    visitados.add(nodoInicio)


    while len(cola) > 0:

        for conexion in grafo[cola[0]]:
            if conexion not in visitados:
                if conexion == nodoObjetivo:
                    return True
                else:
                    if (conexion >= len(grafo)):
                        return False
                    visitados.add(conexion)
                    cola.append(conexion)
        
        cola.pop(0)
    
    return estaElCamino 


def main():
    cantidadDeEntradas = int(stdin.readline().strip())
    for i in range(cantidadDeEntradas):
        grafo = json.loads(stdin.readline().strip())
        nodosInicial = stdin.readline().strip()
        nodos = nodosInicial.split(",")
        for i in range(len(nodos)): 
            nodos[i] = int(nodos[i])
        print(BFSListaAdyacencia(grafo,nodos))


if __name__ == '__main__':
    main()
