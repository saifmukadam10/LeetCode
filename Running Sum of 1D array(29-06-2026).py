class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum = 0
        arr =[]
        for i in range (len(nums)):
            sum += nums[i]
            arr.append(sum)
        return arr
nums = [1, 2, 3, 4]
print(Solution().runningSum(nums))
#time complexity is O(n) and space complexity is O(n)
        
        