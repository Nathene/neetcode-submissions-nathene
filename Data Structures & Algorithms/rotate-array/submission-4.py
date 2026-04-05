class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy = nums[::-1]
        print(copy)
        k = k % len(nums)
        want = copy[:k]
        rest = copy[k:]
        print(want, rest)
        want = want[::-1]
        rest = rest[::-1]
        print(want, rest)
        idx = 0
        for i in range(len(want)):
            nums[idx] = want[i]
            idx +=1
        for i in range(len(rest)):
            nums[idx] = rest[i]
            idx += 1

