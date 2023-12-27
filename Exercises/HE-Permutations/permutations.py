"""
	Prints the permutations of size n taking as range 1..n
"""


def isSolution(n:int, a:list):
    return len(a)==n

def procSolution(a:list):
    for num in a:
        print(num, end=" " )
    print("\n")

def permutations(n:int, k:int, a:int):
    if isSolution(n, a):
        procSolution(a)
    else:
        k+=1
        for candidate in candidates(k, n, a):
            a.append(candidate)
            permutations(n, k, a)
            a.pop()
    return

def candidates(k:int, n:int, a:list):
    ca= []
    for i in range(1, n+1):
        if i not in a:
            ca.append(i)
    return ca

if __name__== "__main__":
    n= 5 # Permutation Size

    permutations(n, k=0, a=[])
    print(counter)
