class Solution:
    def romanToInt(self, s: str) -> int:
        translation = {
            "I": 1, 
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M" : 1000

        }
        results = 0
        d = len(s)

        for i in range(d):
            if i + 1< d and translation[s[i]]< translation[s[i+1]]:
                results -= translation[s[i]]
            else:
                results += translation[s[i]]
        return results
        
        











#    class Solution:
#     def romanToInt(self, s: str) -> int:
#         translations = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         number = 0
#         s = s.replace("IV", "IIII").replace("IX", "VIIII")
#         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#         for char in s:
#             number += translations[char]
#         return number     