def calculate_polynomial(n: int, x: int, xi_list: list) -> int:
    k=1
    for i in range(n):
        k=k*(x-xi_list[i])
    return k
    """
    计算多项式展开式 (x - x₁)(x - x₂)...(x - xn) 的值

    
    参数:
    n -- 整数，表示xi的数量

    x -- 整数

    xi_list -- 包含n个整数的列表

    
    返回:
    展开式的计算结果

    """

        
    return result

if __name__ == "__main__":
    n = int(input())
    x = int(input())
    xi_list = list(map(int, input().split()))
    print(calculate_polynomial(n, x, xi_list))
