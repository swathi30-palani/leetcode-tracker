// Last updated: 7/9/2026, 9:01:26 AM
class Solution {
    public long maxSum(int[] nums, int k, int mul) {
        Arrays.sort(nums);
        long ans = 0;
        int cur = mul;
        for(int i = nums.length - 1 ; i >= nums.length - k; i--){
            if(cur > 1){
                ans += 1L * nums[i] * cur;   
            } else {
                ans += nums[i];
            }
            cur--;
        }
        return ans;    
    }
}