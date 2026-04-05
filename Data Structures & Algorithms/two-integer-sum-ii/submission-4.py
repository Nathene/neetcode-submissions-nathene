class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            left, right = numbers[l], numbers[r]

            if left + right > target:
                r -= 1
            elif left + right < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        return []