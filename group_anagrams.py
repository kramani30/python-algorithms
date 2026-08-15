"""
Group Anagrams
--------------
Given a list of strings, group the anagrams together.
An anagram is a word that contains the same characters
as another word, just in a different order.

Example:
    >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    >>> group_anagrams([""])
    [['']]
    >>> group_anagrams(["a"])
    [['a']]

Time Complexity: O(n * k log k) where k is the max string length
Space Complexity: O(n)
"""


def group_anagrams(str_list: list) -> list:
    """Group strings that are anagrams of each other."""
    ana_dict = {}
    for word in str_list:
        key = tuple(sorted(word))
        if key not in ana_dict:
            ana_dict[key] = [word]
        else:
            ana_dict[key].append(word)
    return list(ana_dict.values())


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(group_anagrams([""]))
    print(group_anagrams(["a"]))
