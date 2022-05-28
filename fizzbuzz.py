for num in range(1, 101):
    string = ''

    # ここから記述
    if num%15==0: #まず15の倍数を考慮。
        string+="FizzBuzz"
    elif num%5==0: #次に5の倍数を考慮。
        string+="Buzz"
    elif num%3==0: #次に3の倍数を考慮。
        string+="Fizz"
    else: #最後に上記以外の考慮.
        string+=str(num) #intをstrに変換。
    # ここまで記述

    print(string)