# def solution(intervals):
#     if not intervals:
#         return []
    
#     intervals.sort(key=lambda x: x[0])
    
#     ans = []
    
#     current = intervals[0]
    
#     for next in intervals[1:]:
#         if current[1] >= next[0]:
#             current[1] = max(current[1], next[1])
#         else:
#             ans.append(current)
#             current = next
    
#     ans.append(current)
    
#     return ans

# # テストケース

# def solution(nums):
#     n = len(nums)
#     ans = [0] * n

#     for i in range(n):
#         left = 0
#         right = 0
        
#         for j in range(i, -1, -1):　最初は自分の場所だからOK
#             if nums[j] > nums[i]:
#                 break
#             if nums[j] == nums[i] and j != i:
#                 break
#             left += 1
        
#         for k in range(i, n):
#             if nums[k] > nums[i]:
#                 break
#             if nums[k] == nums[i] and k != i:
#                 break
#             right += 1
        
#         ans[i] = left + right - 1
    
#     return ans


def solution(nums):
    n = len(nums)
    result = [0] * n

    # 左側からの最大値を求める
    left_max = [0] * n
    left_max[0] = nums[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], nums[i])

    # 右側からの最大値を求める
    right_max = [0] * n
    right_max[n-1] = nums[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], nums[i])

    print(right_max)
    print(left_max)
    for i in range(n):
        # 左側の部分配列の範囲を求める
        left = i
        while left >= 0 and nums[left] <= nums[i]:
            left -= 1

        # 右側の部分配列の範囲を求める
        right = i
        while right < n and nums[right] <= nums[i]:
            right += 1

        # 左側と右側の範囲を結合して、重複する中央の部分を1つ引く
        print(left)
        print(right)
        result[i] = (i - left) + (right - i - 1)
    
    return result





nums=[1,1,1,1,1]
# nums=[3,2,1,6,2]
print(solution(nums))


# 提出したコード
# def solution(intervals):
    
#     intervals.sort(key=lambda x: x[0])

#     current = intervals[0]
    
#     ans = []
    
#     for next in intervals[1:]:
#         if current[1] >= next[0]:
#             current[1] = max(current[1], next[1])
#         else:
#             ans.append(current)
#             current = next
    
#     ans.append(current)
    
#     return ans

# def solution(nums):
#     n = len(nums)
#     ans = [0] * n

#     for i in range(n):
#         left = 0
#         right = 0
        
#         for j in range(i, -1, -1):
#             if nums[j] > nums[i]:
#                 break
#             if nums[j] == nums[i] and j != i:
#                 break
#             left += 1
        
#         for k in range(i, n):
#             if nums[k] > nums[i]:
#                 break
#             if nums[k] == nums[i] and k != i:
#                 break
#             right += 1
        
#         ans[i] = left + right - 1
    
#     return ans