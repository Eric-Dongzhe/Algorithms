import sys
a = [2,4,6,8,10,12,14]
b = [1,3,5]


def merge(A,p,q,r):
	L = A[p:q+1]
	R = A[q+1:r+1]

	#L.append(sys.maxint)
	L.append(float('inf'))
	#R.append(sys.maxint)
	R.append(float('inf'))
	i = 0
	j = 0
	for k in range(p, r+1):
		if L[i] < R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
		

def merge_sort(A,p,r):
	if p<r:
		q = (p+r)/2
		merge_sort(A,p,q)
		merge_sort(A,q+1,r)
		merge(A,p,q,r)

'''
def merge(left,right):
	merged = []
	i, j = 0, 0
	left_len, right_len = len(left), len(right)
	while i < left_len and j < right_len:

		if left[i] <= right[j]:
			merged.append(left[i])
			i += 1
		else:
			merged.append(right[j])
			j += 1
	merged.extend(left[i:])
	merged.extend(right[j:])
	return merged


def merge_sort(lst):
	if len(lst) <= 1:
		return lst

	middle = len(lst) // 2
	left = merge_sort(lst[:middle])
	right = merge_sort(lst[middle:])
	return merge(left, right)
'''

merge_sort(a,0,len(a)-1)
print a