nums1=input("number 1 :").split(" ")
nums2=input("number 2 :").split(" ")

def findMedianSortedArrays(self, nums1, nums2):
     """
     :type nums1: List[int]
     :type nums2: List[int]
     :rtype: float
     """
     nums=sorted(nums1+nums2)
     if len(nums)%2 == 1 :
         return nums[len(nums) // 2]
     else:
         mid1 = nums[(len(nums) // 2) - 1]
         mid2 = nums[len(nums) // 2]
         return (mid1 + mid2) / 2.0