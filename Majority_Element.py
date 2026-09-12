from collections import Counter

n = int(input())

nums = []

for _ in range(n):
    nums.append(int(input()))

freq = Counter(nums)

majority = max(freq, key=freq.get)

print(majority)
# Time Complexity: O(n) ; Space Complexity: O(n)