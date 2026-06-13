class Solution1:
    def isValid1(self, s: str) -> bool:
        a = []
        i =0
        for i in range(len(s)):
            if s [i] == '(' or s[i] == '[' or s[i] == '{':
                a.append(s[i])
            else:
                if not a:
                    return False
                top = a.pop()
                if s[i] == ')' and top != '(':
                    return False
                if s[i] == ']' and top != '[':
                    return False
                if s[i] == '}' and top != '{':
                    return False
        return len(a)== 0
    
#optimal solution   
class Solution:
    def isValid(self, s: str) -> bool :
        stack = []
        bracket_map ={')':'(',
                      ']':'[',
                      '}':'{'}
        for char in s:
            if char in bracket_map:
                top = stack.pop() if stack else '#'
                if bracket_map[char] != top:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
s = "(([][]{}))"
print(Solution().isValid(s))