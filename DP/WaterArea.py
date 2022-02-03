#Solution 1    O(n), O(n)

def waterArea(heights):
    maxes = [0 for x in heights]
	leftMax = 0
	for i in range(len(heights)):
		height = heights[i]
		maxes[i] = leftMax
		leftMax = max(leftMax,height)
	rightMax = 0
	for i in reversed(range(len(heights))):
		height = heights[i]
		minHeight = min(rightMax,maxes[i])
		if height < minHeight:
			maxes[i] = minHeight - height
		else:
			maxes[i] = 0
		rightMax = max(rightMax, height)
	return sum(maxes)


#Solution 2   O(n), O(1)

def waterArea(heights):
    if len(heights) == 0:
		return 0
	leftIdx = 0
	rightIdx = len(heights)-1
	leftMax = heights[leftIdx]
	rightMax = heights[rightIdx]
	surfaceArea = 0
	while leftIdx < rightIdx:
		if heights[leftIdx] < heights[rightIdx]:
			leftIdx += 1
			leftMax = max(leftMax, heights[leftIdx])
			surfaceArea += leftMax - heights[leftIdx]
		else:
			rightIdx -= 1
			rightMax = max(rightMax, heights[rightIdx])
			surfaceArea += rightMax - heights[rightIdx]
	return surfaceArea