# メモ化用の辞書
memo = {}

def rec(x, y, z):
    if (x, y, z) in memo:
        return memo[(x, y, z)]
    
    if x <= y:
        memo[(x, y, z)] = y
        return y
    else:
        result = rec(rec(x - 1, y, z),
                     rec(y - 1, z, x),
                     rec(z - 1, x, y))
        memo[(x, y, z)] = result
        return result


# memo = {}

# def rec(a, b, c):
    
#     if a <= b:
#         return b
    
#     if (a, b, c) in memo:
#         return memo[(a, b, c)]
        
#     result = rec(rec(a-1, b, c),rec(b-1, c, a),rec(c-1, a, b))
    
#     memo[(a, b, c)] = result
#     return result

a, b, c = map(int, input().split())
result = rec(a, b, c)
print(result)



# memo = {}

# def rec(a, b, c):
#     stack = [(a, b, c)]
#     while stack:
#         a, b, c = stack.pop()
#         if (a, b, c) in memo:
#             continue
        
#         if a <= b:
#             memo[(a, b, c)] = b
#         else:
#             if (a-1, b, c) not in memo:
#                 stack.append((a, b, c))
#                 stack.append((a-1, b, c))
#                 continue
#             if (b-1, c, a) not in memo:
#                 stack.append((a, b, c))
#                 stack.append((b-1, c, a))
#                 continue
#             if (c-1, a, b) not in memo:
#                 stack.append((a, b, c))
#                 stack.append((c-1, a, b))
#                 continue

#             memo[(a, b, c)] = memo[(memo[(a-1, b, c)], memo[(b-1, c, a)], memo[(c-1, a, b)])]
    
#     return memo[(a, b, c)]

# a, b, c = map(int, input().split())
# result = rec(a, b, c)
# print(result)

