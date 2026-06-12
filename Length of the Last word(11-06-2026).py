class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newstr = s.strip().split()
        return len(newstr[-1])
s = "Hello World"
print(Solution().lengthOfLastWord(s))