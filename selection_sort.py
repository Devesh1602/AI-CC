# time complexity O(n*n)
# space complexity O(1)
#sorting by finding min_index
def selectionSort(array, size):
	
	for i in range(size):
		min_index = i

		for j in range(i + 1, size):
			# select the minimum element in every iteration
			if array[j] < array[min_index]:
				min_index = j
		# swapping the elements to sort the array
		(array[i], array[min_index]) = (array[min_index], array[i])

user_input = input("Enter the elements of the array: ")
arr = list(map(int, user_input.split()))
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)

'''
Enter the elements of the array (space-separated): 5 2 8 -1 0 3
The array after sorting in Ascending Order by selection sort is:
[-1, 0, 2, 3, 5, 8]

'''