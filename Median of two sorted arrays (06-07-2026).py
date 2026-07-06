class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search time complexity
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        total_half = (m + n + 1) // 2
        
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = total_half - partition1
            
            # Edge cases: if partition is at the boundaries, use infinity
            maxLeft1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            minRight1 = nums1[partition1] if partition1 < m else float('inf')
            
            maxLeft2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            minRight2 = nums2[partition2] if partition2 < n else float('inf')
            
            # Check if we found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If total number of elements is odd
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                # If total number of elements is even
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                
            elif maxLeft1 > minRight2:
                # We are too far right in nums1, move left
                right = partition1 - 1
            else:
                # We are too far left in nums1, move right
                left = partition1 + 1

# Example usage
nums1 = [1, 3]
nums2 = [2]
solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 2.0