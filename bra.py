def EOP(n): #n文字数の正しい()列を返す
    for i in range(1 << n):
        eop = []
        counter = 0
        for j in range(n):
            # 0("("), 1(")")
            
            if i & (1 << j):
                eop.append("(")
                counter += 1
            else:
                eop.append(")")
                counter -= 1
            if counter < 0:
                break
        
        if counter == 0:
            for k in range(n):
                print(eop[k], end="")
            print()

EOP(int(input()))