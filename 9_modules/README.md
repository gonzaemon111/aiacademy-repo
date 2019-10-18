# Moduleのインポート

import文の単純な使い方は次のようになります。
`import 読み込みたいモジュール`
読み込みたいモジュールの部分は、他のPythonファイルのファイル名から拡張子の.pyを取り除いたものです。
例えば、sysモジュールを読み込みたい時は次のようにします。
(sysモジュールは、Pythonをインストールした段階で利用できるモジュールの1つです。これを標準モジュールと呼び、他にもosモジュールなど様々あります。)

## `from`と`import`

`from ファイル名(モジュール名) import *`でファイル名の指定なしに呼び出しが可能になります。

モジュールの関数などを利用する際に、モジュール名.の記述を省略して関数名だけで使用したい場合は以下になります。
`from モジュール名 import 関数名, 関数名, ...`

```python
from math import cos, sin, tan
cos(1)
```

また、名前を指定せずにモジュール内のすべてのメンバ(関数、定数、クラスなどのこと)をインポートする場合は、以下のように指定します。

```python
# from モジュール名 import *
from math import *
cos(1)
sin(1)
```

fortune.pyでrandomをサンプルでimportしているのは関数内ですが、関数外でもインポートできます。

## 別名でのモジュールのインポート

```python=main.py
import fortune

result = fortune.get_fortune()
print("今日の運勢は... ", result)
```

import fortuneと記述していましたが、asを用いることで、別名をつけることができます。
以下が別名をつけたサンプルです。

```python
import fortune as ft

result = ft.get_fortune()
print("今日の運勢は... ", result)
```

別名をつけたことでft.get_fortune()と呼び出すことが出来るようになりました。

## 必要なものだけをimportする

*で全てインポートしましたが、必要な部品だけもインポートできます。

```python
from fortune import get_fortune

result = get_fortune()
print("今日の運勢は... ", result)
```

また別名をつけ、かつget_fortuneだけインポートするサンプルです。

```python
from fortune import get_fortune as gf

result = gf()
print("今日の運勢は... ", result)
```