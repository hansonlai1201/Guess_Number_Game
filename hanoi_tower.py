import sys

sys.stdout.reconfigure(encoding='utf-8')

# 加上 depth 參數，預設為 0
def hanoi_debug(n, source, target, auxiliary, depth=0):
    indent = "    " * depth  # 根據層數產生縮排空格

    print(f"{indent}▶️ 進入第 {depth} 層: 準備把 {n} 個盤子從 {source} 搬到 {target}")

    if n == 1:
        print(f"{indent}  📢 [動作] Move disk 1 from {source} to {target}")
        print(f"{indent}↩️ 執行 return：結束第 {depth} 層，回到上一層")
        return

    # Step 1: 把 n-1 個盤子從 source 搬到 auxiliary
    hanoi_debug(n - 1, source, auxiliary, target, depth + 1)

    # Step 2: 把第 n 個盤子搬到 target
    print(f"{indent}  📢 [動作] Move disk {n} from {source} to {target}")

    # Step 3: 把 n-1 個盤子從 auxiliary 搬到 target
    hanoi_debug(n - 1, auxiliary, target, source, depth + 1)

    print(f"{indent}↩️ 函式執行完畢：自動結束第 {depth} 層，回到上一層")

# 測試 3 個盤子
hanoi_debug(3, 'A', 'C', 'B')