# find the max subarray in the array A

def find_max_crossing_subarray(arr, low, mid, high):
	left_sum = -float('inf')
	sum = 0
	for i in range(low, mid+1)[::-1]:
		sum += arr[i]
		if sum > left_sum:
			left_sum = sum
			max_left = i

	right_sum = -float('inf')
	sum = 0
	for j in range(mid+1, high+1):
		sum += arr[j]
		if sum > right_sum:
			right_sum = sum
			max_right = j
	return(max_left, max_right, left_sum+right_sum)



def find_max_subarray(arr, low, high):
	if low == high:
		return (low, high, arr[low])
	else:
		mid = (low+high)/2
		(left_low, left_high, left_sum) = find_max_subarray(arr, low, mid)
		(right_low, right_high, right_sum) = find_max_subarray(arr, mid+1, high)
		(cross_low, cross_high, cross_sum) = find_max_crossing_subarray(arr, low, mid, high)
		if left_sum >= right_sum and left_sum >= cross_sum:
			return (left_low, left_high, left_sum)
		elif right_sum >= left_sum and right_sum >= cross_sum:
			return (right_low, right_high, right_sum)
		else:
			return (cross_low, cross_high, cross_sum)


def get_max_subarray(A):
	(low, high, sum) = find_max_subarray(A,0,len(A)-1)
	max_sub_A = A[low:high+1]
	return max_sub_A


#a = [1,-1,1,1,-1,0,0,0,0,80]
# a = [1, -4, 3, 5, -7, 2, 8, -9]
a = [1]
# a = [1, -2, 3]
#a = [1, -2, 3, 4, 8, -10, 13, 21, -13]

#(low, high, sum) = Find_Max_Crossing_Subarray(a,0,len(a)/2,len(a)-1)

print find_max_subarray(a,0,len(a)-1)

print get_max_subarray(a)

'''

a=[1,3,5,9,12]
#倒序遍历两种方法
for i in range(5, 0, -1):
	# 5,4,3,2,1
	print i

for i in range(0,5)[::-1]:
	# 4,3,2,1,0
	print i
'''
