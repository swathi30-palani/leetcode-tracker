# Last updated: 7/27/2026, 8:49:30 PM
1class Solution:
2    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
3        res = []
4        def dfs(node, path, curSum):
5            if not node: return
6            curSum += node.val
7            path.append(node.val)
8            if not node.left and not node.right and curSum == targetSum:
9                res.append(path[:])
10            dfs(node.left, path, curSum)
11            dfs(node.right, path, curSum)
12            path.pop()
13        dfs(root, [], 0)
14        return res