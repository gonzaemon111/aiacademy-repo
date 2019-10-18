# coding: UTF-8

# 1) シングルクオテーション
str1 = 'Hello World'

# 2) ダブルクオテーション
str2 = "Hello World"

# 3) トリプル・ダブルクオテーション
str3 = """Hello World
Hello Python"""


print(str1)
print(str2)
print(str3)

print("------------")

# 結合
a = "hello " # 結合後、見やすくするために、最後に半角スペースを入れています。
b = "world"
print(a + b) # hello world

print("------------")

# 反復
a = "hello"
print(a * 3) # hellohellohello