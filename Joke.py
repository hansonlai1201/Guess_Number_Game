import random
import sys

sys.stdout.reconfigure(encoding='utf-8')

person = ["Janson", "Tom"]
name = random.choice(person)
print(f"{name} 和外國人吵架了！")
print(f"{name} 你算哪根蔥?")
print("外國人: 我是洋蔥!")