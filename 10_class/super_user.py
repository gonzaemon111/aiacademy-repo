# coding: UTF-8

from user import User

class SuperUser(User): # ユーザークラスを継承するには、()の中にUserクラスを書けばoKです。
  def __init__(self, name, age):
    # super()を使うことで親クラスのメソッドを呼び出すことができます。
    super().__init__(name) # こクラスから親クラスのコンストラクタを呼び出す
    self.age = age

  # メソッドのオーバーライド
  def hello(self):
    print("SuperHello" + self.name)
    """
    またこクラスのメソッドの中で、例えばオーバライドした
    メソッド内で、super()を使うことで親クラスUserのメソッドを呼び出すこともできます。
    """
    super().hello()