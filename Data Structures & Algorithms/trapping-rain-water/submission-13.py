class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = [0] * len(height)
        r_max = [0] * len(height)

        curr_max = 0

        for i in range(len(height)):
            curr_max = max(curr_max, height[i])
            l_max[i] = curr_max 

        curr_max = 0
        for i in range(len(height) -1, -1, -1):
            curr_max = max(curr_max, height[i])
            r_max[i] = curr_max
        
        res = 0

        for i in range(len(l_max)):
            res += min(l_max[i], r_max[i]) - height[i]
        
        return res