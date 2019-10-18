# coding: UTF-8

class User:
  def __init__(self, name):
    self.name = name
    print("コンストラクタが呼ばれました！")
  def hello(self):
    print("Hello " + self.name)