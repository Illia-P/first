#4 числа
a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))
d = int(input("Enter a number"))
s = (a + b) / (c + d)
print(s)


#триугольник
a = int((input("Введите первою сторону триугольника ")))
b = int((input("Введите вторую сторону триугольника ")))
c = int((input("Введите третию сторону триугольника ")))
if c > a + b and a > b + c and b > a + c:
    print("Такой триугольник сучествует")
else:
    print("Такой триугольник не сучествует")


#система координат
    x = int((input("Введите X ")))
    y = int((input("Введите Y ")))
    if x > 0 and y > 0:
        print("Точка", (x, y), "находиться в І четверти")
    elif x >= 0 and y <= 0:
        print("Точка", (x, y), "находиться в ІV четверти")
    elif x <= 0 and y <= 0:
        print("Точка", (x, y), "находиться в III четверти")
    elif x == 0 and y == 0:
        print("Точка", (x, y), "находиться в начале системи координат")
    else:
        print("Точка", (x, y), "находиться в ІI четверти")

#Calculator
a = int((input("Введите первое число ")))
operation = (input("Введите знак на выбор: +, -, *, / "))
b = int((input("Введите второе число ")))

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/" and b != 0:
    print(a / b)
elif operation == "/" and b == 0:
    print("Error")
else:
    print("Выберете + либо - либо / либо *")


#3 znachenia
znachenie_1 = input("Введите значение ")
znachenie_2 = input("Введите значение ")
znachenie_3 = input("Введите значение ")
if int(znachenie_1) < int(znachenie_2) < int(znachenie_3):
    print(znachenie_1,  znachenie_3)
elif int(znachenie_1) < int(znachenie_3) < int(znachenie_2):
    print(znachenie_1,  znachenie_2)
elif int(znachenie_2) < int(znachenie_1) < int(znachenie_3):
    print(znachenie_2,  znachenie_3)
elif int(znachenie_3) < int(znachenie_2) < int(znachenie_1):
    print(znachenie_3, znachenie_1)
elif int(znachenie_3) < int(znachenie_1) < int(znachenie_2):
    print(znachenie_3, znachenie_2)
elif int(znachenie_2) < int(znachenie_3) < int(znachenie_1):
    print(znachenie_2, znachenie_1)
else:
    print(znachenie_1 , znachenie_2 , znachenie_3)


