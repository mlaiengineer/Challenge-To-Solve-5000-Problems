class Solution:
    def towerOfHanoi(self, n, fromm, to, aux):
        """
        Calculate the total number of moves required to solve the Tower of Hanoi puzzle.

        Parameters:
        n (int): Number of disks.
        fromm (str): The source rod.
        to (str): The target rod.
        aux (str): The auxiliary rod.

        Returns:
        int: Total number of moves to transfer all disks from source to target.
        """
        if n == 0:
            return 0  # No disks to move
        if n == 1:
            return 1  # Base case: only one move needed
        else:
            # Recursive steps:
            # 1. Move n-1 disks from source to auxiliary
            move1 = self.towerOfHanoi(n-1, fromm, aux, to)

            # 2. Move the nth disk from source to target
            move2 = 1

            # 3. Move n-1 disks from auxiliary to target
            move3 = self.towerOfHanoi(n-1, aux, to, fromm)

            # Total moves is sum of all 3 steps
            return move1 + move2 + move3


# 🔍 Test the function with multiple test cases
objSolution = Solution()

# Test case 1: 0 disks
print("Test case n=0: Total moves =", objSolution.towerOfHanoi(0, 'A', 'C', 'B'))  # Expected: 0

# Test case 2: 1 disk
print("Test case n=1: Total moves =", objSolution.towerOfHanoi(1, 'A', 'C', 'B'))  # Expected: 1

# Test case 3: 3 disks
print("Test case n=3: Total moves =", objSolution.towerOfHanoi(3, 'A', 'C', 'B'))  # Expected: 7

# Test case 4: 4 disks
print("Test case n=4: Total moves =", objSolution.towerOfHanoi(4, 'A', 'C', 'B'))  # Expected: 15
