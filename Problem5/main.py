# main.py

def calculate_S(a0, a1, x0, x1, x):
    #输入区
    s0=a0
    s1=a1
    s0=s0*(x-x1)/(x0-x1)
    s1=s1*(x-x0)/(x1-x0)
    S=s0+s1

    
    return S

if __name__ == "__main__":
    print("=== 线性插值计算器 ===")
    try:
        # 获取用户输入

        a0 = float(input("请输入已知点1的函数值 a0: "))
        x0 = float(input("请输入已知点1的x坐标 x0: "))
        a1 = float(input("请输入已知点2的函数值 a1: "))
        x1 = float(input("请输入已知点2的x坐标 x1: "))
        x  = float(input("请输入需要插值的x坐标 x : "))
        
        # 计算并输出结果

        S = calculate_S(a0, a1, x0, x1, x)
        print(f"\n插值结果 S({x}) = {S:.4f}")
        
    except ValueError:
        print("错误：请输入有效的数字！")
    except ZeroDivisionError:
        print("错误：x0 和 x1 不能相同，否则会导致除以零！")
