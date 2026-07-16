// Last updated: 7/16/2026, 9:07:05 AM
1public class Solution {
2    public List<List<Integer>> levelOrderBottom(TreeNode root) {
3        Queue<TreeNode> queue = new LinkedList<TreeNode>();
4        List<List<Integer>> wrapList = new LinkedList<List<Integer>>();
5        
6        if(root == null) return wrapList;
7        
8        queue.offer(root);
9        while(!queue.isEmpty()){
10            int levelNum = queue.size();
11            List<Integer> subList = new LinkedList<Integer>();
12            for(int i=0; i<levelNum; i++) {
13                if(queue.peek().left != null) queue.offer(queue.peek().left);
14                if(queue.peek().right != null) queue.offer(queue.peek().right);
15                subList.add(queue.poll().val);
16            }
17            wrapList.add(0, subList);
18        }
19        return wrapList;
20    }
21}