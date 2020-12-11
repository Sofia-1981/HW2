# num1=int(input("Введите первое число "))
# num2=int(input('Введите второе число '))
# if num1 % 2 == 0:
#     print(num2)
# else:
#     print(num1)
#
#
# num1=int(input("Введите первое число "))
# num2=int(input('Введите второе число '))
# num3=int(input("Введите третье число "))
# if num2<num1<num3 or num3<num1<num2:
#     print(num1)
# elif num1<num2<num3 or num3<num2<num1:
#     print(num2)
# elif num1<num3<num2 or num2<num3<num1:
#     print(num3)
# else:
#     print("Введены недопустимые данные: введите не равные числа")
#
#
# num1=int(input("Введите первое целое число "))
# num2=int(input("Введите второе целое число "))
# if num1%num2==0:
#     q=num1//num2
#     print("Первое число делится нацело на второе число, частное от деления равно", q)
# else:
#     print("Первое число не делится нацело на второе число, частное от деления равно", num1//num2, "остаток от деления равен", num1%num2)
#
#
# x=float(input("Введите первое число "))
# y=float(input("Введите второе число "))
# if x > 0 and y > 0:
#     print('Точка принадлежит первой четверти координатной плоскости')
# elif x > 0 and y < 0:
#     print('Точка принадлежит четвертой четверти координатной плоскости')
# elif x < 0 and y < 0:
#     print('Точка принадлежит третьей четверти координатной плоскости')
# elif x <0 and y > 0:
#     print('Точка принадлежит второй четверти координатной плоскости')
#
#
# list1=[i for i in range(0,101)]
# list2=[]
# for i in list1:
#     if i % 5 == 0:
#         list2.append(i)
# print(list2)
#
#
# list1=[i**3 for i in range(3,13)]
# print(list1)

# list1=[1,2,"поле", 4,10]
# list1.append(list1[0])
# list1.remove(list1[0])
# list1.insert(0,10)
# list1.pop(4)
# print(list1)
#
#
# list1=["1","2","3","4"]
# list2=[]
# if len(list1)==0:
#     print("Список пуст")
# else:
#     for i in range(len(list1)):
#         if i%2==0 or i==0:
#             list2.append(list1[i]*2)
#     print(list2)
#
#
# list1=[1,-2,-3,4]
# listsum=sum(list1)
# listmin=min(list1)
# listmax=max(list1)
# print(listsum, listmin, listmax)# не дает вставить запятые или слова
# for i in list1:
#     if i<0:
#         print(i, end=" ")
#
#
# list1=["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
# day = 'среда'
# for i in list1:
#     if i == day:
#         print("\033[3m\033[30m\033[45m {}". format(i))
#     else:
#         print("\033[0m {}". format(i), end=' ')
#
#
# a=int(input("введитe a "))
# b=int(input("введите b "))
# c=int(input("введите c "))
# # a*x**2+b*x+c==0
# D=b**2-4*a*c
# if D>0:
#     x1 = (-b + D ** 1 / 2)
#     x2=(-b - D ** 1 / 2)
#     print(x1, x2)
# elif D==0:
#     x1=x2=-b/2*a
#     print(x1)
# elif D<0:
#     print("решений нет")