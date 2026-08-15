"""
Unit tests for all algorithm solutions.
Run with: pytest tests/
"""

import pytest
from two_sum import two_sum
from valid_parentheses import valid_parentheses
from group_anagrams import group_anagrams
from longest_substring import longest_substring
from best_time_to_buy_sell_stock import max_profit
from climbing_stairs import climbing_stairs


# ─── Two Sum ───────────────────────────────────────────────────────────────

class TestTwoSum:
    def test_basic(self):
        assert two_sum([2, 7, 11, 15], 9) == [1, 0]

    def test_middle_elements(self):
        assert two_sum([3, 2, 4], 6) == [2, 1]

    def test_duplicates(self):
        assert two_sum([3, 3], 6) == [1, 0]

    def test_no_solution(self):
        assert two_sum([1, 2, 3], 10) == []


# ─── Valid Parentheses ──────────────────────────────────────────────────────

class TestValidParentheses:
    def test_simple_valid(self):
        assert valid_parentheses("()") == True

    def test_multiple_valid(self):
        assert valid_parentheses("()[]{}") == True

    def test_nested_valid(self):
        assert valid_parentheses("{[]}") == True

    def test_mismatched(self):
        assert valid_parentheses("(]") == False

    def test_wrong_order(self):
        assert valid_parentheses("([)]") == False

    def test_empty_string(self):
        assert valid_parentheses("") == True

    def test_unclosed(self):
        assert valid_parentheses("(") == False


# ─── Group Anagrams ─────────────────────────────────────────────────────────

class TestGroupAnagrams:
    def test_basic(self):
        result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        assert sorted([sorted(g) for g in result]) == sorted([
            sorted(["eat", "tea", "ate"]),
            sorted(["tan", "nat"]),
            sorted(["bat"])
        ])

    def test_empty_string(self):
        assert group_anagrams([""]) == [[""]]

    def test_single_char(self):
        assert group_anagrams(["a"]) == [["a"]]

    def test_no_anagrams(self):
        result = group_anagrams(["abc", "def", "ghi"])
        assert len(result) == 3


# ─── Longest Substring ──────────────────────────────────────────────────────

class TestLongestSubstring:
    def test_basic(self):
        assert longest_substring("abcabcbb") == 3

    def test_all_same(self):
        assert longest_substring("bbbbb") == 1

    def test_mixed(self):
        assert longest_substring("pwwkew") == 3

    def test_empty(self):
        assert longest_substring("") == 0

    def test_single_char(self):
        assert longest_substring("a") == 1

    def test_no_repeats(self):
        assert longest_substring("abcdef") == 6


# ─── Best Time to Buy and Sell Stock ────────────────────────────────────────

class TestMaxProfit:
    def test_basic(self):
        assert max_profit([7, 1, 5, 3, 6, 4]) == 5

    def test_no_profit(self):
        assert max_profit([7, 6, 4, 3, 1]) == 0

    def test_buy_low_sell_high(self):
        assert max_profit([2, 4, 1, 7]) == 6

    def test_single_price(self):
        assert max_profit([5]) == 0

    def test_two_prices_profit(self):
        assert max_profit([1, 5]) == 4

    def test_two_prices_loss(self):
        assert max_profit([5, 1]) == 0


# ─── Climbing Stairs ────────────────────────────────────────────────────────

class TestClimbingStairs:
    def test_one_step(self):
        assert climbing_stairs(1) == 1

    def test_two_steps(self):
        assert climbing_stairs(2) == 2

    def test_three_steps(self):
        assert climbing_stairs(3) == 3

    def test_four_steps(self):
        assert climbing_stairs(4) == 5

    def test_five_steps(self):
        assert climbing_stairs(5) == 8

    def test_ten_steps(self):
        assert climbing_stairs(10) == 89
