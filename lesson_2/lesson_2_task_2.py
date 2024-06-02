
def is_year_leap(year):

    tem = int(year) % 4
    print (tem)
    
    if tem == 0 :
        
        return True
    else :
        
        return False
    

year = input("Ввведите год :")

print ("Год :"+ year + " - ",is_year_leap(year))
2
    