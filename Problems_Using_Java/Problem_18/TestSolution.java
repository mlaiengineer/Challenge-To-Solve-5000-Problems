public class TestSolution {
    public static void main(String[] args) {
        Solution solution = new Solution();
        //Test Case 1: Basic Input
        int[] nums1 = {3, 2, 2, 3};
        int val = 3;
        int k = solution.removeElement(nums1, val);
        System.out.println(k);
        //Test Case 2: All Elements Are the Same
        int [] nums2 = {2, 2, 2, 2};
        int val2 = 2;
        int k2 = solution.removeElement(nums2, val2);
        System.out.println(k2);
        //Test Case 3: No Elements to Remove
        int [] nums3 = {1, 2, 3, 4};
        int val3 = 5;
        int k3 = solution.removeElement(nums3, val3);
        System.out.println(k3);
        //Test Case 4: Mixed Elements
        int [] nums4 = {1, 2, 3, 2, 1};
        int val4 = 2;
        int k4 = solution.removeElement(nums4, val4);
        System.out.println(k4);
        //Test Case 5: Empty Array
        int [] nums5 = {};
        int val5 = 2;
        int k5 = solution.removeElement(nums5, val5);
        System.out.println(k5);
        //Test Case 6: Large Array with Multiple Values
        int [] nums6 = {1, 2, 3, 4, 5, 2, 2, 6, 7, 2};
        int val6 = 2;
        int k6 = solution.removeElement(nums6, val6);
        System.out.println(k6);
    }
}
