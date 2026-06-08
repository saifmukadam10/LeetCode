class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if nums is None:
            return 0
        write_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index
nums = [3, 3, 3, 3]
val = 3
print(Solution().removeElement(nums, val))  # Output: 2