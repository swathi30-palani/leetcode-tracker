// Last updated: 7/9/2026, 9:01:25 AM
class Solution {
    public boolean checkGoodInteger(int n) {
        int digitSum = 0;
        int squareSum = 0;

        while (n > 0) {
            int digit = n % 10;
            digitSum += digit;
            squareSum += digit * digit;
            n /= 10;
        }

        return (squareSum - digitSum) >= 50;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.checkGoodInteger(1000));
        System.out.println(sol.checkGoodInteger(19));
    }
}
