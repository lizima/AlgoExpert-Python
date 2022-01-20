# # O(n), O(n)  (O(n^2),O(n)的方法很好想)

class Treeinfo:
	def __init__(self,currentIdx):
		self.currentIdx = currentIdx

def reconstructBst(preOrderTraversalValues):
	treeinfo = Treeinfo(0)
	return helper(preOrderTraversalValues,float("-inf"),float("inf"),treeinfo)

def helper(preOrderTraversalValues,mi,ma,treeinfo):
	if treeinfo.currentIdx == len(preOrderTraversalValues):
		return None

	currentNodeValue = preOrderTraversalValues[treeinfo.currentIdx]
	if currentNodeValue < mi or currentNodeValue >= ma:
		return None

	treeinfo.currentIdx += 1
	leftTree = helper(preOrderTraversalValues,mi,currentNodeValue,treeinfo)
	rightTree = helper(preOrderTraversalValues,currentNodeValue,ma,treeinfo)

	return BST(currentNodeValue,leftTree,rightTree)