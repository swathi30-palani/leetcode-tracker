// Last updated: 7/9/2026, 9:01:34 AM
class Solution {
    public void moveZeroes(int[] nums){

        int index = 0;

        for(int i = 0; i < nums.length; i++){
            if(nums[i] != 0){
                nums[index] = nums[i];
                index++;
            }
        }
        while(index < nums.length){
            nums[index] = 0;
            index++;
        }
    }
}