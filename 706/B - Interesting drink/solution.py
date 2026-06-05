import sys
import bisect
 
n = int(sys.stdin.readline())
prices = list(map(int, sys.stdin.readline().split()))
prices.sort()
 
q = int(sys.stdin.readline())
coins = sys.stdin.read().split()
 
results = []
for coin_str in coins:
    coin = int(coin_str)
    affordable = bisect.bisect_right(prices, coin)
    results.append(str(affordable))
 
print('
'.join(results))