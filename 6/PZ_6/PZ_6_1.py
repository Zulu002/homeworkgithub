import random

def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
            even_numbers.sort(reverse=True)
    print(len(even_numbers))
    return even_numbers


N=int(input(">> "))
a=[]
t=0
d=[]
while  t<N:
    a.append(random.randint(1,100))
    t+=1
print(a)
print(get_even_numbers(a))