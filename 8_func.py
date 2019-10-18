# coding: UTF-8

# hello関数の定義
def hello():
    print("hello!")

# 関数の呼び出し(実行)
hello() # hello! が出力される


# 何も処理のないtest関数を定義
def test():
    pass

test()

print("------------")

def say_hello(name):
    print("こんにちは" + str(name) + "さん")

say_hello("山田") # こんにちは山田さん

print("------------")

def adder1(a, b):
    print(a+b)

def adder2(a, b):
    return a + b

adder1(2, 4)
sum = adder2(2, 4)
print(sum)

print("------------")

def power(x):
    return x*x

def absolute(x):
    if (x < 0):
        return -x
    else:
        return x

print(power(10)) # 100
print(absolute(-10)) # 10


print("------------")
# 引数のデフォルト値

def func(a, b=5):
    print(a)
    print(b)

func(10,15) # 10と15が出力される
func(3) # 3と5が出力される