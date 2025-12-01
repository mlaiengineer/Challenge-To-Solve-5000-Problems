# 🗓️ Today’s Progress — 2025-12-1

Today I solved a FreeCodeCamp problem that requires converting a distance from **miles to kilometers**.  
The task includes rounding the result to **two decimal places**, and the input is always guaranteed to be a non-negative number.

---

## 🚀 Problem Summary

**Goal:**  
Convert a distance in miles to kilometers using the conversion rate:


Then round the output to **two decimal places**.

---

## 🔗 Problem Source  
FreeCodeCamp Problem: **Miles to Kilometers**  
https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-01


## 🧠 Approach

To solve this problem:

1. I used the conversion formula:  
   \[
   kilometers = miles \times 1.60934
   \]

2. After computing the conversion, I applied Python’s built-in `round()` function to format the result to two decimal places.

3. I organized the code using:
   - A clear constant for the conversion rate  
   - A professional docstring  
   - Clean variable naming for readability

This results in a concise and maintainable solution.

---

## ⏱️ Complexity Analysis

### **Time Complexity: O(1)**  
The function performs a constant number of arithmetic operations and rounding.

### **Space Complexity: O(1)**  
Only a few variables are used, and no additional data structures are created.

---

## 🧩 Final Code

```python
def convert_to_km(miles):
    """
    Convert miles to kilometers.

    Args:
        miles (float): Distance in miles (non-negative number).

    Returns:
        float: Distance converted to kilometers, rounded to two decimal places.

    Notes:
        1 mile = 1.60934 kilometers.
    """
    
    # Conversion factor from miles to kilometers
    KM_PER_MILE = 1.60934

    # Convert miles to kilometers
    kilometers = miles * KM_PER_MILE

    # Round the result to two decimal places
    return round(kilometers, 2)
