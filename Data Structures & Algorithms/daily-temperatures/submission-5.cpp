class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        if (temperatures.size() < 1) return std::vector<int>{};
        
        std::vector<int> result(temperatures.size(), 0);
        std::stack<std::pair<int, int>> st;

        for (size_t i = 0; i < temperatures.size(); i++) {
            while (!st.empty() && temperatures[i] > st.top().first) {
                auto [temp, ind] = st.top();
                st.pop();

                result[ind] = i - ind; 
            }
            st.push({temperatures[i], i});
        }
        return result;
    }
};
