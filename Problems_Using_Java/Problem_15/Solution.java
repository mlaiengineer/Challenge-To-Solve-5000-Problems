/**
 * This method computes the result of raising a number 'n' to the power of its reversed digits.
 * For instance, if n = 13, the reversed number becomes 31, and the result will be 13^31.
 *
 * @param n A positive integer input (Assumption: n > 0 to avoid reversal issues).
 * @return The result of raising the original number to the power of its reversed number.
 *         Note: This operation may overflow for large values due to integer limitations.
 */
class Solution {
    public static int reverseExponentiation(int n) {
        // Store the original number as 'n' will be modified during the reversal process
        int originalNumber = n;
        int reversedNumber = 0;

        // Reverse the digits of the number
        while (n > 0) {
            // Extract the last digit using modulo operation
            int lastDigit = n % 10;
            // Build the reversed number by shifting the existing digits to the left
            // and appending the last digit
            reversedNumber = reversedNumber * 10 + lastDigit;
            // Remove the last digit from 'n'
            n = n / 10;
        }

        // Compute the result by raising the original number to the power of the reversed number
        // Note: The result may overflow if the value exceeds the 32-bit integer limit
        int result = (int) Math.pow(originalNumber, reversedNumber);
        return result;
    }
}