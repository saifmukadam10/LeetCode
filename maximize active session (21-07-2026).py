class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        initial_ones = s.count('1')
        t = "1" + s + "1"
        
        # Parse string t into contiguous segments (char, length)
        segments = []
        for char in t:
            if segments and segments[-1][0] == char:
                segments[-1][1] += 1
            else:
                segments.append([char, 1])
        
        max_delta = 0
        
        # Look for '1' segments flanked by '0' segments on both sides
        for i in range(1, len(segments) - 1):
            if segments[i][0] == '1':
                # Check if both adjacent segments are '0's
                if segments[i - 1][0] == '0' and segments[i + 1][0] == '0':
                    left_zero_len = segments[i - 1][1]
                    right_zero_len = segments[i + 1][1]
                    max_delta = max(max_delta, left_zero_len + right_zero_len)
                    
        return initial_ones + max_delta
s = "110001100"
print(Solution().maxActiveSectionsAfterTrade(s))
#time complexity is O(n) and space complexity is 
        