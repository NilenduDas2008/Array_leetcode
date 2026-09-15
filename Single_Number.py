from collections import Counter
n = int(input())
nums = Counter([0]*n)

for _ in range(len(nums)):
    value = int(input())
    nums.append(value)
# for key, count in nums.items():
#     if count == 1:
#         print(key) : this solution is good Time : O(N)  ; Space : O(N) the space can be optimised 

ans = 0
for num in nums:
    ans ^= num

print(ans)

#Time:  O(N) ; Space: O(1)
