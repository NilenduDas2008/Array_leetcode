# n = int(input())
# nums = []

# for _ in range(n):
#     value = int(input())
#     nums.append(value)

# missing = list(set(range(n + 1)) - set(nums))[0] : using extra space through set
# print(missing)


n = int(input())

missing = n

for i in range(n):
    value = int(input())
    missing ^= i
    missing ^= value

print(missing)