def insertion_sort(A):
	for j in range(1, len(A)):
		key = A[j]
		i = j - 1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key


def insertion_sorted(A):
	sorted = []
	for i in range(A)

	for j in range(1, len(A)):
		key = A[j]
		i = j - 1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key
	return A


a = [10,9,8,7,5,6,4,2,3,1,52,12]
b = insertion_sorted(a)
print a