def power_set(nums):
    result = []

    def helper(nums, i, subset):

        if i==len(nums):
            result.append(subset[:])
            return
        
        helper(nums, i+1, subset)
        subset.append(nums[i])
        helper(nums, i+1, subset)
        subset.pop()

    helper(nums, 0, [])
    return result

a =[1,2,3]

print(power_set(a))

