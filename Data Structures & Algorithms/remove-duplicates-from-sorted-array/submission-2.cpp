class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        std::unordered_set<int> my_set;
        auto it = std::unique(nums.begin(), nums.end());

        nums.erase(it, nums.end());

        return nums.size();
    }
};