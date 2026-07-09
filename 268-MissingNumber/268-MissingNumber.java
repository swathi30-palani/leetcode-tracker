// Last updated: 7/9/2026, 9:01:35 AM
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int sum = n * (n + 1) / 2;

        for(int num : nums){
            sum -= num;
        } 
        return sum;
    }
}