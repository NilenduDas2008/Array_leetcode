from collections import Counter

n = int(input())
nums = []

for _ in range(n):
    value = int(input())
    nums.append(value)

# frequency = Counter(nums)

# for num, count in frequency.items():
#     if count == 1:
#         print(num)
#         break
# this solution is good Time : O(N)  ; Space : O(N) the space can be optimised 

ans = 0
for num in nums:
    ans ^= num

print(ans)

#Time:  O(N) ; Space: O(1)
