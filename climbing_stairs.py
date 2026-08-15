"""
Climbing Stairs
---------------
You are climbing a staircase with n steps. Each time you can
either climb 1 or 2 steps. Return the number of distinct ways
you can climb to the top.

This follows the Fibonacci sequence:
- ways(1) = 1
- ways(2) = 2
- ways(n) = ways(n-1) + ways(n-2)

Example:
    >>> climbing_stairs(1)
    1
    >>> climbing_stairs(2)
    2
    >>> climbing_stairs(3)
    3
    >>> climbing_stairs(4)
    5
    >>> climbing_stairs(5)
    8

Time Complexity: O(n)
Space Complexity: O(1)
"""


def climbing_stairs(n: int) -> int:
    """Return the number of distinct ways to climb n stairs."""
    if n <= 2:
        return n
    prev2 = 1
    prev1 = 2
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1


if __name__ == "__main__":
    print(climbing_stairs(1))  # 1
    print(climbing_stairs(2))  # 2
    print(climbing_stairs(3))  # 3
    print(climbing_stairs(4))  # 5
    print(climbing_stairs(5))  # 8
