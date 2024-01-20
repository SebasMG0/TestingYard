"""
 You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""

def climbingStairs(n:int)->int:
    i, j, k= 0, 1, 0

    for _ in range (n):
        k= i+j
        i= j
        j= k

    return k


def climbStairs(n: int) -> int:
    dp= [1, 1]
    for _ in range(n-1):
        dp.append(dp[-1]+dp[-2])
    return dp[-1]



for i in range(1, 46):
    print("--"*8)
    print(climbingStairs(i))
    print(climbStairs(i))
    print("--"*8)
