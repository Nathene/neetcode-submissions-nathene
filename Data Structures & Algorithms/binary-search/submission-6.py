class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            print(f"mid: {mid}, nums[mid] = {nums[mid]}")
            print(nums[mid] == target)
            print(f"{nums[mid]} == {target}")
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        

        return res