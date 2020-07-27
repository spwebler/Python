# Function to move all zeros present in the list to the end
def reorder(A):

	# k stores index of next available position
	k = 0

	# do for each element
	for i in A:
		# if current element is non-zero, put the element at
		# next free position in the list
		if i:
			A[k] = i
			k = k + 1

	# move all 0's to the end of the list (remaining indices)
	for i in range(k, len(A)):
		A[i] = 0


# Move all zeros present in the list to the end
if __name__ == '__main__':

	A = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]

	reorder(A)
	print(A)
