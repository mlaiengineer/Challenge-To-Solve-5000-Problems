"""
🎯 Problem:
Given `n` friends sitting in a circle and counting out every `k`-th person for elimination,
return the winner (last person remaining).

This is a classic recursive version of the Josephus problem.

🧠 Approach:
- Represent people in a list from 1 to n.
- Use recursion to eliminate the (startIndex + k - 1) % len(list) person at each step.
- Continue until one person remains.
"""

def find_the_winner(n, k):
    # Initialize the list of friends from 1 to n
    tempArr = [i + 1 for i in range(n)]
    
    def helper_function(tempArr, startIndex):
        # 🛑 Base case: only one person left
        if len(tempArr) == 1:
            return tempArr[0]
        
        # 🔁 Recursive case: remove the k-th person
        indexToRemove = (startIndex + k - 1) % len(tempArr)
        del tempArr[indexToRemove]
        
        # Continue from the person after the one removed
        return helper_function(tempArr, indexToRemove)
    
    return helper_function(tempArr, 0)

# ✅ Test Cases
print("🧪 Test Case 1: find_the_winner(5, 2) => Expected: 3")
print("Output:", find_the_winner(5, 2))  # ➤ 3

print("\n🧪 Test Case 2: find_the_winner(6, 5) => Expected: 1")
print("Output:", find_the_winner(6, 5))  # ➤ 1

print("\n🧪 Test Case 3: find_the_winner(10, 3) => Expected: 4")
print("Output:", find_the_winner(10, 3))  # ➤ 4
