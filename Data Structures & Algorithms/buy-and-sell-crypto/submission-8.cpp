class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int result = 0;

        int cur_min = prices[0];
        int cur_max = 0;

        for (const int& price : prices) {
            cur_min = std::min(cur_min, price);

            int current_profit = price - cur_min;

            cur_max = std::max(cur_max, current_profit);
        }
        return cur_max;
    }
};
