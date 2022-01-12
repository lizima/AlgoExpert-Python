# O(n) O(n) 很简单，只需要中序遍历
# 但有一个time O(h+k), space O(h)的方法

class TreeInfo:
	def __init__(self, alreadyvisitednumber, justvisited):
		self.alreadyvisitednumber = alreadyvisitednumber
		self.justvisited = justvisited

def findKthLargestValueInBst(tree, k):
	treeinfo = TreeInfo(0,-1)
	helper(tree,k,treeinfo)
	return treeinfo.justvisited

def helper(tree,k,treeinfo):
	if treeinfo.alreadyvisitednumber == k or not tree:
		return
	helper(tree.right,k,treeinfo)
	if treeinfo.alreadyvisitednumber < k:
		treeinfo.alreadyvisitednumber += 1
		treeinfo.justvisited = tree.value
		helper(tree.left,k,treeinfo)