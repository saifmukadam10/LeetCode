class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert_pos = 0

        for i in range(len(nums)):
            if nums[i]== 0:
                nums[insert_pos], nums[i]= nums[i], nums[insert_pos]
                insert_pos += 1
        return nums

nums = [0,1,2,4,0]
print(Solution().moveZeroes(nums))

#Time Complexity - O(n)
#Space - O(1)