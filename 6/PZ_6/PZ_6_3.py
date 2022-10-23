import random
N = int(input("введите число N >> "))
a=[]
t=0
b=[]
while  t<N:
    a.append(random.randint(1,100))
    t+=1
for i in a:
    b.append(i/sum(a))
print(a)
print(b)

# import random
# N = int(input("введите число N >> "))
# a=[]
# t=0
# b=[]
# while  t<N:
#     a.append(random.randint(1,100))
#     t+=1
# for i in a:
#     b.append(i/N)
# print(a)
# print(b)