# coding: UTF-8

print("Hello" + "World") # +により文字列同士を連結
name = "Tom"
print("My name is " + name)

age = 24
# 以下は、データ型の異なる文字列型と数値型を連結してエラーになっているプログラムです。

"""
print("My name is " + name + "My age is " + age) # この行はエラーになります
# TypeError: Can't convert 'int' object to str implicitly
"""

print("My name is " + name + "My age is " + str(age)) # str()メソッドを使い、cast(型変換)をする

print("------------")


name = "Tom"
age = 24
print("My name is " + name + "My age is " + str(age))

"""
先ほど、数値型を文字列型に変換しましたが、反対に文字列型を数値型に変換することもできます。
その場合「int」を用います。
"""

string_price = "1000"
price = 500

total_price = int(string_price) + price
print(total_price) # 1500

