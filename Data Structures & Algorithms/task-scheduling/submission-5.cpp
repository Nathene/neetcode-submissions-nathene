class Solution {

public:
    int leastInterval(vector<char>& tasks, int n) {
        if (n == 0) return tasks.size();

        std::unordered_map<char, int> count;
        for (char t : tasks) count[t]++;

        std::priority_queue<int> available;
        for (const auto& [_, freq] : count) {
            available.push(freq);
        }

        std::deque<std::pair<int, int>> frontier;

        int cycles{};

        while (!available.empty() || !frontier.empty()) {
            cycles++;

            if (!available.empty()) {
                int freq = available.top() - 1;
                available.pop();

                if (freq > 0) {
                    frontier.push_back({freq, cycles + n});
                }
            }

            if (!frontier.empty() && frontier.front().second <= cycles) {
                available.push(frontier.front().first);
                frontier.pop_front();
            }

        }

        return cycles;



    }
};
