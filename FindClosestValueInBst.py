# Average: O(log(n)) time   O(1) space
# Worst: O(n) time   O(1) space

def findClosestValueInBst(tree, target):
	closest = float("inf")
	p = tree
	while p:
		if abs(target-closest) > abs(target-p.value):
			closest = p.value
		if target == p.value:
			return target
		elif target > p.value:
			p = p.right
		else:
			p = p.left
	return closest
