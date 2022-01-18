# O(h) O(h) not optimal
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
	if isDescendant(nodeOne, nodeTwo):
		return isDescendant(nodeTwo, nodeThree)
	
	if isDescendant(nodeThree, nodeTwo):
		return isDescendant(nodeTwo, nodeOne)
	
	return False
def isDescendant(node, target):
	if not target:
		return False
	while node:
		if target.value < node.value:
			node = node.left
		elif target.value > node.value:
			node = node.right
		else:
			return True
	return False