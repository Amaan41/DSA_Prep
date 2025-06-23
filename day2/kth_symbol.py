def kth_symbol(n, k):
    if n==1 or k==1:
        return 0
    if n==2 and k==2:
        return 1
    l = 2**(n-1)
    mid = l/2
    if k>mid:
        return int(not kth_symbol(n-1,k-mid))
    else:
        return kth_symbol(n-1,k)
        
print(kth_symbol(4,8))
