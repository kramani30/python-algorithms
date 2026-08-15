"""
Best Time to Buy and Sell Stock
--------------------------------
Given an array where prices[i] is the price of a stock on day i,
return the maximum profit you can achieve by buying on one day
and selling on a later day. If no profit is possible, return 0.

Example:
    >>> max_profit([7, 1, 5, 3, 6, 4])
    5
    >>> max_profit([7, 6, 4, 3, 1])
    0
    >>> max_profit([2, 4, 1, 7])
    6

Time Complexity: O(n)
Space Complexity: O(1)
"""


def max_profit(prices: list) -> int:
    """Return the maximum profit from a single buy and sell transaction."""
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
    print(max_profit([7, 6, 4, 3, 1]))      # 0
    print(max_profit([2, 4, 1, 7]))         # 6
