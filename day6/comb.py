# def combine(n,k):
#     result  = []

#     def helper(i, curr):
#         if len(curr) == k:
#             result.append(curr[:])

#         for j in range(i, n+1):
#             curr.append(j)
#             helper(j+1, curr)
#             curr.pop()
    
#     helper(1,[])
#     return result

# print(combine(4,3))

#Optimised

def combine(n,k):
    result  = []

    def helper(i, curr):
        if len(curr) == k:
            result.append(curr[:])
            return

        need = k-len(curr)  #optimisation

        for j in range(i, n-(need-1)+1):    #opt : exclude branches that won't give that req length 'k'
            curr.append(j)
            helper(j+1, curr)
            curr.pop()
    
    helper(1,[])
    return result

print(combine(4,3))

