// Last updated: 7/9/2026, 9:01:28 AM
class Solution {
    public int countValidSubarrays(int[] nums,int x){
        int n = nums.length;
        int count = 0;

        for(int i = 0; i < n; i++){
            long sum = 0;

            for(int j = i; j < n; j++){
            sum += nums[j];

            long temp = sum;

            int lastDigit = (int)(temp % 10);

            while(temp >= 10){
                temp /= 10;
            }
            int firstDigit = (int)temp;

            if(firstDigit == x && lastDigit == x){
                count++;  
            }
        }
    }
    return count;
    }
}