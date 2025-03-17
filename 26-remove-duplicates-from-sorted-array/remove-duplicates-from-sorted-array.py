class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        nums2 = nums.copy()

        nums.clear()
        nums.extend(set(nums2))
        nums.sort()

        k = len(nums)
        return k