def AddLeftDigit(): #вводим собственную функцию
    D=int(input("введите число D >> "))
    K=int(input("введите число K >> "))
    A=""
    a=1
    while a<2: #создаём цикл
        if D<=9 and D>0: #проверяем подходит ли нам число
            str(print(K,D,A, sep="")) #выводим данные как сказано в задаче
            A=int(input("введите число D2 >> ")) #просим ввести 3 число
            a+=1 #плюс 1 к значению a
            str(print(K, D, A, sep=""))  # выводим последнее число
        else:
            print("error")
            break

AddLeftDigit() #выводим функцию
