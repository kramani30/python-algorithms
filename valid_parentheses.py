"""
Valid Parentheses
-----------------
Given a string containing only '(', ')', '{', '}', '[', ']',
return True if the string is valid, False otherwise.

A string is valid if:
- Every opening bracket has a corresponding closing bracket
- Brackets are closed in the correct order

Example:
    >>> valid_parentheses("()")
    True
    >>> valid_parentheses("()[]{}")
    True
    >>> valid_parentheses("(]")
    False
    >>> valid_parentheses("([)]")
    False
    >>> valid_parentheses("{[]}")
    True

Time Complexity: O(n)
Space Complexity: O(n)
"""


def valid_parentheses(paren_str: str) -> bool:
    """Return True if all brackets are correctly matched and ordered."""
    paren_map = {")": "(", "}": "{", "]": "["}
    stack = []
    for char in paren_str:
        if char not in paren_map:
            stack.append(char)
        else:
            if stack and stack[-1] == paren_map[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    print(valid_parentheses("()"))      # True
    print(valid_parentheses("()[]{}"))  # True
    print(valid_parentheses("(]"))      # False
    print(valid_parentheses("([)]"))    # False
    print(valid_parentheses("{[]}"))    # True
