// Last updated: 7/15/2026, 9:58:27 PM
1
2class Solution {
3    public boolean helper(TreeNode p, TreeNode q) {
4        // Case 1: Both nodes are null — perfectly balanced structural match ✓
5        if (p == null && q == null) return true;
6        
7        // Case 2: One node is null while the other exists — structural asymmetry ✗
8        if (p == null || q == null) return false;
9        
10        // Case 3: The values of the corresponding mirror nodes don't match ✗
11        if (p.val != q.val) return false;
12        
13        // Recursively cross-check outer branches and inner branches simultaneously 🔀
14        return helper(p.left, q.right) && helper(p.right, q.left);
15    }
16
17    public boolean isSymmetric(TreeNode root) {
18        if (root == null) return true;
19        // Launch mirror comparisons using the left and right children of the root anchor node
20        return helper(root.left, root.right);
21    }
22}