def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    h=0 #先頭のindex
    l=len(sorted_array)-1 #末尾のindex
    
    while h<l: #先頭、末尾の要素が中間値になるまでループ
        m=int((h+l)/2)
        if sorted_array[m]==target_number: #中間の値が探索対象の時
            return m
            break
        elif sorted_array[m]>target_number:#対象が中間の値より小さい時、末尾を中間の一つ前の要素にする。
            l=m-1 
        else:#対象が中間の値より大きい時、先頭を中間の次の要素にする
            h=m+1 
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
