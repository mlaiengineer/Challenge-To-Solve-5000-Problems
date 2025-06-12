# 🚀 Unique Permutations Generator using Backtracking
# 📌 Description:
# This script generates all unique permutations of a list of integers using backtracking and hashing to avoid duplicates.
# 🎯 Time Complexity: O(n * n!)
# 🔍 Space Complexity: O(n) for recursion stack

class Solution(object):
    def permuteUnique(self, nums):
        """
        Generate all unique permutations of the given list.

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []  # ✅ Stores all unique permutations

        def backtrack(index):
            # 📌 Base Case: If index reaches the end, record the current permutation
            if index == len(nums):
                result.append(nums[:])  # 📋 Make a deep copy of the current state
                return

            used = {}  # 🔍 Hash table to track duplicates at the current recursion level

            for j in range(index, len(nums)):
                if nums[j] in used:
                    continue  # ❌ Skip duplicates

                used[nums[j]] = True  # ✅ Mark this element as used at this level

                # 🔄 Swap current element with the index element
                nums[index], nums[j] = nums[j], nums[index]

                # 🔁 Recurse to the next index
                backtrack(index + 1)

                # ⏪ Backtrack to restore the original array
                nums[index], nums[j] = nums[j], nums[index]

        #nums.sort()  # 🔢 Optional: Sorting helps make deduplication more efficient
        backtrack(0)
        return result


# 🧪 Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    input1 = [1, 1, 2]
    print("🧪 Test Case 1: Input:", input1)
    print("✅ Output:", sol.permuteUnique(input1))
    print("------------------------------------------------")

    # Test Case 2
    input2 = [1, 2, 3]
    print("🧪 Test Case 2: Input:", input2)
    print("✅ Output:", sol.permuteUnique(input2))
    print("------------------------------------------------")

    # Test Case 3
    input3 = [2, 2, 1, 1]
    print("🧪 Test Case 3: Input:", input3)
    print("✅ Output:", sol.permuteUnique(input3))
    print("------------------------------------------------")
