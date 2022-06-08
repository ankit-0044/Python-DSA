def binary_search(list,item):
	low = 0 
	high = len(list) -1
	
	while low <=  high:
		mid = (low + high)
		guess = list[mid]
		if guess == item:
			return mid
		elif guess > item:
			high = mid -1
		else:
			low = mid + 1
my_list =[1,3,5,7,9]

result1 = binary_search(my_list,3)
result2 = binary_search(my_list,-1)
print(f"Element 3 is at position: {result1}")
print(f"Element -1 is at position: {result2}")