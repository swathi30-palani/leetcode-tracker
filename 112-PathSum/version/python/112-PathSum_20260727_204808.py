# Last updated: 7/27/2026, 8:48:08 PM
1class Solution:
2    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
3        if not root:
4            return False
5        
6        if not root.left and not root.right:
7            return targetSum - root.val == 0
8        
9        targetSum -= root.val
10        
11        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)