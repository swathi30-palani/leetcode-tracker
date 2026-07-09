// Last updated: 7/9/2026, 9:01:23 AM
class Solution {
    public int maxDistance(String moves){
        int u = 0, d = 0, l = 0, r = 0, blank = 0;

        for(int c : moves.toCharArray()){
            if(c == 'U') u++;
            else if(c == 'D') d++;
            else if(c == 'L') l++;
            else if(c == 'R') r++;
            else blank++;
        }
        int veritical = Math.abs(u - d);
        int horizontal = Math.abs(l - r);

        return veritical + horizontal + blank;
    }
}