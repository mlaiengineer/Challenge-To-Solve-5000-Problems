from solution import Solution

sol = Solution()

test_cases = [
    # (input, expected_output, description)
    ("abacaba",  2, "Basic case - a:4, b:2, c:1 → 2 even"),
    ("zzacccz",  0, "No even frequencies at all"),
    ("aabb",     2, "All characters appear even times"),
    ("abcd",     0, "All characters appear once - no even"),
    ("aa",       1, "Single character repeated twice"),
    ("a",        0, "Single character appearing once"),
    ("aabbcc",   3, "All three chars appear twice"),
    ("aaabbbccc",0, "All chars appear odd times (3 each)"),
    ("abcabc",   3, "All chars appear exactly twice"),
    ("aabbccddeeffgghhiijj", 10, "10 chars each appearing twice"),
]

print(f"{'#':<5} {'Input':<25} {'Expected':<10} {'Got':<10} {'Status'}")
print("-" * 65)
for i, (s, expected, desc) in enumerate(test_cases, 1):
    result = sol.count(s)
    status = "✅ PASS" if result == expected else "❌ FAIL"
    print(f"{i:<5} {s:<25} {expected:<10} {result:<10} {status}")
    print(f"      → {desc}")
    print()