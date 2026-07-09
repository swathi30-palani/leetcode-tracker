// Last updated: 7/9/2026, 9:03:00 AM
class Solution {
    private int count = 0;

    public int totalNQueens(int n) {
        boolean[] cols = new boolean[n];          // track used columns
        boolean[] d1 = new boolean[2 * n];        // track used diagonals (row+col)
        boolean[] d2 = new boolean[2 * n];        // track used diagonals (row-col+n)
        backtrack(0, n, cols, d1, d2);
        return count;
    }

    private void backtrack(int row, int n, boolean[] cols, boolean[] d1, boolean[] d2) {
        if (row == n) {
            count++;
            return;
        }
        for (int col = 0; col < n; col++) {
            int id1 = row + col;
            int id2 = row - col + n;
            if (cols[col] || d1[id1] || d2[id2]) continue;

            cols[col] = d1[id1] = d2[id2] = true;
            backtrack(row + 1, n, cols, d1, d2);
            cols[col] = d1[id1] = d2[id2] = false; // backtrack
        }
    }
}
