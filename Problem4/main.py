# main.py

def left_side(x, num_terms):
    """
    计算方程左侧前 num_terms 项的和。
    """
    result=0
    for i in range(num_terms):
        k=2**(i)
        result=result+((k)*x**(k-1)-2*k*x**(2*k-1))/((1-x**k)+x**(2*k))

    return result

def right_side(x):
    result=(1+2*x)/(1+x+x**2)
    """
    计算方程右侧的固定值。
    """
    return result

def find_num_terms(x, tolerance=1e-6):
    t=right_side(x)
    n=1
    while t>=tolerance:
        t=right_side(x)-left_side(x, n)
        n+=1
    num_terms=n
        
    """
    寻找满足左侧与右侧差异小于容差的最小项数。
    """



    return num_terms

if __name__ == "__main__":
    x = 0.25  # 题目给定的 x 值
    num_terms = find_num_terms(x)
    print(f"所需最小项数: {num_terms}")
