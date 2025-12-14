# 📝 Title Case a String

## 📌 Problem Description

Given a string `title`, return a new string formatted in **title case** using the following rules:

- Capitalize the **first letter** of each word.
- Convert all **other letters** in each word to lowercase.
- Words are always separated by a **single space**.

### Example

Input: "the quick brown fox"
Output: "The Quick Brown Fox"


---

## 🔗 Problem Source

FreeCodeCamp — Daily Coding Challenge  
https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-14

---

## 🚀 Approach Used

To solve this problem, I used a **manual string manipulation approach** instead of relying on Python’s built-in `title()` method.

### Steps:
1. Split the input string into individual words using `split()`.
2. For each word:
   - Capitalize the first character using `upper()`.
   - Convert the remaining characters to lowercase using `lower()`.
3. Store the formatted words in a list.
4. Join the words back into a single string using spaces.

This approach makes the logic explicit, readable, and suitable for learning purposes.

---

## 🧠 Why This Approach?

- Avoids hidden behavior of built-in methods.
- Clearly demonstrates string indexing and manipulation.
- Easy to debug and understand.
- Follows the exact rules defined in the problem.

---

## ⏱️ Complexity Analysis

### **Time Complexity: O(n)**  
Where `n` is the total number of characters in the string.  
Each character is processed once.

### **Space Complexity: O(n)**  
A new list of formatted words and a new string are created.

---

## 🧩 Final Code

```python
def title_case(title):
    words = title.split()
    formatted_words = []

    for word in words:
        formatted_words.append(word[0].upper() + word[1:].lower())

    return " ".join(formatted_words)

