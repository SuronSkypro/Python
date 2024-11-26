import requests
import pytest


COMPANY_ID = ""
API_KEY = ""
SOTR_ID =""
ADDED_PROJECT_ID = ""



BASE_URL = "https://ru.yougile.com"
GetCompanyID_URL = BASE_URL + "/api-v2/auth/companies"
GetApiKey_URL = BASE_URL + "/api-v2/auth/keys/get"
GetSotrList_URL = "https://ru.yougile.com/api-v2/users"
PROJECT_URL = "https://ru.yougile.com/api-v2/projects"

LOGIN_FIRST = {
    "login": "suron.skypro@yandex.ru",
    "password": "SuronSkypro2024",
    "name": "Skypro"
}

LOGIN_COMPANY_ID = {
    "login": "suron.skypro@yandex.ru",
    "password": "SuronSkypro2024",
    "companyId": ""
}

AUTH_HEADERS = {
    "Authorization": f"Bearer {API_KEY}"
    }
    



def test_GetCompanyID():
    response = requests.post(GetCompanyID_URL, json=LOGIN_FIRST)
    assert response.status_code == 200, "Ошибка получения company ID"
    response_data = response.json()
    if "content" in response_data and response_data["content"]:
        COMPANY_ID = response_data["content"][0]["id"]
        LOGIN_COMPANY_ID["companyId"] = COMPANY_ID 
        return response_data["content"][0]["id"]
    raise ValueError("Неправильная структура или ответ пустой")

def test_GetApiKey():
    response = requests.post(GetApiKey_URL, json=LOGIN_COMPANY_ID)
    assert response.status_code == 200, "Ошибка получения API key"
    response_data = response.json()
    API_KEY = response_data[0]["key"]
    AUTH_HEADERS["Authorization"] = f"Bearer {API_KEY}"
    return response_data[0]["key"]
    

def test_GetSotrList():
    response = requests.get(GetSotrList_URL, headers= AUTH_HEADERS)
    assert response.status_code == 200, "Ошибка получения SotrID key"
    response_data = response.json()
    if "content" in response_data and response_data["content"]:
        SOTR_ID = response_data["content"][0]["id"]
        return response_data["content"][0]["id"]
    raise ValueError("Неправильная структура или ответ пустой")

def test_GetProjectList():
    response = requests.get(PROJECT_URL, headers= AUTH_HEADERS)
    assert response.status_code == 200, "Не могу получить список сотрудников"
    response_data = response.json()
    assert len(response_data) >= 0

def test_positiv_AddProject():

    # Получаем входные данные
    COMPANY_ID = test_GetCompanyID()
    LOGIN_COMPANY_ID["companyId"] = COMPANY_ID
    # Получение API_KEY
    API_KEY = test_GetApiKey()
    #  Получение Sotr_List
    AUTH_HEADERS["Authorization"] = f"Bearer {API_KEY}"
    SOTR_ID = test_GetSotrList()
    
    # Получаем список проектов и запоминаем их количество
    response = requests.get(PROJECT_URL, headers= AUTH_HEADERS)
    assert response.status_code == 200, "Не могу получить список сотрудников"
    response_data = response.json()
    Before_add_count = response_data.get("paging", {}).get("count", None)

    # Добавляем новый проект
    ProjectData= {
       "title": "Проект добавлен через API Skypro #1",
        "users": {
           SOTR_ID : "admin"
        }   
    }
    
    response = requests.post(PROJECT_URL, headers = AUTH_HEADERS,json = ProjectData)
    assert response.status_code == 201, "Не могу добавить проект"
    ADDED_PROJECT_ID  = response_data.get("id", None)


    # Снова олучаем список проектов и сравниваем их количество с предыдущем  для проверки что проект добавился
    response = requests.get(PROJECT_URL, headers= AUTH_HEADERS)
    assert response.status_code == 200, "Не могу получить список сотрудников"
    response_data = response.json()
    After_add_count = response_data.get("paging", {}).get("count", None)
    
    assert  After_add_count > Before_add_count, "----------------------"

def test_negative_AddProject():
     
     # Получаем входные данные-----------------------------------------------------------------
    COMPANY_ID = test_GetCompanyID()
    LOGIN_COMPANY_ID["companyId"] = COMPANY_ID
    # Получение API_KEY
    API_KEY = test_GetApiKey()
    #  Получение Sotr_List
    AUTH_HEADERS["Authorization"] = f"Bearer {API_KEY}"
    SOTR_ID = test_GetSotrList()

    # Получаем список проектов и запоминаем их количество
    response = requests.get(PROJECT_URL, headers= AUTH_HEADERS)
    assert response.status_code == 200, "Не могу получить список сотрудников"
    response_data = response.json()
    Before_add_count = response_data.get("paging", {}).get("count", None)

    # Добавляем новый проект без обязятельного поля
    ProjectData= {
        "users": {
           SOTR_ID : "admin"
        }   
    }
    
    # Должны получить ошибку 400
    response = requests.post(PROJECT_URL, headers= AUTH_HEADERS,json = ProjectData)
    assert response.status_code == 400 , "Странно на проект добавился"


    # Снова олучаем список проектов и сравниваем их количество с предыдущем  для проверки что проект добавился
    response = requests.get(PROJECT_URL, headers= AUTH_HEADERS)
    assert response.status_code == 200, "Не могу получить список сотрудников"
    response_data = response.json()
    After_add_count = response_data.get("paging", {}).get("count", None)
    assert  After_add_count == Before_add_count

def test_Delete_Project():

    # Получаем входные данные
    COMPANY_ID = test_GetCompanyID()
    LOGIN_COMPANY_ID["companyId"] = COMPANY_ID
    # Получение API_KEY
    API_KEY = test_GetApiKey()
    #  Получение Sotr_List
    AUTH_HEADERS["Authorization"] = f"Bearer {API_KEY}"
    SOTR_ID = test_GetSotrList()
    
    # Получаем список проектов и запоминаем их количество
    response = requests.get(PROJECT_URL, headers= AUTH_HEADERS)
    assert response.status_code == 200, "Не могу получить список сотрудников"
    response_data = response.json()
    Before_add_count = response_data.get("paging", {}).get("count", None)


    # Добавляем новый проект
    ProjectData= {
       "title": "Проект добавлен через API Skypro УДАЛЯЕМ ",
        "users": {
           SOTR_ID : "admin"
        }   
    }
    
    response = requests.post(PROJECT_URL, headers = AUTH_HEADERS,json = ProjectData)
    assert response.status_code == 201, "Не могу добавить проект"
    response_data = response.json()
    ADDED_PROJECT_ID  = response_data.get("id", None)

    TempUrl=PROJECT_URL + "/"  + str(ADDED_PROJECT_ID)
    PROJECT_ID= ADDED_PROJECT_ID
    response = requests.put(TempUrl, headers = AUTH_HEADERS)
    assert response.status_code == 200, "Не могу удалить  проект"
    
    response_data = response.json()
    ADDED_PROJECT_ID  = response_data.get("id", None)
    assert PROJECT_ID == ADDED_PROJECT_ID


    


