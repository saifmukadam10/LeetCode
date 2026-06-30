class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            # Right sum is everything else minus left_sum and the current number
            if left_sum == (total_sum - left_sum - num):
                return i
            
            # Update left_sum for the next iteration
            left_sum += num
            
        return -1
nums = [1, 7, 3, 6, 5, 6]
print(Solution().pivotIndex(nums))