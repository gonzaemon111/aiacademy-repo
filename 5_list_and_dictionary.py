# coding: UTF-8

# list型

li = []
li.append("python")
print(li) # ['python']
li.append("php")
print(li) # ['python', 'php']

# dictionary型

# 辞書型(ディクショナリー型）はKeyとValueのペアを保持するデータ型です。

profile = {"name": "tani", "email": "kazunori-t@cyberbra.in" }
print(profile["name"]) # tani

# 新しく要素を追加
profile["gender"] = "male"

# 新しく要素を追加した辞書型(profile)を出力
print(profile)