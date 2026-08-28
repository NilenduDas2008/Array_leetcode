
# n = int(input())
# nums = []

# for i in range(n):
#     item = int(input())
#     nums.append(item)
# squared_nums = [x**2 for x in nums]
# squared_nums.sort()
# print(squared_nums)

# this above solution is good but T.C = O(nlogn) it can be O(n) with optimization

n = int(input())
nums = []

for counter in range(n):
    item = int(input())
    nums.append(item)

result = [0] * n

i = 0
j = n - 1
k = n - 1

while i <= j:
    if abs(nums[i]) > abs(nums[j]):
        result[k] = nums[i] * nums[i]
        i = i + 1
    else:
        result[k] = nums[j] * nums[j]
        j = j - 1

    k = k - 1

print(result)