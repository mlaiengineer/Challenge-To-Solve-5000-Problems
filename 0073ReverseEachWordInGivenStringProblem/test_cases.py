import unittest
from problem_solution import Solution


class TestReverseEachWord(unittest.TestCase):
    """Comprehensive test suite for the Reverse Each Word problem."""

    def setUp(self):
        """Initialize Solution before each test"""
        self.solution = Solution()

    # ========== GEEKSFORGEEKS EXAMPLE TEST CASES ==========

    def test_example_1_multiple_words_with_spaces(self):
        """Leading and trailing spaces with multiple words"""
        self.assertEqual(self.solution.reverseWords(" i like this program very much "), "i ekil siht margorp yrev hcum")

    def test_example_2_two_words_with_spaces(self):
        """Leading and trailing spaces with two words"""
        self.assertEqual(self.solution.reverseWords(" pqr mno "), "rqp onm")

    def test_example_3_single_word(self):
        """Single word with no spaces"""
        self.assertEqual(self.solution.reverseWords("pqr"), "rqp")

    # ========== EDGE CASES ==========

    def test_single_character_word(self):
        """Single character word should remain unchanged"""
        self.assertEqual(self.solution.reverseWords("a"), "a")

    def test_single_character_multiple_words(self):
        """Multiple single character words should remain unchanged"""
        self.assertEqual(self.solution.reverseWords("a b c"), "a b c")

    def test_leading_and_trailing_spaces(self):
        """Extra leading and trailing spaces should be removed"""
        self.assertEqual(self.solution.reverseWords("  hello  world  "), "olleh dlrow")

    # ========== WORD REVERSAL SCENARIOS ==========

    def test_palindrome_word(self):
        """Palindrome words should remain the same after reversing"""
        self.assertEqual(self.solution.reverseWords("madam racecar level"), "madam racecar level")

    def test_all_same_characters(self):
        """Words with all same characters should remain unchanged"""
        self.assertEqual(self.solution.reverseWords("aaa bbb ccc"), "aaa bbb ccc")

    def test_two_character_words(self):
        """Two character words should be swapped"""
        self.assertEqual(self.solution.reverseWords("ab cd ef"), "ba dc fe")

    # ========== COMPLEX SCENARIOS ==========

    def test_long_single_word(self):
        """Long single word should be fully reversed"""
        self.assertEqual(self.solution.reverseWords("abcdefghij"), "jihgfedcba")


# ========== TEST RUNNER ==========

def run_tests_with_summary():
    """Run all tests and display a clean summary"""

    suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseEachWord)
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