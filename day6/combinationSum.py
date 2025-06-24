def combinationSum(candidates, target):
    result = []

    def find_max(arr):
        if arr==[]:
            return 0
        else:
            return max(arr)
        
    def helper(curr):
        if sum(curr) == target:
            result.append(curr[:])
            return 
        
        for j in candidates:
            if sum(curr) + j <= target and j>=find_max(curr):
                curr.append(j)
                helper(curr)
                curr.pop() 

    helper([])
    return result

print(combinationSum([7,6,3,2], 7))