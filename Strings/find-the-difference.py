class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sm1 = sum([ord(i) for i in s])
        sm2 = sum([ord(i) for i in t])
        return chr(sm2-sm1)
        
