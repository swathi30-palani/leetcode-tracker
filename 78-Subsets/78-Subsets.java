// Last updated: 7/9/2026, 9:02:16 AM
import java.util.*;

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), nums, 0);
        return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> temp, int[] nums, int start) {
        result.add(new ArrayList<>(temp)); // add current subset

        for (int i = start; i < nums.length; i++) {
            temp.add(nums[i]);                  // choose element
            backtrack(result, temp, nums, i+1); // explore further
            temp.remove(temp.size() - 1);       // un-choose (backtrack)
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {1,2,3};
        System.out.println(sol.subsets(nums));
    }
}
