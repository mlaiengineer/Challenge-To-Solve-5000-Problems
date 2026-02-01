from problem_solution import Solution


def test_push_zeros_to_end():
    sol = Solution()

    # 1️⃣ example case
    assert sol.pushZerosToEnd([1, 2, 0, 4, 3, 0, 5, 0]) == [1, 2, 4, 3, 5, 0, 0, 0]

    # 2️⃣ no zeros
    assert sol.pushZerosToEnd([1, 2, 3]) == [1, 2, 3]

    # 3️⃣ all zeros
    assert sol.pushZerosToEnd([0, 0, 0]) == [0, 0, 0]

    # 4️⃣ zeros at start
    assert sol.pushZerosToEnd([0, 0, 1, 2]) == [1, 2, 0, 0]

    # 5️⃣ zeros at end already
    assert sol.pushZerosToEnd([1, 2, 3, 0, 0]) == [1, 2, 3, 0, 0]

    # 6️⃣ single zero
    assert sol.pushZerosToEnd([0]) == [0]

    # 7️⃣ single non-zero
    assert sol.pushZerosToEnd([7]) == [7]

    # 8️⃣ alternating zeros
    assert sol.pushZerosToEnd([0, 1, 0, 2, 0, 3]) == [1, 2, 3, 0, 0, 0]

    # 9️⃣ large values with zeros
    assert sol.pushZerosToEnd([100, 0, 200, 0, 300]) == [100, 200, 300, 0, 0]

    # 🔟 empty array
    assert sol.pushZerosToEnd([]) == []

    print("✅ All 10 test cases passed!")


if __name__ == "__main__":
    test_push_zeros_to_end()
