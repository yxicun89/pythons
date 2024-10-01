# N,M,D=map(int,input().split())
# A=list(input().split())
# H=list(map(int,input().split()))
# Q=int(input())

# for _ in range(Q):
#     kind,date=input().split()
#     if kind == "ORDER":
#         b,c,k=map(int,input().split())
#         for _ in range(k):
#             x_y = list(map(int,input().split()))

#     elif kind == "CANCEL":

#     else:


# from collections import defaultdict, deque
# import datetime

# class OrderSystem:
#     def __init__(self, N, M, D, A, H):
#         self.N = N
#         self.M = M
#         self.D = D
#         self.A = A
#         self.H = H
#         self.orders = {}
#         self.shipments = defaultdict(int)
#         self.pending_orders = deque()
        
#     def process_query(self, query):
#         parts = query.split()
#         if parts[0] == "ORDER":
#             self.order(parts)
#         elif parts[0] == "CANCEL":
#             self.cancel(parts)
#         elif parts[0] == "SHIP":
#             self.ship(parts)
            
#     def order(self, parts):
#         T = parts[1]
#         B = parts[2]
#         C = parts[3]
#         K = int(parts[4])
#         items = [(parts[5 + 2*i], int(parts[6 + 2*i])) for i in range(K)]
        
#         C_date = datetime.datetime.strptime(C, "%Y-%m-%d")
#         if self.H[C_date.weekday()] == 0:
#             print(f"{T} Ordered {B} Error: shipment not possible on this day")
#             return
        
#         for X, Y in items:
#             if self.shipments[(C, X)] + Y > self.M:
#                 print(f"{T} Ordered {B} Error: the number of available shipments has been exceeded")
#                 return
        
#         for X, Y in items:
#             self.shipments[(C, X)] += Y
        
#         self.orders[B] = {"T": T, "C": C, "items": items}
#         self.pending_orders.append(B)
#         print(f"{T} Ordered {B}")
    
#     def cancel(self, parts):
#         T = parts[1]
#         B = parts[2]
        
#         if B in self.orders:
#             order = self.orders.pop(B)
#             C = order["C"]
#             items = order["items"]
#             for X, Y in items:
#                 self.shipments[(C, X)] -= Y
#             print(f"{T} Canceled {B}")
#         else:
#             print(f"{T} Canceled {B} Error: order does not exist")
    
#     def ship(self, parts):
#         T = parts[1]
#         ship_date = datetime.datetime.strptime(T, "%Y-%m-%dT%H:%M:%S")
        
#         shipped_orders = []
#         for B in list(self.pending_orders):
#             order = self.orders[B]
#             order_date = datetime.datetime.strptime(order["C"], "%Y-%m-%d")
#             if order_date <= ship_date:
#                 shipped_orders.append(B)
#                 self.pending_orders.remove(B)
        
#         if shipped_orders:
#             print(f"{T} Shipped {len(shipped_orders)} Orders")
#             for B in shipped_orders:
#                 print(B)
#         else:
#             print(f"{T} Shipped 0 Orders")

# def main():
#     import sys
#     input = sys.stdin.read()
#     data = input.splitlines()
    
#     # 初期設定の読み取り
#     N, M, D = map(int, data[0].split())
#     A = data[1].split()
#     H = list(map(int, data[2].split()))
#     Q = int(data[3])
    
#     order_system = OrderSystem(N, M, D, A, H)
    
#     # クエリの処理
#     index = 4
#     while index < len(data):
#         if data[index].startswith("ORDER"):
#             query = data[index] + " " + data[index+1] + " " + data[index+2]
#             index += 3
#             order_system.process_query(query)
#         elif data[index].startswith("CANCEL"):
#             query = data[index] + " " + data[index+1]
#             index += 2
#             order_system.process_query(query)
#         elif data[index].startswith("SHIP"):
#             query = data[index]
#             index += 1
#             order_system.process_query(query)
    
#     sys.exit(0)

# if __name__ == "__main__":
#     main()

import sys
input = sys.stdin.read
data = input().splitlines()
    
N, M, D = map(int, data[0].split())
A = data[1].split()
H = list(map(int, data[2].split()))
Q = int(data[3])

parts=data[4].split
# N種類の商品,商品番号A
# 操作は発送と取り消しの2つ
# D日後までの範囲で商品の発送日を指定する。注文番号で識別,複数注文するかもしれない

# 発送可能数 M ・・・1日最大 M 個発送できる
# 1種類でも超えたら注文を受理しない
# H は各曜日の初期状態,0なら発送可能数0,1なら発送可能数 M

# クエリは注文と日時を受け取る

# ORDERなら
# 注文番号B,発送の日付C,注文する商品の種類数K,注文する商品の種類X_K,商品の個数Y_Kを入力
# T Ordered Bを出力する,受理しないときは, T Ordered B Error: the number of available shipments has been exceeded.


# CANCELなら注文番号Bを入力(発注済みはない)
# T Canceled Bを出力


# SHIPなら,
# T shipped E Oeders
# B_1,B_2,....,B_Nを出力(注文番号をためていく)



# 3 10 10
# AAAAA BBBBB CCCCC
# 1 1 1 1 1 1 1
# 5

# ORDER 2022-01-01T01:00:00
# AAAAAAAAAA 2022-01-02 1
# AAAAA 6

# ORDER 2022-01-01T02:00:00
# BBBBBBBBBB 2022-01-02 1
# AAAAA 5

# ORDER 2022-01-01T03:00:00
# CCCCCCCCCC 2022-01-03 1
# BBBBB 1

# SHIP 2022-01-02T00:00:00

# CANCEL 2022-01-02T01:00:00
# CCCCCCCCCC

# s=list(input().split())

# ans=""

# for i in range(len(s)):
#     if i != len(s) and "Postcode:" in s[i]:
#         ans= ans + s[i+1]

# if ans == '' or '-' not in ans or ' ' in ans:
#     ans = "FORMAT ERROR"
# else:
#     ans=ans.replace('-','')
#     ans = ''.join(filter(str.isdigit,ans))

# if len(ans) == 7:
#     print(ans)
# else:
#     print("FORMAT ERROR")