# Last updated: 8/16/2026, 9:34:37 AM
1# Definition for a Node.
2class Node(object):
3    def __init__(self, val=0, left=None, right=None, next=None):
4        self.val = val
5        self.left = left
6        self.right = right
7        self.next = next
8
9
10class Solution(object):
11    def connect(self, root):
12        """
13        :type root: Node
14        :rtype: Node
15        """
16        if not root:
17            return None
18
19        level_start = root
20
21        while level_start.left:
22            current = level_start
23
24            while current:
25                current.left.next = current.right
26                if current.next:
27                    current.right.next = current.next.left
28                current = current.next
29
30            level_start = level_start.left
31
32        return root