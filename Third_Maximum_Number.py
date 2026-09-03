#i am solving leetcode 414 third maximum number now give me hint as a interviewer
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
arr = []
for i in range(n):
    value = int(input())
    arr.append(value)

nums = list(set(arr))