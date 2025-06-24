def combinationSum2(candidates, target):
    #write code here
    candidates.sort()
    result = []
    n = len(candidates)
    def helper(i, curr, curr_sum):
        #base case
        if  curr_sum == target:
            result.append(curr[:])
            return 
        if curr_sum > target:
            return
        if i > n-1:
            return
        #recursive case

        hash = {}

        for j in range(i, n):
            if candidates[j] not in hash:
                hash[candidates[j]] = True
                curr.append(candidates[j])
                helper(j+1, curr, curr_sum+candidates[j])
                curr.pop()

    helper(0, [], 0)
    return result
        
        
print(combinationSum2([3,5,2,1,3], 7))
        
        
    