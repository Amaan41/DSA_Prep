def climbStairs(n):
    ht = {1:1, 2:2}
    if n in ht:
        return ht[n]
    else:
        ht[n] = climbStairs(n-1) + climbStairs(n-2)
        return ht[n]
    
print(climbStairs(4))
