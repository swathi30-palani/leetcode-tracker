// Last updated: 7/15/2026, 9:59:55 PM
1class Solution {
2    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
3        List<List<Integer>> res = new ArrayList<>();
4        if (root == null) return res;
5
6        Deque<TreeNode> q = new LinkedList<>();
7        q.addFirst(root);
8        boolean reverse = false;
9
10        while (!q.isEmpty()) {
11            List<Integer> current = new ArrayList<>();
12            int level = q.size();
13
14            for (int i = 0; i < level; i++) {
15                if (!reverse) {
16                    TreeNode curr = q.pollFirst();
17                    current.add(curr.val);
18                    if (curr.left != null) q.addLast(curr.left);
19                    if (curr.right != null) q.addLast(curr.right);
20                } else {
21                    TreeNode curr = q.pollLast();
22                    current.add(curr.val);
23                    if (curr.right != null) q.addFirst(curr.right);
24                    if (curr.left != null) q.addFirst(curr.left);
25                }
26            }
27
28            res.add(current);
29            reverse = !reverse;
30        }
31
32        return res;
33    }
34}