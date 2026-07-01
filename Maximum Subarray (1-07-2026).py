class Solution:
    def maxSubArray(self, nums : list[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        n = len(nums)

        for i in range(1, n):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))
#time complexity is O(n) and space complexity is O(1)