// Last updated: 8/16/2026, 9:38:10 AM
1class Solution {
2    public List<Integer> getRow(int rowIndex) {
3
4        List<Integer> row = new ArrayList<>();
5
6        row.add(1);
7
8        for (int i = 1; i <= rowIndex; i++) {
9
10            row.add(1);
11
12            for (int j = i - 1; j > 0; j--) {
13                row.set(j, row.get(j) + row.get(j - 1));
14            }
15        }
16
17        return row;
18    }
19}