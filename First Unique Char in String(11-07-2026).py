class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        
        # Count the occurrences of each character
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # Find the index of the first unique character
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        
        return -1
s = "leetcode"
print(Solution().firstUniqChar(s))
#time complexity is O(n) and space complexity is O(n)