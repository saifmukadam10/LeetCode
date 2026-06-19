class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        #SORTING APPROACH
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

    def containsDuplicate2(self, nums :list[int]) -> bool:
        #HASH SET APPROACH
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    def containsDuplicate3(self, nums: list[int]) -> bool:
        #HASH MAP APPROACH
        seen ={}
        for num in nums:
            if num in seen:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False

nums = [1, 2, 3, 1]
print(Solution().containsDuplicate3(nums))
# time complexity: O(n log n) due to sorting