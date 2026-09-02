from collections import Counter

m = int(input())
nums1 = []
for i in range(m):
    value1  = int(input())
    nums1.append(value1)

n = int(input())
nums2 = []
for i in range(n):  
    value2 = int(input())
    nums2.append(value2)

freq1 = Counter(nums1)
freq2 = Counter(nums2)

intersection_number = freq1 & freq2 
result = list(intersection_number.elements())
print(result)

#Time: O(m + n + k)  ,  Space: O(m + n) in the worst case in above code the S.C can be optimized











