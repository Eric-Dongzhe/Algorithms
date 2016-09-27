def insertion_sort(A):
	for j in range(1, len(A)):
		key = A[j]
		i = j - 1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key


a = [10,9,8,7,5,6,4,2,3,1,52,12]
insertion_sort(a)
print a