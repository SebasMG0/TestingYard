"""
    Permutaciones que cumplen: permutación [i] != i
"""

counter= 0

def processSolution(a):
    print(a)

def isSolution(n, k):
    return n==k

def genCandidates(a:list, k:int, n:int ):
    #Determina si el elemento i está o no en la permutación
    inPerm= [False]*(n+1)
    candidatos= []

    for v in a:
        inPerm[v]= True

    for i in range(1, len(inPerm)):
        if not inPerm[i] and i!=k:
            candidatos.append(i)

    return candidatos

def backtracking(a, k, n):
    if isSolution(n, k):
        processSolution(a)

        # Contador
        global counter
        counter+=1

    else:
        # Siguiente paso en la ejecución y nuevos candidatos
        k+=1
        candidatos= genCandidates(a, k, n)

        # Para cada candidato posible en la posición dada
        for c in candidatos:
            a.append(c) # Añadir el candidato
            backtracking(a, k, n)
            a.pop(-1) #Eliminarlo el candidato para utilizar otro

def genPermutations(n:int):
    a= []
    k= 0
    backtracking(a, k, n)

    global counter
    print(counter)

genPermutations(5)
