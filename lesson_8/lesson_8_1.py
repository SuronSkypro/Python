import requests
import json

TestUrl= "https://x-clients-be.onrender.com"
Testuser ={
    'username': 'bloom',
    'password':'fire-fairy'
 }
TestUrlHeader = {}




def auth():
    resp = requests.post(TestUrl+"/auth/login",json = Testuser)
    assert resp.status_code == 201
    
    TestUrlHeader["x-client-token"]=resp.json()["userToken"]

    
def get_company_list():
    resp = requests.get(TestUrl+"/company")
    return resp

def test_get_employee_list():
    company_list = get_company_list()

    for company_list in company_list:
        resp = requests.get(TestUrl+"/company")



auth()




