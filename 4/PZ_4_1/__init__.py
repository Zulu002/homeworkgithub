try:
    a= int(input("введие число А: "))
    b= int(input("введите число B оно больше А: "))
    sum=0
    if a<b: #проверяет больше ли значение b или нет
        while a<b:  #начинает цикл который будет идти пока a больше b
            sum+= a**2 # формула нахождения суммы всех квадратов
            a+=1
        print(sum)
    else:
        print('error')
except:
    print("error")
