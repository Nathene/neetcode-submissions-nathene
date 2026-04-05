class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        one, two, three = 0, 1, 1

        for i in range(3, n+1):
            new_val = one + two + three
            one = two
            two = three
            three = new_val
        
        return three