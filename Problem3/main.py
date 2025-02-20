def horner_method(coefficients, x):
    #输入区
    k=0
    for i in coefficients:
        k=k*x+i

    return k

if __name__ == "__main__":
    # 读取输入：第一行为 x0，第二行为多项式系数（从高次到低次排列）
    x0 = float(input().strip())
    coefficients = list(map(float, input().split()))
    
    # 计算并输出结果
    print(horner_method(coefficients, x0))
