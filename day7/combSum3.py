def combine(k,n):
    res = []

    def helper(i, curr):
        #base case
        if sum(curr) == n and len(curr) == k:
            res.append(curr[:])
            return
        if sum(curr) > n or len(curr) == k:
            return
        
        #rec case

        for j in range(i,10):
            curr.append(j)
            helper(j+1, curr)
            curr.pop()
        
    helper(1,[])
    return res
    

print(combine(3,9))


