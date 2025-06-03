"""
🎯 Problem:
Given `n` friends sitting in a circle and counting out every `k`-th person for elimination,
return the winner (the last person remaining).

This version uses an **iterative mathematical approach** based on the **Josephus problem recurrence**.

🧠 Approach:
- We define f(i) as the winner's position in a group of size i.
- Recurrence relation: f(i) = (f(i - 1) + k) % i
- Start from f(1) = 0 (0-based indexing)
- Convert final answer to 1-based indexing by returning f(n) + 1

⏱️ Time Complexity: O(n)
💾 Space Complexity: O(1)
"""

def findTheWinner(n, k):
    """
    🔁 Iterative Josephus Solution
    :param n: Number of friends
    :param k: Count interval to eliminate a friend
    :return: The winner's position (1-based index)
    """
    saveWinner = 0  # f(1) = 0 (0-based)
    for i in range(2, n + 1):
        saveWinner = (saveWinner + k) % i
    return saveWinner + 1  # Convert to 1-based indexing

# ✅ Test Cases
print("🧪 Test Case 1: findTheWinner(5, 2) => Expected: 3")
print("Output:", findTheWinner(5, 2))  # ➤ 3

print("\n🧪 Test Case 2: findTheWinner(6, 5) => Expected: 1")
print("Output:", findTheWinner(6, 5))  # ➤ 1

print("\n🧪 Test Case 3: findTheWinner(10, 3) => Expected: 4")
print("Output:", findTheWinner(10, 3))  # ➤ 4
