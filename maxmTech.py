def maxnum(arr):
	if len(arr)==1:
		return arr[0]

	n=len(arr)//2
	left = arr[:n]
	right = arr[n:]
	# maxnum(left)
	# maxnum(right)

	return max(maxnum(left),maxnum(right))


arr = (3, 7, 4, 6, 1, 8, 2, 5)	
print(maxnum(arr))


# for row in range(5,0,-1):
# 	for col in range(row):
# 		print("*",end = "")
# 	print()
