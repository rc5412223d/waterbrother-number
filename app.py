print ("水哥是gay")
print ("水哥牌計算機")
ask = input("請輸入一個數字: ")
a = int(ask)
ask2 = input("請輸入另一個數字: ")
b = int(ask2)
print ("請選擇運算符號: +, -, *, /")
ask3 = input("請輸入運算符號: ")
print ("計算結果為: ")
if ask3 == "+":
    print (a + b)
elif ask3 == "-":
    print (a - b)
elif ask3 == "*":
    print (a * b)
elif ask3 == "/":
    print (a / b)