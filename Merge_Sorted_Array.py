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

# this above solution is very bad , it has T.C = O(m+nlog(m+n))  and it can be O(m+n)

m = int(input())

nums1 = []
for i in range(m):
    nums1.append(int(input()))

n = int(input())

nums2 = []
for i in range(n):
    nums2.append(int(input()))

# Add empty spaces to nums1
nums1 += [0] * n

# Three pointers
i = m - 1
j = n - 1
k = m + n - 1

# Merge from the back
while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1

    k -= 1

# If elements are remaining in nums2
while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1

print(nums1)

# its two pointer method and most optimized cuz T.C = O(M+N) and S.C = (1)