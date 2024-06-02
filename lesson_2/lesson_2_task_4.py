
def fizz_buzz(n):
    
    if  n % 3 == 0 and n % 5 == 0 :
        print ("FizzBuzz")
    elif n % 3 == 0 :
        print ("Fizz")
    elif n % 5 == 0 :
        print ("Buzz")
    else:
        print (str(n))


max = input("Введите максимальное число : ")

i = 1
while i < int(max):
    fizz_buzz(i)
    i=i+1