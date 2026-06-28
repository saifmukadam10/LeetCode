class Solution:
    def binarySearch(self, nums: list[int], target : int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right: 
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return -1
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
print(Solution().binarySearch(nums, target))