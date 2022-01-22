# time O(n)  space O(log(n))

def maxPathSum(tree):
    # Write your code here.
    return findMaxSum(tree).maxNotPathroot

def findMaxSum(tree):
	if not tree:
		return TreeInfo(float("-inf"),float("-inf"))
	if not tree.left and not tree.right:
		return TreeInfo(tree.value,tree.value)
	
# 	if not tree.left:
# 		rightInfo = findMaxSum(tree.right)
# 		thismaxPathRoot = rightInfo.maxPathRoot+tree.value
# 		return TreeInfo(thismaxPathRoot,max(thismaxPathRoot,rightInfo.maxNotPathroot))
	
# 	if not tree.right:
# 		leftInfo = findMaxSum(tree.left)
# 		thismaxPathRoot = leftInfo.maxPathRoot+tree.value
# 		return TreeInfo(thismaxPathRoot,max(thismaxPathRoot,leftInfo.maxNotPathroot))
	
	leftInfo = findMaxSum(tree.left)
	rightInfo = findMaxSum(tree.right)
	
	thismaxPathRoot = max(leftInfo.maxPathRoot,rightInfo.maxPathRoot) + tree.value
	thismaxNotPathRoot = max(leftInfo.maxNotPathroot, rightInfo.maxNotPathroot,leftInfo.maxPathRoot+rightInfo.maxPathRoot+tree.value, thismaxPathRoot)
	return TreeInfo(thismaxPathRoot,thismaxNotPathRoot)

class TreeInfo:
	def __init__(self,maxPathRoot,maxNotPathroot):
		# not means, not sure, but not exactly not
		self.maxPathRoot = maxPathRoot
		self.maxNotPathroot = maxNotPathroot