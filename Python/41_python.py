
# Created a dictionary called stocks

stocks = {
	#Ticker, #Stock Rates

	'GOOG': 520.54,
	'FB': 76.45,
	'YHOO': 39.28,
	'AMZN': 306.21,
	'AAPL': 99.76
}

# If we put stocks.keys() first and then stocks.values(), it would be sorted in alphabatical order
# This zip the dictionary in a list and in different tuples.
# zip(stocks.values(), stocks.keys())

print(min(zip(stocks.values(), stocks.keys()))
# Will print the minimum stock rate with its ticker.

print(min(zip(stocks.values(), stocks.keys()))
# Will print the maximum stock rate with its ticker.

print(sorted(zip(stocks.values(), stocks.keys()))
# Will print the stocks in ascending order according to the stocks rates.


#But if we put stocks.key() first then it will print stocks from A - Z according to the name of tickers
print(sorted(zip(stocks.keys()), stocks.values()))
