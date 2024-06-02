
def month_to_season(n):
    print(n)
    if int(n) >= 3 and int(n) <= 5:
        print ("Весна")
    elif int(n) >= 6 and int(n) <= 9:
        print ("лето")
    elif int(n) >= 9 and int(n) <= 11:        
        print ("осень")
    elif int(n) == 12 or int(n) <= 2:        
        print ("зима")
    else:
    
        print ("Такого месяца нет!!!!!!!!!!")
        

    
mon= input("Введите номер месяца : ")

month_to_season(mon)


