#include <limits>

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = numeric_limits<int>::max();
        int max_profit = 0;

        for (int i = 0; i < prices.size(); i++) {
            if (prices[i] < min_price) {
                min_price = prices[i];
            }

            int curr_profit = prices[i] - min_price;

            if (curr_profit > max_profit) {
                max_profit = curr_profit;
            }
        }

        return max_profit;
    }
};
