// Last updated: 7/16/2026, 9:03:42 AM
1class Solution {
2    public TreeNode buildTree(int[] inorder, int[] postorder) {
3        return buildTree(inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1);
4    }
5    
6    private TreeNode buildTree(int[] inorder, int inStart, int inEnd, int[] postorder, int postStart, int postEnd) {
7        
8        if (inStart > inEnd || postStart > postEnd) {
9            return null;
10        }
11        
12        
13        int rootVal = postorder[postEnd];
14        TreeNode root = new TreeNode(rootVal);
15        
16        
17        int rootIndex = 0;
18        for (int i = inStart; i <= inEnd; i++) {
19            if (inorder[i] == rootVal) {
20                rootIndex = i;
21                break;
22            }
23        }
24        
25       
26        int leftSize = rootIndex - inStart;
27        int rightSize = inEnd - rootIndex;
28        root.left = buildTree(inorder, inStart, rootIndex - 1, postorder, postStart, postStart + leftSize - 1);
29        root.right = buildTree(inorder, rootIndex + 1, inEnd, postorder, postEnd - rightSize, postEnd - 1);
30        
31        return root;
32    }
33}
34