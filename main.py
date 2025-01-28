"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import pytest
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1


def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	
	"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""

	if(left > right):
		return -1
	else:
		mid = ((right - left) // 2) + left
		if(mylist[mid] == key):
			return mid
		elif(key < mylist[mid]):
			return _binary_search(mylist, key, left, mid - 1)
		else:
			return _binary_search(mylist, key, mid + 1, right)

	### TODO
	"""
	linear search:
		best case: key is the first position in the list 0 -> O(1)
		worst case: Key is not in the list -> O(len(list))
	binary search:
		best case: Key is in the middle of the list -> O(1)
		worst case: Key is not in the list, which will have a run time of -> log(base 2)(length(list))
	
	
	
	
	"""

	###




def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `search_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	### TODO
	clock = 0
	a = time.time() 
	search_fn(mylist, key)
	b = time.time()
	clock = (b - a) * 1000
	return clock 



	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be 
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	### TODO

	array = []
	for size in (sizes):
		n = int(size)
		size = list(range(n))
		binary = time_search(binary_search, size, -1)
		linear = time_search(linear_search, size, -1)
		array.append((n, linear, binary))
	return(array)

	"""|        n |   linear |   binary |
|----------|----------|----------|
|       10 |    0.000 |    0.000 |
|      100 |    0.000 |    0.000 |
|     1000 |    0.000 |    0.000 |
|    10000 |    0.000 |    0.000 |
|   100000 |    2.520 |    0.000 |
|  1000000 |   26.525 |    0.000 |
| 10000000 |  273.368 |    0.000 |



9: Yes, because the search time for binary search is drastically lower than linear search, 
assuming the list is pre-sorted. 

10: 
	The worst case time complexity of searching a list containing n elements 
	linear-ly k times is -> O(n*k)

	For binary, the worst case complexity is the time sorting plus the regular complexity times k -> O(n^2) + O(log(base 2)(n * k).

	For virtually every value of k comparing the two complexities, it is requires less work 
	sorting the list for a binary search. 

	




"""





	###

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
	headers=['n', 'linear', 'binary'],
	floatfmt=".5f",
	tablefmt="github"))

print_results(compare_search())
