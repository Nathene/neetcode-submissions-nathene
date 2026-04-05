class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [ [] for i in range(len(nums) + 1)]

        count = Counter(nums)

        for key, val in count.items():
            freq[val].append(key)
        
        res = []
        for i in range(len(freq) -1, -1, -1):
            if freq[i] == []:
                continue
            while freq[i] != [] and k > 0:
                res.append(freq[i].pop())
                k -= 1
            if k == 0:
                break
        
        return res


