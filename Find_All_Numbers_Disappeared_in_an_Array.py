n = int(input())
nums = []

for _ in range(n):
    num = int(input())
    nums.append(num)  

arr = list(range(1,n+1))

nums_set = set(nums)
result = [x for x in arr if x not in nums_set]
print(result)

# Time Complexity: O(n) ;  Space Complexity: O(n)