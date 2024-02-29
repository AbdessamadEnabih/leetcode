# Intersection of Two Arrays II
# 32 ms Beats 99.80% of users with Python3
from collections import Counter
def intersect(nums1, nums2):
    values = list()
    pnt1, pnt2 = 0, 0
    
    nums1.sort()
    nums2.sort()
    
    while pnt1 < len(nums1) and pnt2 < len(nums2):
        if nums1[pnt1] == nums2[pnt2]:
            values.append(nums1[pnt1])
            pnt1 +=1
            pnt2 +=1
        elif nums1[pnt1] < nums2[pnt2]:
            pnt1 += 1
        else : 
            pnt2 += 1

    return values

nums1 = [1, 2, 2, 1]
nums2 = [2]
print(intersect(nums1, nums2))
