class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occr = {}
        
        for num in nums:
            if num in occr:
                occr[num] += 1
            else:
                occr[num] = 1

        for num in occr:
            if occr[num] >= len(nums)/2:
                return num

        return 1