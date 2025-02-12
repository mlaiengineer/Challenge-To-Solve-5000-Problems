/**
 * @title Probability Calculation for Dice Sum ≤ 9
 * @description This script calculates the probability of rolling two 6-sided dice
 *              and getting a sum of 9 or less. It simplifies the fraction using GCD.
 * @author asshaieas
 * @version 1.0
 */

function processData(input) {
    /**
     * Helper function to compute the Greatest Common Divisor (GCD)
     * using the Euclidean algorithm.
     * 
     * @param {number} a - First number
     * @param {number} b - Second number
     * @returns {number} - The greatest common divisor of a and b
     */
    function hcf(a, b) {
        while (b) {
            [a, b] = [b, a % b]; // Swap values and compute remainder
        }
        return a;
    }

    let count = 0;  // Counter for valid outcomes where sum ≤ 9
    let total = 36; // Total possible outcomes (6-sided die * 6-sided die)

    // Iterate over all possible outcomes of rolling two dice
    for (let i = 1; i <= 6; i++) {
        for (let j = 1; j <= 6; j++) {
            if (i + j <= 9) count++; // Count valid pairs
        }
    }

    let gcd = hcf(count, total); // Compute GCD to simplify probability

    // Output the probability in its simplest fraction form
    console.log(`${count / gcd}/${total / gcd}`);

    // Setup for Node.js input handling (if needed for interactive use)
    process.stdin.resume();
    process.stdin.setEncoding("ascii");
    _input = "";
    process.stdin.on("data", input => _input += input);
    process.stdin.on("end", () => processData(_input));
}

/**
 * Benefits of this solution:
 * 1️⃣ Rolls two 6-sided dice (Total possible outcomes = 36).
 * 2️⃣ Counts all valid pairs where sum ≤ 9.
 * 3️⃣ Computes GCD to simplify the fraction representation of probability.
 * 4️⃣ Time Complexity: O(1) - Fixed 36 iterations.
 * 5️⃣ Space Complexity: O(1) - No extra memory used.
 */

// Run the function if being executed in a standalone Node.js environment
if (require.main === module) {
    processData();
}

// Export the function for testing purposes
function testProcessData() {
    function processData() {
        function hcf(a, b) {
            while (b) {
                [a, b] = [b, a % b];
            }
            return a;
        }

        let count = 0, total = 36;

        for (let i = 1; i <= 6; i++) {
            for (let j = 1; j <= 6; j++) {
                if (i + j <= 9) count++;
            }
        }

        let gcd = hcf(count, total);
        return `${count / gcd}/${total / gcd}`;
    }

    // ✅ Expected output: "5/9"
    let expectedOutput = "5/9";

    // Running five test cases
    for (let i = 1; i <= 5; i++) {
        let result = processData();
        console.log(`Test Case ${i}: ${result} ${result === expectedOutput ? "✅ PASS" : "❌ FAIL"}`);
    }
}

// Run the tests
testProcessData();