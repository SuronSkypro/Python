from mailing import Mailing
from Address import Address


tt = Mailing(Address("000001","Город 1","Удица 1",1,1),Address("000002","Город 2","Улица 2",2,2),100,"track001")

print("Отправление", tt.track, "из", tt.from_address.Index," , ",tt.from_address.City," , ",tt.from_address.Street,", дом - ", tt.from_address.Home, " в ", tt.to_address.Index," , ",tt.to_address.City," , ",tt.to_address.Street," дом - ", tt.to_address.Home," Стоимость : ", tt.cost)
        

