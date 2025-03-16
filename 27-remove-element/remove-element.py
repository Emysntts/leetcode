from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        list_append = []
        nums2 = nums.copy()
        
        for i, element in enumerate(nums):
            if element == val: 
                list_append.append(i)

        nums.clear()
        nums.extend(item for i, item in enumerate(nums2) if i not in list_append)

        k = len(nums)
    
        return k

