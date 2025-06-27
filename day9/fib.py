# Recursive approach: T = O(2^N), S = O(n)
# def fib(n):
#     sum = 0
    
#     if n == 0 :
#         return 0
#     if n == 1:
#         return 1
    
#     sum  = fib(n-1) + fib (n-2)
#     return sum

# print(fib(8))


#With Memoization  : Approach 2 , both T & S = O(n)
# def fib(n, ht = {0 : 0, 1 : 1}):
#     if n in ht:
#         return ht[n]
#     else:
#         ht[n] = fib(n-1, ht) + fib(n-2, ht)
#         return ht[n]

# print(fib(9))

#Tabulation, both T & S = O(n)
# def fib(n):
#     array = [0]*(n+1)

#     if n>0:
#         array[1] = 1
    
#     count = 1

#     while count < n:
#         count += 1
#         array[count] = array[count-1] + array[count-2]

#     return array[n]

# print(fib(9))

# Space = O(1)
def fib(n):
    if n<=1:
        return n
    
    prev = 0
    curr = 1
    count = 1

    while count < n:
        next = prev + curr
        count+=1
        prev = curr
        curr = next
    return curr
        

    


print(fib(9))


