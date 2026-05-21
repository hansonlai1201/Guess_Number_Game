import sys
import random

sys.stdout.reconfigure(encoding='utf-8')

def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    # Step 1: 把 n-1 個盤子從 source 搬到 auxiliary
    hanoi(n - 1, source, auxiliary, target)

    # Step 2: 把第 n 個盤子搬到 target
    print(f"Move disk {n} from {source} to {target}")

    # Step 3: 把 n-1 個盤子從 auxiliary 搬到 target
    hanoi(n - 1, auxiliary, target, source)


# 測試
n = 3
hanoi(n, 'A', 'C', 'B')