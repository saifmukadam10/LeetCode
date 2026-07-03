class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:

            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[l]
nums = [3, 4, 5, 1, 2]
print(Solution().findMin(nums))
#time complexity is O(log n) and space complexity is O(1)