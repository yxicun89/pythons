# import re
# S = input().split()
# flag=1

# # japanese_pattern = re.compile(r'[\u3040-\u30FF\u4E00-\u9FFF]')
# combined_pattern = re.compile(r'[\u3040-\u30FF\u4E00-\u9FFFa-zA-Z0-9]+')


# if not S[-1].isalnum():
#     flag=0
#     ans="invalid input"
# elif len(str(int(S[-1]))) != len(S[-1]) or int(S[-1]) > 10000000 or int(S[-1]) < 0:
#     flag=0
#     ans="invalid input"
# else:
#     n = int(S[-1])
#     ans=S[-1]

# current=0

# dictionary = {}
# for part in S[:-1]:
#     key, value = part.split(':',1)
#     if key in dictionary or key == '':
#         flag=0
#         ans="invalid input"
#     else:
#         dictionary[key] = value

# if len(dictionary) > 5 or len(dictionary) == 0:
#     flag=0
#     ans="invalid input"

# if flag == 1:
#     for key,value in dictionary.items():
#         print(not (bool(combined_pattern.search(value))))
#         if not (bool(combined_pattern.search(value))) or len(value) >= 50 or len(str(int(key))) != len(key) or current == int(key) or int(key) > 100 or int(key) < 0:
#             ans = "invalid input"
#             break
#         elif int(key) > current and n % int(key) == 0:
#             ans = value
#             current = int(key)

# print(ans)

#1:一 2:二 3:三 5:四 18:WhyJapanesePeople? 15



# N, Q = map(int, input().split())

# L_R = [list(map(int, input().split())) for _ in range(N)] #選手iのスコアの下限と上限
# query = [list(map(int, input().split())) for _ in range(Q) 

#クエリ1・・・ti=1なら選手xiのスコア範囲をli,riに変更
#クエリ2・・・ti=2なら上位xi人が予選通過できるとした場合,上位xi人が予選を通過できる場合,N人の選手のうち通過可能選手人数を出力
# def main():
#     import sys
#     input = sys.stdin.read
#     data = input().split()
    
#     idx = 0
    
#     N, Q = int(data[idx]), int(data[idx + 1])
#     idx += 2
    
#     ranges = []
#     for _ in range(N):
#         L, R = int(data[idx]), int(data[idx + 1])
#         idx += 2
#         ranges.append((L, R))
    
#     queries = []
#     for _ in range(Q):
#         query_type = int(data[idx])
#         if query_type == 1:
#             xi = int(data[idx + 1]) - 1
#             li = int(data[idx + 2])
#             ri = int(data[idx + 3])
#             queries.append((query_type, xi, li, ri))
#             idx += 4
#         elif query_type == 2:
#             xi = int(data[idx + 1])
#             queries.append((query_type, xi))
#             idx += 2
    
#     results = []
#     for query in queries:
#         if query[0] == 1:
#             _, xi, li, ri = query
#             ranges[xi] = (li, ri)
#         elif query[0] == 2:
#             _, xi = query
#             count = 0
#             for L, R in ranges:
#                 max_possible_positions = sum(1 for l, r in ranges if (r > L))
#                 if max_possible_positions >= xi:
#                     count += 1
#             results.append(str(count))
    
#     print("\n".join(results))

# if __name__ == "__main__":
#     main()



# def number_to_words(n):

#     units = ["", "thousand", "million", "billion"]
    
#     under_20 = [
#         "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
#         "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
#     ]
    
#     tens = [
#         "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
#     ]
    
#     def words(num):
#         if num < 20:
#             return under_20[num]
#         elif num < 100:
#             return tens[num // 10] + ('' if num % 10 == 0 else ' ' + under_20[num % 10])
#         elif num < 1000:
#             return under_20[num // 100] + " hundred" + ('' if num % 100 == 0 else ' ' + words(num % 100))
#         else:
#             for i, unit in enumerate(units):
#                 if num < 1000 ** (i + 1):
#                     return words(num // (1000 ** i)) + ' ' + units[i] + ('' if num % (1000 ** i) == 0 else ' ' + words(num % (1000 ** i)))
    
#     return words(n)

# def number_to_english(x):
#     if not x or (x[0] == '0' and len(x) > 1 and x[1] != '.'):
#         return -1
    
#     try:
#         if '.' in x:
#             integer_part, decimal_part = x.split('.')
#             integer_part_words = number_to_words(int(integer_part))
#             decimal_part_words = ' '.join([number_to_words(int(digit)) for digit in decimal_part])
#             result = f"{integer_part_words} point {decimal_part_words}"
#         else:
#             result = number_to_words(int(x))
    
#         return result.capitalize()
#     except Exception as e:
#         return -1


# x=input()
# print(number_to_english(x))


# or not x.replace('.', '', 1).isdigit() 

n=int(input())
c = [input().split() for _ in range(n)]

ans=[]

for i in range(len(c)):
    if c[i][0] == "n" or c[i][1] == "n":
        ans.append(i+1)

print(len(ans))
for i in ans:
    print(i)