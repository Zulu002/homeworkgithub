def AddLeftDigit():
    D = int(input("введите число D >>"))
    K = int(input("введите число B >>"))
    A=""
    a=1
    while a<2:
        if D<=9 and D>0:
            str(print(K,D,A, sep=""))
            A = int(input("введите число D2 >>"))
            a+=1
        elif a>=2:
            break
        else:
            print("error")
    str(print(K, D, A, sep=""))


AddLeftDigit()