import random
import sys

sys.stdout.reconfigure(encoding='utf-8')

def guess_number_game():
    number_to_guess = int(random.random() * 100) + 1
    guess = -1
    attempts = 0
    max_attempts = 10

    print("歡迎來到猜數字遊戲！")
    print("你有 10 次機會猜中數字。")

    while guess != number_to_guess and attempts < max_attempts:
        try:
            guess = int(input("\n請猜一個 1~100 的數字: "))

            if guess < 1 or guess > 100:
                print("請輸入 1~100 範圍內")
                continue

            if guess < number_to_guess:
                print("太小了！")
            elif guess > number_to_guess:
                print("太大了！")
            else:
                print("恭喜你猜對了！")
                print(f"你總共猜了 {attempts} 次。")

            attempts += 1

        except ValueError:
            print("請輸入一個『1~100的整數』！")

    # 迴圈結束後再判斷是否失敗
    if guess != number_to_guess:
        print(f"很遺憾，你沒有猜中。正確的數字是 {number_to_guess}。")

if __name__ == "__main__":
    guess_number_game()
