# should consider general condition(the answer best resut condition)
# when the straight method doesn't work
# then enumerate every element (to be or not to be condition)
def max_profit(prices):
	if not prices:
		return 0
	
	profit = [0] * len(prices)
	for i in range(1, len(prices)):
		profit[i] = max(profit[i-1] + prices[i] - prices[i-1], 0)

	return max(profit)