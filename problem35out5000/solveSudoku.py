class Solution(object):
    def solveSudoku(self, board):
        """
        Solves the Sudoku puzzle using optimized backtracking.
        Uses sets to track existing numbers in rows, columns, and boxes for O(1) validation.
        :type board: List[List[str]]
        :rtype: None (modifies the board in-place)
        """
        # Initialize data structures to track numbers in rows, columns, and boxes
        rows = [set() for _ in range(9)]      # Rows[i] holds numbers present in row i
        cols = [set() for _ in range(9)]      # Cols[j] holds numbers in column j
        boxes = [set() for _ in range(9)]     # Boxes[k] holds numbers in 3x3 box k
        empty_cells = []                      # List of coordinates of empty cells

        # Fill the tracking sets with the initial board state
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    empty_cells.append((i, j))
                else:
                    rows[i].add(cell)
                    cols[j].add(cell)
                    box_id = (i // 3) * 3 + (j // 3)
                    boxes[box_id].add(cell)

        def backtrack(index):
            """
            Recursive function to attempt to fill empty_cells one by one.
            Uses backtracking with early pruning via sets for efficient validation.
            """
            if index == len(empty_cells):
                return True  # Puzzle solved

            row, col = empty_cells[index]
            box_id = (row // 3) * 3 + (col // 3)

            for num in '123456789':
                # Only place the number if it's not already used in row, col, or box
                if num not in rows[row] and num not in cols[col] and num not in boxes[box_id]:
                    # Make a move
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box_id].add(num)

                    if backtrack(index + 1):
                        return True

                    # Undo move (backtrack)
                    board[row][col] = "."
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box_id].remove(num)

            return False  # Trigger backtracking

        backtrack(0)


# ------------------- TEST CASES -------------------
if __name__ == "__main__":
    def print_board(board):
        for row in board:
            print(" ".join(row))
        print()

    solver = Solution()

    # Test Case 1: Easy Puzzle
    board1 = [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "9", ".", ".", "1", ".", ".", "3", "."],
        [".", ".", "6", ".", "2", ".", "7", ".", "."],
        [".", ".", ".", "3", ".", "4", ".", ".", "."],
        ["2", "1", ".", ".", ".", ".", ".", "9", "8"],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "2", "5", ".", "6", "4", ".", "."],
        [".", "8", ".", ".", ".", ".", ".", "1", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]
    print("✅ Test Case 1:")
    print("Input:")
    print_board(board1)
    solver.solveSudoku(board1)
    print("Output:")
    print_board(board1)

    # Test Case 2: Medium Puzzle
    board2 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print("✅ Test Case 2:")
    print("Input:")
    print_board(board2)
    solver.solveSudoku(board2)
    print("Output:")
    print_board(board2)

    # Test Case 3: Already Solved
    board3 = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
    ]
    print("✅ Test Case 3:")
    print("Input:")
    print_board(board3)
    solver.solveSudoku(board3)
    print("Output (should be unchanged):")
    print_board(board3)

# -----------------------------------
# 🔍 Time Complexity:
# Worst-case: O(9^m), where m = number of empty cells (at most 81).
# Practical complexity is much lower due to early pruning using sets.

# 💾 Space Complexity:
# - O(1) extra space for board (in-place modification).
# - O(81) = 3x9 sets for rows, cols, boxes.
# - O(m) recursion stack, m = number of empty cells.
# -----------------------------------
