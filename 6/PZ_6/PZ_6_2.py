import random
a = [random.randint(0, 20) for el in range(10)]
print(a)
result=0
count=0
for j in range(len(a)-2):
    if a[j+2] > a[j+1] > a[j]:
        count+=1
    elif count>=1 and a[j+1] > a[j+2]:
        result+=1
        count=0
if a[-1] > a[-2] > a[-3]:
    result+=1
print(result)