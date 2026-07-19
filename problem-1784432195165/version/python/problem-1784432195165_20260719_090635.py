# Last updated: 7/19/2026, 9:06:35 AM
1class Solution:
2    def countDominantNodes(self, root):
3        self.count = 0
4
5        def dfs(node):
6            if not node:
7                return float("-inf")
8
9            left_max = dfs(node.left)
10            right_max = dfs(node.right)
11
12            subtree_max = max(left_max, right_max)
13
14            if node.val >= subtree_max:
15                self.count += 1
16
17            return max(node.val, subtree_max)
18
19        dfs(root)
20        return self.count