class Solution:
    def merge(self, nums1 : list[int], nums2: list[int], m : int, n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i]> nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -=1
            k -= 1
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3
Solution().merge(nums1, nums2, m, n)
print(nums1)