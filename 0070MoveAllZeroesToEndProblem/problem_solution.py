class Solution:
    def pushZerosToEnd(self, arr):
        # write_pos points to where the next non-zero element should go
        write_pos = 0

        for read_pos in range(len(arr)):
            # If current element is non-zero, move it forward
            if arr[read_pos] != 0:
                arr[read_pos], arr[write_pos] = arr[write_pos], arr[read_pos]
                write_pos += 1

        return arr
"""
Solve Move All Zeros to End using two-pointer in-place approach

- Implemented O(n) time, O(1) space solution
- Preserved relative order of non-zero elements
- Used write-index pointer strategy

"""