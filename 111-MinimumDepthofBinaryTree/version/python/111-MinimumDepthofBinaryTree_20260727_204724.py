# Last updated: 7/27/2026, 8:47:24 PM
1from collections import deque
2
3class Solution(object):
4    def minDepth(self, root):
5        if not root:
6            return 0
7
8        queue = deque([(root, 1)])
9        while queue:
10            node, depth = queue.popleft()
11            if not node.left and not node.right:
12                return depth
13            if node.left:
14                queue.append((node.left, depth + 1))
15            if node.right:
16                queue.append((node.right, depth + 1))