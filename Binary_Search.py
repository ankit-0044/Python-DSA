# defining function with two parameters
def binary_search(sorted_list, item):
	# initialize low and high variable
	low = 0 
	high = len(sorted_list) -1
	
	# checking and comparing
	while low <=  high:
		mid = int( (low + high) / 2)
		guess = sorted_list[mid]
		
		if guess == item:
			return mid
			
		elif guess > item:
			high = mid -1
			
		else:
			low = mid + 1

# input List (must be sorted)
my_list =[1,3,5,7,9,11,45]

# function call with arguments
# taking return from function storing in -
# result1, result2 variables
result1 = binary_search(my_list,11)
result2 = binary_search(my_list,-1)

# printing return(result1, result2) with f-string formating
print(f"Element 11 is at position: {result1}")
print(f"Element -1 is at position: {result2}")