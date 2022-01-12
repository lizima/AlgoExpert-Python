# O(n) time   O(d) space

def validateBst(tree):
    return validateBstHelper(tree,float("-inf"),float("inf"))

def validateBstHelper(tree,mi,ma):
	if not tree:
		return True
	if tree.value < mi or tree.value >= ma:
		return False
	lv = validateBstHelper(tree.left,mi,tree.value)
	if not lv:
		return False
	return validateBstHelper(tree.right,tree.value,ma)

# 或者中序遍历也ok