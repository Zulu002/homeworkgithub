try:
    nv = 1000
    mv = float(input("введите процент вклада >> "))
    K = 1
    if mv > 0 and mv < 25:
        while nv <= 1100:
            K+=1
            nv=nv+nv*mv/100
        print(K, "мес ", nv,"конечный вклад")
    else:
        print('error')
except:
    print('error')