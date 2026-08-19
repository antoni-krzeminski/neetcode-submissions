public class Solution {
    public int MaxProfit(int[] prices) {
        if (prices == null || prices.Length <= 1) return 0;

        int n = prices.Length;
        
        // Stan 'hold': Maksymalny zysk, gdy posiadamy akcję
        int hold = -prices[0];
        // Stan 'sold': Maksymalny zysk tuż po sprzedaży (wymusza cooldown jutro)
        int sold = 0;
        // Stan 'rest': Maksymalny zysk, gdy jesteśmy w cooldownie lub po prostu czekamy
        int rest = 0;

        for (int i = 1; i < n; i++) {
            int prevHold = hold;
            int prevSold = sold;
            int prevRest = rest;

            // 1. Możemy trzymać akcję lub kupić nową (tylko jeśli wczoraj odpoczywaliśmy)
            hold = Math.Max(prevHold, prevRest - prices[i]);

            // 2. Możemy sprzedać tylko jeśli wczoraj trzymaliśmy akcję
            sold = prevHold + prices[i];

            // 3. Odpoczynek: max z wczorajszej sprzedaży (wchodzimy w cooldown) 
            // lub wczorajszego odpoczynku
            rest = Math.Max(prevRest, prevSold);
        }

        // Wynik to max z bycia w stanie 'sold' lub 'rest' (nie opłaca się kończyć z akcją w ręku)
        return Math.Max(sold, rest);
    }
}