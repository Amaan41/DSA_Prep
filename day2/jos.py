# def find_the_winner(n,k):
#     def elim(a,start):
#         if len(a)==1:
#             return a[0]
#         remove = (start + k - 1) % len(a)
#         a.pop(remove)
#         return elim(a,remove)

#     a=[]
#     for i in range(1,n+1):
#         a.append(i)
#     return elim(a,0)


#print(find_the_winner(41,2))

def findTheWinner(n,k):
    if n==1:
        return 0;
    else: 
        return (findTheWinner(n-1,k) + k) % n 
    
print(findTheWinner(41,2)+1)

# def win(n,k):
#     winner_index=0
#     for i in range(2,n+1):
#         winner_index = (winner_index + k) % i
#     return winner_index + 1

# print(win(41,2))

