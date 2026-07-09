// Last updated: 7/9/2026, 9:02:31 AM
import java.util.*;

class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
        int i = 0;

        while (i < words.length) {
            int j = i, lineLen = 0;
            while (j < words.length && lineLen + words[j].length() + (j - i) <= maxWidth) {
                lineLen += words[j].length();
                j++;
            }

            int spaces = maxWidth - lineLen;
            int gaps = j - i - 1;
            StringBuilder sb = new StringBuilder();

            if (j == words.length || gaps == 0) {
                for (int k = i; k < j; k++) {
                    sb.append(words[k]);
                    if (k < j - 1) sb.append(" ");
                }
                while (sb.length() < maxWidth) sb.append(" ");
            } else {
                int spaceEach = spaces / gaps;
                int extra = spaces % gaps;
                for (int k = i; k < j; k++) {
                    sb.append(words[k]);
                    if (k < j - 1) {
                        for (int s = 0; s < spaceEach; s++) sb.append(" ");
                        if (extra-- > 0) sb.append(" ");
                    }
                }
            }

            result.add(sb.toString());
            i = j;
        }

        return result;
    }
}
