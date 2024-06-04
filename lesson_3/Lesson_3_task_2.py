from smartphone import Smartphone

Smartcatalog = []

Smartcatalog.append(Smartphone("Nokia","6300","+70000000000"))
Smartcatalog.append(Smartphone("Samsung","galaxy s10","+70000000001"))
Smartcatalog.append(Smartphone("Huawei","nova","+70000000001"))
Smartcatalog.append(Smartphone("Apple","iphone 16","+70000000001"))
Smartcatalog.append(Smartphone("RUPHONE","1","+70000000001"))

for i in range(0,len(Smartcatalog)):
    print(Smartcatalog[i].PhoneFirma,"-",Smartcatalog[i].PhoneModel,".",Smartcatalog[i].PhoneNumber)
