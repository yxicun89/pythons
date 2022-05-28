def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    left=[] 
    right=[] 
    count=0 #基準値の数

    for x in array:
        #基準値より小さい要素をleftに格納
        if x < pivot:
            left.append(x)
        #基準値より大きい要素をrightに格納
        elif x > pivot:
            right.append(x)
        #基準値の時は、何回基準値が現れたかカウントする。
        else:
            count+=1
    #要素数が1になるまで繰り返す。
    if len(left)!=0:
        left = sort(left)
    if len(right)!=0:
        right = sort(right)
    #基準値をリストに加えることに注意する、
    return left + [pivot]*count + right
    # ここまで記述

if __name__ == '__main__':
    main()
