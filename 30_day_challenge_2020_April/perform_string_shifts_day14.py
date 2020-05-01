class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        move = sum(map(lambda ll: ll[1] if ll[0] == 1 else -ll[1], shift)) % len(s)        
        return s[-move:] + s[:-move]