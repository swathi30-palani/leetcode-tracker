# Last updated: 8/14/2026, 3:55:44 PM
1# ✅ Approach 1: Extra Space
2class Solution:
3    def flatten(self, root: Optional[TreeNode]) -> None:
4        if not root: return
5        nodes = []
6        
7        def preorder(node):
8            if not node: return
9            nodes.append(node)
10            preorder(node.left)
11            preorder(node.right)
12        
13        preorder(root)
14        for i in range(len(nodes) - 1):
15            nodes[i].left = None
16            nodes[i].right = nodes[i + 1]
17
18# ✅ Approach 2: In-Place Optimized
19class Solution:
20    def flatten(self, root: Optional[TreeNode]) -> None:
21        current = root
22        while current:
23            if current.left:
24                temp = current.left
25                while temp.right:
26                    temp = temp.right
27                temp.right = current.right
28                current.right = current.left
29                current.left = None
30            current = current.right