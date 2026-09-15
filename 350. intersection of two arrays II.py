class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = []
        for i in nums1:
            if i in nums2:
                intersect.append(i)
                nums2.remove(i)
        return intersect
