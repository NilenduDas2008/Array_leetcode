from collections import Counter

n = int(input())
nums = []
for _ in range(n):
    value = int(input())
    nums.append(value)
k = int(input())

# count = 0
# for i in range(n):
#     for j in range(i , n):
#         sum = 0
#         for x in range(i , j+1):
#             sum += nums[x]
#             if sum == k:
#                 count += 1
# print(count)

# this is brute force approach and it has time complexity of O(N^3)

# prefix_sum = [0] * (n + 1)

# for i in range(n):
#     prefix_sum[i + 1] = prefix_sum[i] + nums[i]

# count = 0
 
# for i in range(n):
#     for j in range(i, n):
#         subarray_sum = prefix_sum[j + 1] - prefix_sum[i]

#         if subarray_sum == k:
#             count += 1

# print(count)
         
# this is the approach where we use prefix sum method and now the T.C:O(N^2) its better but still too much . If we use prefixSum + hashing then it can be O(N)

def subarraySum(nums, k):
    prefix_sum = 0
    count = 0

    prefix_freq = {0: 1}

    for num in nums:
        prefix_sum += num

        required = prefix_sum - k

        if required in prefix_freq:
            count += prefix_freq[required]

        prefix_freq[prefix_sum] = prefix_freq.get(prefix_sum, 0) + 1

    return count

# best approach using hashing and prefix sum both . T.C: O(N) and S.C: O(N)