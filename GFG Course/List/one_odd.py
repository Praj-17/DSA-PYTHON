def getOddOccurrence(arr):

	# Initialize result
	res = 0
	
	# Traverse the array
	for element in arr:
		# XOR with the result
		res = res ^ element

	return res
print(getOddOccurrence([1,2,2,3,3,4,4,5,5]))

print(5^6)