def binary_search(arr,value):
	# if array empty,or has 1 element or not value we are looking for
	if len(arr)==0 or (len (arr)=1 and arr[0]!=val:
		return False

   # middle value.
	mid=arr[len(arr)/2]	
	if val==mid:return True
	if val<mid: return binary_search(arr[:len(arr)/2],val)
	if val>mid: return binary_search(arr[len(arr)/2+1:],val)
