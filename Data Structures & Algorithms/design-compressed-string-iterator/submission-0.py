from typing import Generator
class StringIterator:

    def __init__(self, compressedString: str):
        self._generator = self._decompress(compressedString)
        self.next_val = next(self._generator, None)
    
    def _decompress(self, s: str) -> Generator[int, None, None]:
        i = 0
        while i < len(s):
            char = s[i]
            i += 1
            num_str = ""

            while i < len(s) and s[i].isdigit():
                num_str += s[i]
                i += 1
            
            count = int(num_str)

            for _ in range(count):
                yield char

    def next(self) -> str:
        if not self.hasNext(): return ""
        char = self.next_val
        self.next_val = next(self._generator, None)
        return char

    def hasNext(self) -> bool:
        return self.next_val is not None


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
