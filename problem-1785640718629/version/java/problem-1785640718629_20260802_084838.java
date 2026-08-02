// Last updated: 8/2/2026, 8:48:38 AM
1class Solution {
2    private int gcd(int a, int b){
3        while(b != 0){
4            int temp = b;
5            b = a % b;
6            a = temp;
7        }
8        return a;
9    }
10    public long maxPairStrength(int[] nums) {
11        long ans = 0;
12        for (int i = 0; i < nums.length ; i++){
13            for (int j = 0; j < nums.length; j++){
14                int g = gcd(nums[i] , nums[j]);
15                long strength = (1L * nums[i] * nums[j]) / (1L * g * g);
16                ans = Math.max(ans, strength);
17            }
18        }
19        return ans;    
20    }
21}