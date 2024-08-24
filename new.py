def equation(a, b, c, d, e):
    return (a * 3) + (b / 4) - (c + 3) - (d - 2) + (e + 4) - 24

def equation_derivative_a():
    return 3

def equation_derivative_b():
    return 1 / 4

def equation_derivative_c(d, e):
    return -(d - 2) / (e + 4)

def equation_derivative_d(c, e):
    return (c + 3) / (e + 4)

def equation_derivative_e(c, d, e):
    return -(c + 3) * (d - 2) / (e + 4)**2

def newton_method():
    # 初期値を設定
    a = 1
    b = 1
    c = 1
    d = 1
    e = 1

    # 収束判定の閾値
    epsilon = 1e-6

    # 収束しない場合の上限反復回数
    max_iterations = 1000

    # 反復により方程式を解く
    for i in range(max_iterations):
        f = equation(a, b, c, d, e)
        f_prime_a = equation_derivative_a()
        f_prime_b = equation_derivative_b()
        f_prime_c = equation_derivative_c(d, e)
        f_prime_d = equation_derivative_d(c, e)
        f_prime_e = equation_derivative_e(c, d, e)

        determinant = f_prime_a * ((f_prime_e * f_prime_d) - (f_prime_c * f_prime_e)) - \
                      f_prime_b * ((f_prime_e * f_prime_d) - (f_prime_c * f_prime_d))

        # ニュートン法の更新式
        a -= (f_prime_a * ((f * f_prime_e) - (f_prime_e * f))) / determinant
        b -= (f_prime_b * ((f * f_prime_d) - (f_prime_d * f))) / determinant
        c -= (f_prime_c * ((f * f_prime_e) - (f_prime_e * f))) / determinant
        d -= (f_prime_d * ((f * f_prime_c) - (f_prime_c * f))) / determinant
        e -= (f_prime_e * ((f * f_prime_c) - (f_prime_c * f))) / determinant

        # 収束判定
        if abs(f) < epsilon:
            return a, b, c, d, e

    # 収束しなかった場合、Noneを返す
    return None, None, None, None, None

def main():
    a, b, c, d, e = newton_method()

    if a is not None and b is not None and c is not None and d is not None and e is not None:
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)
    else:
        print("方程式の解を見つけることができませんでした。")

if __name__ == "__main__":
    main()


# from sympy import symbols, Eq, solve

# def newton_method(expression, variables):
#     # 初期値を設定
#     initial_values = {var: 1 for var in variables}

#     # 収束判定の閾値
#     epsilon = 1e-6

#     # 収束しない場合の上限反復回数
#     max_iterations = 1000

#     # sympy のシンボルを作成
#     sym_vars = symbols(variables)

#     # 数式をパース
#     parsed_expression = eval(expression)

#     # parsed_expression = sympify(expression)

#     # 反復により方程式を解く
#     for i in range(max_iterations):
#         # 数式を計算
#         f = parsed_expression.subs(initial_values)

#         # 微分を計算
#         f_prime = [parsed_expression.diff(var) for var in sym_vars]

#         # 行列の形式で方程式を解く
#         determinant = f_prime.jacobian(sym_vars).det()

#         # ニュートン法の更新式
#         updates = solve([Eq(var, val - f / f_prime_val) for var, val, f_prime_val in zip(sym_vars, initial_values.values(), f_prime)])
#         initial_values.update(updates)

#         # 収束判定
#         if abs(f) < epsilon:
#             return initial_values

#     # 収束しなかった場合、Noneを返す
#     return None

# def main():
#     try:
#         # 数式の入力を受け取る
#         expression = input("数式を入力してください: ")
#         variables = input("変数をカンマ区切りで入力してください (例: a,b,c,d,e): ").split(',')

#         # ニュートン法を実行
#         result = newton_method(expression, variables)

#         if result is not None:
#             print("方程式の解:")
#             for var, val in result.items():
#                 print(f"{var} = {val}")
#         else:
#             print("方程式の解を見つけることができませんでした。")

#     except Exception as e:
#         print("エラー:", e)

# if __name__ == "__main__":
#     main()