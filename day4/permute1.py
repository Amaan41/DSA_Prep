def permute(nums):
    result = []

    def backtrack(i):
        if i == len(nums)-1:
            result.append(nums[:])

        for j in range(i,len(nums)):
            nums[i],nums[j] = nums[j],nums[i]
            backtrack(i+1)
            nums[i],nums[j] = nums[j],nums[i]
    
    backtrack(0)
    return result

a = [1]
print(permute(a))