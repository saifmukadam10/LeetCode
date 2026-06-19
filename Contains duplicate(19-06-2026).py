class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        #SORTING APPROACH
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
nums = [1, 2, 3, 5]
print(Solution().containsDuplicate(nums))
# time complexity: O(n log n) due to sorting