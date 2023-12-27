def bellmanFord(g:list, po:int):
    w= [float("inf") for _ in range(len(g))]
    w[po]= 0

    for _ in range(len(g)-1):
        i=0
        for v in g:
            for e in v:
                cw= w[i]+e[0]
                if w[e[1]] > cw:
                    w[e[1]]= cw
            i+= 1
    return w

g= [ [(4, 1), (2, 2)],
     [(3, 2), (2,3), (3, 4)],
     [(1, 1), (4, 3), (5, 4)],
     [],
     [(1, 3)]
]
#Expected result: [0, 3, 2, 5, 6]
print(bellmanFord(g, 0))

g1= [ [(2, 2)],
      [(1, 0)],
      [(-2, 1)],
      [(-4, 0), (-1, 2)],
      [(1, 3)],
      [(8, 4), (10, 0)]
]
# Expected Result: [5, 5, 7, 9, 8, 0]
print(bellmanFord(g1, 5))
