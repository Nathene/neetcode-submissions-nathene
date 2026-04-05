class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 0
        digits[len(digits) - 1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if rem:
                digits[i] += 1
                rem = 0
            if digits[i] > 9:
                digits[i] = digits[i] % 10
                rem = 1
        
        return [1] + digits if rem else digits

        