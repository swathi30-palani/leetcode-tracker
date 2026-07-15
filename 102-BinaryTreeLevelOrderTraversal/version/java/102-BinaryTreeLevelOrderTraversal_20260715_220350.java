// Last updated: 7/15/2026, 10:03:50 PM
1class Solution {
2    public TreeNode buildTree(int[] preorder, int[] inorder) {
3        Deque<Integer> preorderQueue = new ArrayDeque<>();
4        for (int val : preorder) {
5            preorderQueue.offer(val);
6        }
7
8        return build(preorderQueue, inorder);        
9    }
10
11    private TreeNode build(Deque<Integer> preorder, int[] inorder) {
12        if (inorder.length > 0) {
13            int idx = indexOf(inorder, preorder.poll());
14            TreeNode root = new TreeNode(inorder[idx]);
15
16            root.left = build(preorder, Arrays.copyOfRange(inorder, 0, idx));
17            root.right = build(preorder, Arrays.copyOfRange(inorder, idx + 1, inorder.length));
18
19            return root;
20        }
21        return null;
22    }
23
24    private int indexOf(int[] arr, int value) {
25        for (int i = 0; i < arr.length; i++) {
26            if (arr[i] == value) {
27                return i;
28            }
29        }
30        return -1; // shouldn't happen with valid input
31    }    
32}