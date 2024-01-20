"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.
"""

def countBits(n: int) -> list[int]:
    ans= [0]
    l= 0

    while len(ans)<=n:
        if ans[-1]==l:
            ans.append(1)
            l+=1

        t= []
        k= len(ans)
        for i in range(1, k-1):
            if k + len(t) == n+1: break
            t.append(ans[i]+1)
        ans.extend(t)
    return ans

for i in range(0, 10):
    print("--"*8)
    print(i, ":", countBits(i))
