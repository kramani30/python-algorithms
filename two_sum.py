"""
Two Sum
-------
Given a list of integers and a target sum, return the indices
of the two numbers that add up to the target.

Example:
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
    >>> two_sum([3, 2, 4], 6)
    [1, 2]

Time Complexity: O(n)
Space Complexity: O(n)
"""


def two_sum(nums: list, target: int) -> list:
    """Return indices of two numbers that add up to target."""
    comp_dict = {}
    for index, num in enumerate(nums):
        comp = target - num
        if comp not in comp_dict:
            comp_dict[num] = index
        else:
            return [index, comp_dict[comp]]
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([3, 2, 4], 6))         # [1, 2]
    print(two_sum([3, 3], 6))            # [1, 0]
