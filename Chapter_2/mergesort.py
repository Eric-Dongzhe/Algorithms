import sys

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

'''
def merge(A,p,q,r):
	L = A[p:q+1]
	R = A[q+1:r+1]
	i = 0
	j = 0
	k = p
	while i < len(L) and j < len(R):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
		k =+1
'''

def merge_sort(A, p, r):
	if p<r:
		q = (p+r) / 2
		merge_sort(A, p, q)
		merge_sort(A, q+1, r)
		merge(A, p, q, r)


def merged(L,R):
	merged = []
	i, j = 0, 0
	L_len, R_len = len(L), len(R)
	while i < L_len and j < R_len:
		if L[i] <= R[j]:
			merged.append(L[i])
			i += 1
		else:
			merged.append(R[j])
			j += 1
	merged.extend(L[i:])
	merged.extend(R[j:])
	return merged


def merge_sorted(lst):
	if len(lst) <= 1:
		return lst

	middle = len(lst) // 2
	L = merge_sorted(lst[:middle])
	R = merge_sorted(lst[middle:])
	return merged(L, R)


res = merge_sorted(lst)
print res