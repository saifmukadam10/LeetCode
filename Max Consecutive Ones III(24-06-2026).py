class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        max_len = 0
        zero_count = 0
        
        # Expand the window using the right pointer
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
                
            # If we have more than k zeros, shrink the window from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
                
            # Calculate the max length of the valid window seen so far
            max_len = max(max_len, right - left + 1)
            
        return max_len