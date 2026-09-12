import math
n = int(input())
nums = []

for i in range(n):
    value = int(input())
    nums.append(value)
# result = []
# for i in range(n):
#     skip_index = i
#     result.append(math.prod(nums[:skip_index] + nums[skip_index + 1:]))
# print(result)
# this code has T.C: O(N^2) so time limit exceeds .

left_prod = 1
right_prod = 1
result = [1]*len(nums)

for i in range(len(nums)):
    result[i] = left_prod
    left_prod *= nums[i]

for i in range(len(nums)-1, -1, -1):
    result[i] *= right_prod
    right_prod *= nums[i]
print(result)

# O(N) time ; O(N) space