# n = int(input())
# arr = []
# for i in range(n):
#     value = int(input())
#     arr.append(value)
     
# nums = sorted(set(arr))
# if len(nums) >= 3:
#     print(nums[-3])
# else:
#     print(max(nums))
# Time Complexity: O(n log n) ; Space complexity: O(n). the problem can be solved with T.C: O(n) i mean without sorting 

n = int(input())

max1 = max2 = max3 = float('-inf')

for _ in range(n):
    x = int(input())
    
    if x == max1 or x == max2 or x == max3:
        continue  # duplicate hole, podium touch korbo na
    
    if x > max1:
        max3 = max2
        max2 = max1
        max1 = x
    elif x > max2:
        max3 = max2
        max2 = x
    elif x > max3:
        max3 = x

if max3 == float('-inf'):
    print(max1)
else:
    print(max3)