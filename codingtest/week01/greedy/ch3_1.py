n = 1260
count = 0

coins_types = [500, 100, 50, 10]

for coin in coins_types:
    count += n // coin
    n %= coin

print(count)