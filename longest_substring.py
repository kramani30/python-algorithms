"""
Longest Substring Without Repeating Characters
-----------------------------------------------
Given a string, find the length of the longest substring
without repeating characters.

Example:
    >>> longest_substring("abcabcbb")
    3
    >>> longest_substring("bbbbb")
    1
    >>> longest_substring("pwwkew")
    3
    >>> longest_substring("")
    0

Time Complexity: O(n)
Space Complexity: O(n)
"""


def longest_substring(s: str) -> int:
    """Return the length of the longest substring without repeating characters."""
    substrings = []
    current = ""
    for char in s:
        if char not in current:
            current += char
        else:
            substrings.append(current)
            current = char
    substrings.append(current)
    return len(max(substrings, key=len)) if substrings else 0


if __name__ == "__main__":
    print(longest_substring("abcabcbb"))  # 3
    print(longest_substring("bbbbb"))     # 1
    print(longest_substring("pwwkew"))    # 3
    print(longest_substring(""))          # 0
