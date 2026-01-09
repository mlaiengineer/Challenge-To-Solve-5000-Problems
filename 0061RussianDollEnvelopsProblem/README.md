# Russian Doll Envelopes

## Problem
Given envelopes `[width, height]`, find the maximum number that can be nested.

## Optimized Approach
- Sort envelopes by width ↑ and height ↓
- Apply Longest Increasing Subsequence on heights using binary search

## Complexity
- Time: O(n log n)
- Space: O(n)

## Example
Input:

[[5,4],[6,4],[6,7],[2,3]]

Output:
 3
