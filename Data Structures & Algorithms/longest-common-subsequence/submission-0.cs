public class Solution {
    public int LongestCommonSubsequence(string text1, string text2) {
        int n = text1.Length;
        int m = text2.Length;
        
        // Tworzymy tabelę o rozmiarze (n+1) x (m+1)
        int[,] dp = new int[n + 1, m + 1];

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (text1[i - 1] == text2[j - 1]) {
                    // Jeśli znaki pasują, bierzemy wynik z "ukosu" i dodajemy 1
                    dp[i, j] = 1 + dp[i - 1, j - 1];
                } else {
                    // Jeśli nie pasują, bierzemy maksimum z góry lub z lewej
                    dp[i, j] = Math.Max(dp[i - 1, j], dp[i, j - 1]);
                }
            }
        }

        return dp[n, m];
    }
}