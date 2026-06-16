class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal =[]
        newstr  = s.lower()
        for char in newstr:
            if char.isalnum():
                pal.append(char)
        cleaned = "".join(pal)

        left =0
        right = len(cleaned)-1
        while left <= right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True
s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))    
