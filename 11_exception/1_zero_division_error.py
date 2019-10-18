print("何か数字を入力してください！")
i = input()
input_num = int(i) 

try:
    result = 5 / input_num
    print(result)
except ZeroDivisionError:
    print('ZeroDivisionError!!')