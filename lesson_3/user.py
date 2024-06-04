class user:

    first_name = "noname"
    last_name = "noname"

    def __init__(self,fn, ln):
        print("CREATE")
        self.first_name = fn
        self.last_name= ln

    def get_fname(self):
        print("Имя : ", self.first_name)
    
    def get_lname(self):
        print("Фамилие : ",self.last_name)



    def get_fullname(self):
        print("Имя : ",self.first_name,"  Фамилие : ",self.last_name)


alx = user("ALX","IVANOV")

alx.get_fname()
alx.get_lname()
alx.get_fullname()