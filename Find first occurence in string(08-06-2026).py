class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
    haystack = "hello"
    needle = "ll"   
    print(Solution().strStr(haystack, needle))  # Output: 2