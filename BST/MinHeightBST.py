# time O(n)    space O(n) (end up with a BST with n nodes)

def minHeightBst(array):
	return minHeightBSTHelper(array,0,len(array)-1)

def minHeightBSTHelper(array,left,right):
	if left < right:
		return None
	mid = (left + right) // 2
	root = BST(array[mid])
	root.left = minHeightBSTHelper(array,left,mid-1)
	root.right = minHeightBSTHelper(array,mid+1,right)
	return root