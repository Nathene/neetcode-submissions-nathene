class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {

        auto can_eat = [&piles, h](int k) -> bool {
            int hours = 0;
            for (auto const& pile : piles) {
                hours += (pile + k - 1) / k;
            }
            return (hours <= h);
        };

        int l = 1;
        int r = *std::ranges::max_element(piles);
        int best = r;
        while (l <= r) {
            int mid = l + (r - l) / 2;

            if (can_eat(mid)) {
                best = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return best;
    }

};
