"""
Test Suite for LeetCode 139: Word Break
Tests Recursion, Memoization, and Tabulation (Bottom-Up DP) solutions separately.
Contains 15 optimized test cases covering all key scenarios.
"""

import unittest
from recursion_solution import Solution as RecursionSolution
from tabulation_solution import Solution as TabulationSolution
from memoization_solution import Solution as MemoizationSolution


class BaseTestWordBreak:
    """
    Base test class containing all test cases.
    Shared between RecursionSolution, MemoizationSolution, and TabulationSolution test classes.
    """

    # ========== LEETCODE EXAMPLE TEST CASES ==========

    def test_example_1_basic_segmentation(self):
        """'leetcode' segments into 'leet' + 'code'"""
        self.assertTrue(self.solution.wordBreak("leetcode", ["leet", "code"]))

    def test_example_2_word_reuse(self):
        """'applepenapple' segments using 'apple' twice"""
        self.assertTrue(self.solution.wordBreak("applepenapple", ["apple", "pen"]))

    def test_example_3_impossible_segmentation(self):
        """'catsandog' cannot be fully segmented"""
        self.assertFalse(self.solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    # ========== EDGE CASES ==========

    def test_single_character_match(self):
        """Single character string that exists in dictionary"""
        self.assertTrue(self.solution.wordBreak("a", ["a"]))

    def test_single_character_no_match(self):
        """Single character string that does NOT exist in dictionary"""
        self.assertFalse(self.solution.wordBreak("a", ["b"]))

    def test_entire_string_is_one_word(self):
        """Entire string exists as a single word in dictionary"""
        self.assertTrue(self.solution.wordBreak("programming", ["programming"]))

    # ========== WORD REUSE SCENARIOS ==========

    def test_same_word_repeated(self):
        """Same word reused multiple times to segment string"""
        self.assertTrue(self.solution.wordBreak("dogdogdog", ["dog"]))

    def test_repeated_pattern(self):
        """Alternating words form the full string"""
        self.assertTrue(self.solution.wordBreak("abababab", ["ab", "ba"]))

    # ========== OVERLAPPING / TRICKY CASES ==========

    def test_greedy_would_fail(self):
        """Greedy approach fails here but correct solution should pass"""
        self.assertTrue(self.solution.wordBreak("aaab", ["a", "aa", "aaa", "aaab"]))

    def test_prefix_confusion(self):
        """Dictionary has prefixes that could mislead — must pick correct word"""
        self.assertTrue(self.solution.wordBreak("goalspecial", ["go", "goal", "goals", "special"]))

    def test_overlapping_words_valid(self):
        """Multiple valid segmentation paths exist"""
        self.assertTrue(self.solution.wordBreak("cars", ["car", "ca", "rs"]))

    # ========== FALSE CASES ==========

    def test_almost_complete_segmentation(self):
        """String almost segments but last character has no match"""
        self.assertFalse(self.solution.wordBreak("aaaaaab", ["a", "aa", "aaa", "aaaa"]))

    def test_missing_middle_word(self):
        """Start and end match but middle part has no match"""
        self.assertFalse(self.solution.wordBreak("abcdef", ["ab", "ef"]))

    # ========== COMPLEX SCENARIOS ==========

    def test_long_string_valid(self):
        """Longer string with valid segmentation using multiple words"""
        self.assertTrue(self.solution.wordBreak("ilikesamsung", ["i", "like", "sam", "sung", "samsung"]))

    def test_long_string_invalid(self):
        """Longer string where segmentation is impossible"""
        self.assertFalse(self.solution.wordBreak("ilikesamsung", ["i", "like", "sam", "sun"]))


# ========== RECURSION SOLUTION TESTS ==========

class TestRecursionSolution(BaseTestWordBreak, unittest.TestCase):
    """Runs all test cases against the Recursion Solution"""

    def setUp(self):
        """Initialize RecursionSolution before each test"""
        self.solution = RecursionSolution()


# ========== MEMOIZATION SOLUTION TESTS ==========

class TestMemoizationSolution(BaseTestWordBreak, unittest.TestCase):
    """Runs all test cases against the Memoization (Top-Down DP) Solution"""

    def setUp(self):
        """Initialize MemoizationSolution before each test"""
        self.solution = MemoizationSolution()


# ========== TABULATION SOLUTION TESTS ==========

class TestTabulationSolution(BaseTestWordBreak, unittest.TestCase):
    """Runs all test cases against the Tabulation (Bottom-Up DP) Solution"""

    def setUp(self):
        """Initialize TabulationSolution before each test"""
        self.solution = TabulationSolution()


# ========== TEST RUNNER ==========

def run_tests_with_summary():
    """Run all tests and display a clean summary"""

    suite = unittest.TestLoader().loadTestsFromTestCase(TestRecursionSolution)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMemoizationSolution))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestTabulationSolution))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Total Tests Run  : {result.testsRun}")
    print(f"Successes        : {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures         : {len(result.failures)}")
    print(f"Errors           : {len(result.errors)}")
    print("=" * 70)

    return result


if __name__ == "__main__":
    run_tests_with_summary()