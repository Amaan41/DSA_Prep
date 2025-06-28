def minCostClimbingStairs(cost):
    def helper(index):
        if index > len(cost) - 1:
            return 0

        onestep = cost[index] + helper(index + 1)
        twostep = cost[index] + helper(index + 2)    
        return min(onestep, twostep)
    return min(helper(0), helper(1))

minCostClimbingStairs([10,20,30])
