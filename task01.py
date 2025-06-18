def find_coins_greedy(amount, denominations=[50, 25, 10, 5, 2, 1]):
    # Dictionary to store the result: coin -> number of times it's used
    result = {}

    # Sort the coin denominations from largest to smallest
    for coin in sorted(denominations, reverse=True):
        # If the current coin can be used (i.e., amount is big enough)
        if amount >= coin:
            # Determine how many of this coin we can use
            count = amount // coin

            # Save the count of this coin in the result
            result[coin] = count

            # Subtract the value of used coins from the remaining amount
            amount -= coin * count

    # Return the dictionary with the used coins
    return result

greed_al = find_coins_greedy(151)
print("\nGreedy algorithm:", greed_al)



def find_min_coins(amount, denominations=[50, 25, 10, 5, 2, 1]):
    # Initialize dp array: minimum number of coins to make each amount
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    # print(f"Initial dp: {dp}")

    # Initialize prev array to reconstruct solution path
    prev = [0] * (amount + 1)
    # print(f"Initial prev: {prev}")

    # Fill dp and prev arrays
    for i in range(1, amount + 1):
        for coin in denominations:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = coin
        # print(f"dp after amount {i}: {dp}")
        # print(f"prev after amount {i}: {prev}")

    # Backtrack to build result
    result = {}
    # print("\nBacktracking to find coins used:")
    while amount > 0:
        coin = prev[amount]
        # print(f"Amount: {amount}, using coin: {coin}")
        result[coin] = result.get(coin, 0) + 1
        amount -= coin
        # print(f"Updated result: {result}, remaining amount: {amount}")

    return result

change = find_min_coins(14, [1, 3, 4])
print("\nDynamic Algorithm:", change)
