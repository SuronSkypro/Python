from Address import Address


class Mailing:
    
    from_address = Address("000000","No name","No name",0,0)
    to_address = Address("000000","No name","No name",0,0)
    cost = 0
    track = "000000"

    def __init__(self,from_adress,to_adress,cost,track):
        print("Create")
        self.to_address=to_adress
        self.from_address=from_adress
        self.cost=cost
        self.track=track
    






