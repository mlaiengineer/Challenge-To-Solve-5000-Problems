"""
Test Suite for LeetCode 139: Word Break
Contains 20+ comprehensive test cases covering various scenarios
"""

import unittest
from tabulation_solution import Solution


class TestWordBreak(unittest.TestCase):
    """
    Comprehensive test suite for the Word Break problem.
    Tests edge cases, basic cases, and complex scenarios.
    """

    def setUp(self):
        """Initialize the Solution object before each test"""
        self.solution = Solution()

    # ========== LEETCODE EXAMPLE TEST CASES ==========

    def test_example_1_basic_segmentation(self):
        """Test Case 1: Basic segmentation - 'leetcode' = 'leet' + 'code'"""
        s = "leetcode"
        wordDict = ["leet", "code"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_example_2_word_reuse(self):
        """Test Case 2: Word reuse allowed - 'apple' appears twice"""
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_example_3_impossible_segmentation(self):
        """Test Case 3: Impossible to segment - missing 'og' to complete 'dog'"""
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        self.assertFalse(self.solution.wordBreak(s, wordDict))

    # ========== EDGE CASES ==========

    def test_single_character_match(self):
        """Test Case 4: Single character string that matches"""
        s = "a"
        wordDict = ["a"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_single_character_no_match(self):
        """Test Case 5: Single character string with no match"""
        s = "a"
        wordDict = ["b"]
        self.assertFalse(self.solution.wordBreak(s, wordDict))

    def test_exact_match_entire_string(self):
        """Test Case 6: Entire string is one word in dictionary"""
        s = "programming"
        wordDict = ["programming"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_empty_segmentation_impossible(self):
        """Test Case 7: String cannot be segmented at all"""
        s = "aaaaaaa"
        wordDict = ["aaaa", "aa"]
        self.assertFalse(self.solution.wordBreak(s, wordDict))

    # ========== MULTIPLE WORDS SEGMENTATION ==========

    def test_three_word_segmentation(self):
        """Test Case 8: String segments into three words"""
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_four_word_segmentation(self):
        """Test Case 9: String segments into four words"""
        s = "pineapplepenapple"
        wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_many_small_words(self):
        """Test Case 10: Many single character words"""
        s = "abcd"
        wordDict = ["a", "b", "c", "d"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    # ========== WORD REUSE SCENARIOS ==========

    def test_same_word_repeated_multiple_times(self):
        """Test Case 11: Same word used multiple times"""
        s = "aaaaaaa"
        wordDict = ["aaaa", "aaa"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_alternating_pattern(self):
        """Test Case 12: Alternating word pattern"""
        s = "abababab"
        wordDict = ["ab", "ba"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    # ========== OVERLAPPING POSSIBILITIES ==========

    def test_overlapping_words_valid(self):
        """Test Case 13: Multiple valid segmentation paths exist"""
        s = "cars"
        wordDict = ["car", "ca", "rs"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_prefix_confusion(self):
        """Test Case 14: Dictionary contains word prefixes that could mislead"""
        s = "goalspecial"
        wordDict = ["go", "goal", "goals", "special"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    # ========== FALSE CASES ==========

    def test_almost_complete_segmentation(self):
        """Test Case 15: Almost complete but fails at the end"""
        s = "aaaaaab"
        wordDict = ["a", "aa", "aaa", "aaaa"]
        self.assertFalse(self.solution.wordBreak(s, wordDict))

    def test_missing_middle_word(self):
        """Test Case 16: Missing word in the middle prevents segmentation"""
        s = "abcdef"
        wordDict = ["ab", "ef"]
        self.assertFalse(self.solution.wordBreak(s, wordDict))

    def test_substring_not_word(self):
        """Test Case 17: Substrings exist but not as complete words"""
        s = "basketball"
        wordDict = ["basket", "ball", "et"]
        self.assertFalse(self.solution.wordBreak(s, wordDict))

    # ========== COMPLEX SCENARIOS ==========

    def test_long_string_valid(self):
        """Test Case 18: Longer string with valid segmentation"""
        s = "ilikesamsung"
        wordDict = ["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_long_string_invalid(self):
        """Test Case 19: Longer string with invalid segmentation"""
        s = "ilikesamsung"
        wordDict = ["i", "like", "sam", "sun"]
        self.assertFalse(self.solution.wordBreak(s, wordDict))

    def test_repeated_pattern_valid(self):
        """Test Case 20: Repeated pattern that can be segmented"""
        s = "dogdogdog"
        wordDict = ["dog"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    # ========== ADDITIONAL EDGE CASES ==========

    def test_single_letter_repeated(self):
        """Test Case 21: Single letter repeated many times"""
        s = "aaaaaa"
        wordDict = ["a", "aa"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_all_words_same_length(self):
        """Test Case 22: All dictionary words have same length"""
        s = "abcdefgh"
        wordDict = ["ab", "cd", "ef", "gh"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_greedy_would_fail(self):
        """Test Case 23: Greedy approach would fail, DP should succeed"""
        s = "aaab"
        wordDict = ["a", "aa", "aaa", "aaab"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_large_dictionary_no_match(self):
        """Test Case 24: Large dictionary but no valid segmentation"""
        s = "xyz"
        wordDict = ["a", "b", "c", "ab", "bc", "abc", "x", "y", "z", "xy"]
        self.assertFalse(self.solution.wordBreak(s, wordDict))

    def test_dictionary_with_duplicates_concept(self):
        """Test Case 25: Testing with various word combinations"""
        s = "catskicatcats"
        wordDict = ["cats", "cat", "ski"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))


def run_tests_with_details():
    """
    Run all tests and display detailed results.
    """
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWordBreak)

    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Print summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Total Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 70)

    return result


if __name__ == "__main__":
    # Run tests with detailed output
    run_tests_with_details()