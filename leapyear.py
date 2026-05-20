def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def check_leap_year():
    try:
        year = int(input("請輸入一個年份: "))
        if is_leap_year(year):
            print(f"{year} 是閏年！")
        else:
            print(f"{year} 不是閏年。")
    except ValueError:
        print("請輸入一個有效的年份！")

if __name__ == "__main__":
    check_leap_year()