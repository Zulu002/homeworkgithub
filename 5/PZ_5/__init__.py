def star(a):
    b=1
    c="*"
    while b<=a:
        print(c)
        c+="*"
        b+=1

a=int(input("введите число >>"))

star(a)