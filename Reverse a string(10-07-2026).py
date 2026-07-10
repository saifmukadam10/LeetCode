class Solution:
    def reverseString(self, s: list[str]) -> None:
        
       left =0 
       right = len(s) - 1

       while left < right:
        s[left],s[right] = s[right], s[left]
        left += 1
        right -=1
s = ["h","e","l","l","o"]
Solution().reverseString(s)
print(s)
#time complexity is O(n) and space complexity is O(1)