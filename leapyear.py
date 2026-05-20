def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def check_leap_year():
    while True:
        try:
            year = int(input("請輸入一個年份: "))
            if year < 1900 or year > 2100:
                print("請輸入1900年至2100年之間的年份！")
                continue
            if is_leap_year(year):
                print(f"{year} 是閏年！")
            else:
                print(f"{year} 不是閏年。")
            break
        except ValueError:
            print("請輸入一個有效的年份！")

if __name__ == "__main__":
    check_leap_year()