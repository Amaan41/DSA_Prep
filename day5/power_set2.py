def power_set(nums):
    nums.sort()
    result = []
    
    def helper(i, curr):
        #base
        if i == len(nums):
            result.append(curr[:])
            return
        
        #include
        curr.append(nums[i])
        helper(i+1, curr)
        curr.pop()
        
        #exclude
        while i<len(nums)-1 and nums[i]==nums[i+1]:
            i+=1
        helper(i+1, curr)
        
    helper(0,[])
    return result

a  = [1,3,3]
print(power_set(a))
