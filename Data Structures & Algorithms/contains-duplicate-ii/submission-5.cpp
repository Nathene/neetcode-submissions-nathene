class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        std:unordered_set<int> seen;
        
        int l = 0;
        for (int r = 0; r < nums.size(); r++) {
            if (seen.contains(nums[r])) return true;
            seen.insert(nums[r]);
            if (r - l >= k) {
                seen.erase(nums[l]);
                l++;
            }
        }
        return false;
    }
};