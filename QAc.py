def pivot(lis,low,high): 
    i = ( low-1 )         
    pivot = lis[high]     
  
    for j in range(low , high): 
        if   lis[j] < pivot:  
            i = i+1 
            lis[i],lis[j] = lis[j],lis[i] 
  
    lis[i+1],lis[high] = lis[high],lis[i+1] 
    return ( i+1 ) 
def quick_sort(lis,low,high): 
    if low < high: 
        pi = pivot(lis,low,high) 
        quick_sort(lis, low, pi-1) 
        quick_sort(lis, pi+1, high) 
  
lis = [5,4,3,2,1] 
n = len(lis) 
quick_sort(lis,0,n-1) 
print ("Sorted list is:") 
print(lis)
