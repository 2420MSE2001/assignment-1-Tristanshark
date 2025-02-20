# main.py

def calculate_sum():
    k=0
    i=0
    while i<=50:
        k=k+i
        i+=1
    return k


if __name__ == "__main__":
    result = calculate_sum()
    print(f"1+2+...+50的和是：{result}")
