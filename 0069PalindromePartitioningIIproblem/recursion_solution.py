class RecursionSolution(object):
    def minCut(self, s):
        """
        Returns the minimum number of cuts needed to partition the string
        such that every substring is a palindrome.
        """
        n = len(s)

        def is_palindrome(left, right):
            """
            Checks whether the substring s[left:right+1] is a palindrome.
            """
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def min_cuts(start, end):
            """
            Recursively computes the minimum cuts needed for substring s[start:end+1].
            """

            # Base case:
            # If the substring is already a palindrome or has only one character
            if start == end or is_palindrome(start, end):
                return 0

            # Worst case: cut before every character
            min_cut_count = end - start

            # Try all possible cut positions
            for cut in range(start, end):
                if is_palindrome(start, cut):
                    min_cut_count = min(
                        min_cut_count,
                        1 + min_cuts(cut + 1, end)
                    )

            return min_cut_count

        return min_cuts(0, n - 1)
