class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        current_start = lower
        for num in nums:
            if num > current_start:
                # There is a gap between current_start and num - 1
                result.append([current_start, num - 1])
            current_start = num + 1

        # Don't forget to check if there's a gap after the last number!
        if current_start <= upper:
            result.append([current_start, upper])
        
        return result



       