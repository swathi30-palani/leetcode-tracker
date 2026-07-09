// Last updated: 7/9/2026, 9:01:21 AM
class Solution {
    public long maxSubarraySum(int[] nums, int k) {
        long NEG = Long.MIN_VALUE/4;
        
        long noOp = NEG;
        long mul = NEG;
        long div = NEG;
        long afterMul = NEG;
        long afterDiv = NEG;
        
        long ans = NEG;

        for(int x : nums){
            long  m = 1L * x * k;
            long d = x / k;

            long nNoOp = Math.max(noOp + x, (long) x);
            long nMul = Math.max(Math.max(noOp + m, m), mul + m);
            long nDiv = Math.max(Math.max(noOp + d, d), div + d);

            long nAfterMul = Math.max(Math.max(afterMul + x, mul + x), (long) x);
            long nAfterDiv = Math.max(Math.max(afterDiv + x, div + x), (long) x);
            
            noOp = nNoOp;
            mul = nMul;
            div = nDiv;
            afterMul = nAfterMul;
            afterDiv = nAfterDiv;
            ans = Math.max(ans , 
                  Math.max(noOp, 
                  Math.max(nMul,
                  Math.max(nDiv, 
                  Math.max(nAfterMul, nAfterDiv)))));
            
        }
        return ans;    
    }
}