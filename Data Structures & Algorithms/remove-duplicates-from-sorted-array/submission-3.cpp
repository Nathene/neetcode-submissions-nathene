class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        auto it = std::unique(nums.begin(), nums.end());

        nums.erase(it, nums.end());

        return nums.size();
    }
};