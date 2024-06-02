import math

def square(length):
    temp = math.ceil(length)*math.ceil(length)
    return temp


len= float(input("Введите длину стороны квадрата: "))
tt=square(len)
print ("Площадь квадрата = " + str(tt))