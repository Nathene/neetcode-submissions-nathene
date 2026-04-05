class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = Counter(people)

        people.sort()
        res = 0
        l, r = 0, len(people) - 1
        
        while l <= r:
            if people[r] + people[l] > limit:
                r -= 1
            else:
                r -= 1
                l += 1
            res += 1
            
            
        
        return res
        
