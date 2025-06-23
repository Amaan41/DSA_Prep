# Unique elements only
def permUnique(nums):
    result = []

    def backtrack(i):
        if i == len(nums)-1:
            result.append(nums[:])

        hashtable = {}

        for j in range(i,len(nums)):
            if nums[j] not in hashtable:
                hashtable[nums[j]] = True
                nums[i],nums[j] = nums[j],nums[i]
                backtrack(i+1)
                nums[i],nums[j] = nums[j],nums[i]
    
    backtrack(0)
    return result

a = [1,1,2]
print(permUnique(a))