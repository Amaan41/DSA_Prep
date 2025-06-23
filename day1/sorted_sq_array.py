def sorted_array(array):
    new_array = [0]*len(array);
    i,j = 0, len(array)-1;
    k = len(array)-1;
    while i<=j:
        if array[i]**2 < array[j]**2:
            new_array[k] = array[j]**2;
            j-=1
        else: 
            new_array[k] = array[i]**2;
            i+=1
        k-=1;
    print(new_array);

a = [-5,-2,-1,2,3,3,7]
sorted_array(a)


        

