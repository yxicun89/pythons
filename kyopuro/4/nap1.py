# item[[weight,price],[].....]
item = [[4, 60], [11, 73], [9, 33], [8, 62],[5, 97],
        [1, 26], [10, 89], [2, 65], [14, 97],[0, 74]]
name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','J']
capacity = 35

# i番目以降のパッキングの価値の最大値


def knapsack(i, capacity):
    if i >= len(item):
        return 0, []
    elif capacity - item[i][0] < 0.0:
        return knapsack(i+1, capacity)
    else:
        # i番目の品物を入れない場合
        p1, l1 = knapsack(i+1, capacity)

        # i番目の品物を入れる場合
        p2, l2 = knapsack(i+1, capacity - item[i][0])
        p2 += item[i][1]
        l2.append(i)
        if p1 > p2:
            return p1, l1
        else:
            return p2, l2


price, lst = knapsack(0, capacity)

print("TOTAL PRICE=", price)
print("ITEMS : {}".format(','.join(name[i] for i in lst)))