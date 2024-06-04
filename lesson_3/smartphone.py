class Smartphone:
    
    PhoneFirma = "noname"
    PhoneModel = "noname"
    PhoneNumber = "+70000000000"


    def __init__(self,Firma,Model,Number):
        print("CREATE")
        self.PhoneFirma = Firma
        self.PhoneModel = Model
        self.PhoneNumber = Number


        