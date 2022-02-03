def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
    dp = [[0 for i in range(capacity+1)] for j in range(len(items)+1)]
	for i in range(1,len(dp)):
		v = items[i-1][0]
		w = items[i-1][1]
		for c in range(0,len(dp[0])):
			dp[i][c] = dp[i-1][c] if w > c else max(dp[i-1][c],dp[i-1][c-w]+v)
	return [dp[-1][-1],helper(dp,items)]

def helper(dp,items):
	sequence = []
	i = len(dp)-1 #4
	j = len(dp[0]) - 1 #10
	while i > 0 and j > 0:
		if dp[i][j] == dp[i-1][j]:
			i -= 1
		else:
			sequence.append(i-1)
			j -= items[i-1][1]
			i -= 1
	return list(reversed(sequence))