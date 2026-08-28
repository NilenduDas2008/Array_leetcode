# m = int(input())
# n = int(input())

# nums1 = []
# for i in range(m):
#     item1 = int(input())
#     nums1.append(item1)

# nums2 = []
# for i in range(n):
#     item2 = int(input())
#     nums2.append(item2)

# nums1 += nums2
# nums1.sort()

# this above solution is good but it has T.C = O(m+nlog(m+n))  and it can be O(m+n)

m = int(input())
n = int(input())

nums1 = []
for _ in range(m):
    nums1.append(int(input()))

nums2 = []
for _ in range(n):
    nums2.append(int(input()))

result = []

i = 0
j = 0

while i < m and j < n:
    if nums1[i] <= nums2[j]:
        result.append(nums1[i])
        i += 1
    else:
        result.append(nums2[j])
        j += 1

while i < m:
    result.append(nums1[i])
    i += 1

while j < n:
    result.append(nums2[j])
    j += 1

print(*result)