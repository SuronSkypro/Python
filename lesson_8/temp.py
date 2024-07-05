import requests
import json

TestUrl= "https://x-clients-be.onrender.com"
TestUrl_Token=""

 
Testuser ={
    'username': 'bloom',
    'password':'fire-fairy'
 }



resp = requests.post(TestUrl+"/auth/login",json= Testuser)
print(resp.status_code)
    
TestUrl_Token=resp.json()["userToken"]

print(TestUrl_Token)
