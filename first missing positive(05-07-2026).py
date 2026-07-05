class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:

        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:

                correct_idx = nums[i] -1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        
        # Step 3: If all numbers 1 to n are present, return n + 1
        return len(nums) + 1
nums = [3, 4, -1, 1]
print(Solution().firstMissingPositive(nums))
        