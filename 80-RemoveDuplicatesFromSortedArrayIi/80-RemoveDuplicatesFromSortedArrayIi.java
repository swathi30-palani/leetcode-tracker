// Last updated: 7/9/2026, 9:02:11 AM
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length <= 2) return nums.length;

        int index = 2; // start from 3rd element
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] != nums[index - 2]) {
                nums[index] = nums[i];
                index++;
            }
        }
        return index;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {1,1,1,2,2,3};
        int len = sol.removeDuplicates(nums);
        System.out.println("New length: " + len);
        for (int i = 0; i < len; i++) {
            System.out.print(nums[i] + " ");
        }
    }
}
