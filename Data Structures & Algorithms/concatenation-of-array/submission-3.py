

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

from dataclasses import dataclass
@dataclass
class test_meeting_rooms:
    name: str
    args: tuple[any, ...]
    expected: list[int]


tests = [
    test_meeting_rooms("easy example", ([1,2,3]), [1,2,3,1,2,3])
]

for test in tests:
    actual = Solution().getConcatenation(test.args)
    res: str = actual == "PASSED" if actual == test.expected else "FAILED"
    print(f'{test.name}: expected = {test.expected}, actual == {actual} -- {res} ')