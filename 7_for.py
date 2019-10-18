# coding: UTF-8

"""
for ループ内変数 in リスト名:
    実行する処理
"""

for i in ["apple", "banana", "melon"]:
  print(i)

print("------------")

for i in range(10):
  print(i)

print("------------")

for i in range(10):
  if i == 3:
      break
  print(i) # 0 1 2を出力

print("------------")

data = [1, 2, 3, 4, 5, "f"]
for x in data:
    if x == 'f':
        print('found')
        break
else:
    print('not found') # このサンプルの場合elseの処理は実行されない！

print("------------")


for char in "hello":
    print(char)

print("------------")

# リストの要素を順に処理しつつ、インデックス番号も知りたい場合があるかと思います。 その場合、enumerate()を使います。

for index, name in enumerate(["apple", "banana", "melon"]):
    print(index, name)

print("------------")

print(list(range(101)))

print("------------")

data = {"tani": 21, "kazu": 22, "python": 100}
for key, value in data.items():
     print("key: {} value: {}".format(key, value))

print("------------")
print("While文")

# nが10になるまで繰り返し
n = 0
while n < 10:
    print(n)
    n += 1 # +1するのを忘れずに。


print("------------")

print("リスト内包表記(List Comprehensions)")
# リスト内包表記(List Comprehensions)
result = [x**2 for x in range(1,11)]
print(result) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 通常のループでは次のようになります。
result = []
for i in range(1,11):
    result.append(i**2)

print(result)

# 標準入力

print("名前を入力してください")
name = input()
print("あなたの名前は"+name+"です")