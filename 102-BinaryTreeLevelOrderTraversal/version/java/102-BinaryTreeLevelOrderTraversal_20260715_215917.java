// Last updated: 7/15/2026, 9:59:17 PM
1class Solution {
2    public List<List<Integer>> levelOrder(TreeNode root) {
3        List<List<Integer>> ans = new ArrayList<>();
4
5        if(root == null){
6            return ans;
7        }
8
9        Queue<TreeNode> queue = new LinkedList<>();
10        queue.offer(root);
11
12        while(!queue.isEmpty()) {
13
14            int size = queue.size(); 
15            List<Integer> level = new ArrayList<>();
16
17            for(int i = 0; i < size; i++){
18
19                TreeNode curr = queue.poll();
20                level.add(curr.val);
21
22                if(curr.left != null){
23                    queue.offer(curr.left);
24                }
25
26                if(curr.right != null){
27                    queue.offer(curr.right);
28                }
29            }
30
31            ans.add(level);
32        }
33
34        return ans;
35    }
36}