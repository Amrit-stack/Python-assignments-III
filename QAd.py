def merge(lis, l, m, r):
	n1 = m - l + 1
	n2 = r- m  
	L = [0] * (n1) 
	R = [0] * (n2) 
	for i in range(0 , n1): 
		L[i] = lis[l + i] 

	for j in range(0 , n2): 
		R[j] = lis[m + 1 + j] 
	i = 0	 
	j = 0	 
	k = l	 

	while i < n1 and j < n2 : 
		if L[i] <= R[j]: 
			lis[k] = L[i] 
			i += 1
		else: 
			lis[k] = R[j] 
			j += 1
		k += 1

	while i < n1: 
		lis[k] = L[i] 
		i += 1
		k += 1

	
	while j < n2: 
		lis[k] = R[j] 
		j += 1
		k += 1


def merge_sort(lis,l,r):
	if l < r:
		m = (l+(r-1))//2
		merge_sort(lis, l, m) 
		merge_sort(lis, m+1, r) 
		merge(lis, l, m, r) 



lis = [5,4,3,2,1] 
n = len(lis) 
print ("Given array is") 
print(lis)
merge_sort(lis,0,n-1) 
print ("\nSorted array is") 
print(lis)

