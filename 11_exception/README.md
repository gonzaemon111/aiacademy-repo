# 例外処理

**例外処理とは、プログラムがある処理を実行している途中で、なんらかの異常が発生した場合に、現在の処理を中断し、別の処理を行うことです。**
**例外処理を記述することで、予期していなかったエラーに対応できるプログラムを書くことができます。**

予期していないエラーとはなんでしょうか？
実は、エラーは大きく分けて**2**種類あります。

- 構文エラー(Syntax Error)
- 例外(Exception)

ここで、構文エラーに関しては、省く


例外処理を記述することで、予期せぬエラーに対応できるプログラムを書くことができます。
予期せぬエラーというのは、つまり想定外の事象によりプログラムが動作しなくなってしまうことです。
これを例外と呼びます。
例外には、IndexErrorやTypeErrorやNameErrorやZeroDivisionErrorなどがあります。
これらの例外エラーは構文エラーとは違って致命的ではないので、例外処理を記述していればプログラムは実行し続けることが出来ます。

### 例外処理の構文
```python
# 例外処理の構文

try:
    例外が発生しそうなプログラム
except:
    例外が起きた時の処理
```

サンプルプログラム！
```python
try:
    # バグ1
    i = input()
    input_num = int(i)
    result = 5 / input_num # 5 / 2 => 2.05
    print(result)

    # バグ2
    a = "a"
    b = 5
    print(a+b)

except (TypeError, ZeroDivisionError, KeyError) as e:
    print(type(e))
```

exceptには、OSErrorやValueError,ZeroDivisionError, NameError, TypeErrorなど例外を記述することができます。

### 複数の例外を捕捉する

例外は、複数のexcept節を用いて発生した例外に応じた処理をすることもできます。
また、上記のサンプルのように、()に複数の種類を1か所で捕捉して書くこともできます。

```python
try:
    print('処理')
except KeyError as e:
    print('KeyError')
except ZeroDivisionError as e:
    print('ZeroDivisionError')
except:
    print('Error')
```


#### else / finally

forやwhile文同様に、tryブロックが例外を発生せずに最後まで処理が進んだ場合、elseブロックが実行されます。
また、tryブロックが例外を発生しなくても、実行されるfinallyも定義できます。
finallyは「例外の発生に関係なく最後に処理を実行します。
また、finallyは例外が発生しても例外処理の後に必ず実行されます。

```python
try:
    print('処理')
except KeyError as e:
    print('KeyError')
except ZeroDivisionError as e:
    print('ZeroDivisionError')
else:
    print('問題なく処理が実行されました')
finally:
    print('処理2')
```

