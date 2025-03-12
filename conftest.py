import string
import random
from random import randint
import pytest
import requests
from data import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    browser = None
    if browser_name == "chrome":
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        ValueError("Can't create instance for this browser param")
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture(scope='session')
def payload():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = str(randint(10000, 99999)) + "@gmail.com"
    password = str(randint(1000000, 9999999))
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    return payload

@pytest.fixture(scope='session')
def registration(payload):
    response = requests.post(Urls.CREATE_USER, data=payload)
    assert response.status_code == 200
    return {
        'email': payload['email'],
        'password': payload['password'],
        'name': payload['name'],
        'accessToken': response.json().get('accessToken')
    }

@pytest.fixture(scope='session')
def get_token(registration):
    return registration['accessToken']

@pytest.fixture(scope='session', autouse=True)
def delete_user(get_token):
    headers = {'Authorization': f'{get_token}'}
    yield
    delete_response = requests.delete(Urls.AUTH_USER, headers=headers)
    assert delete_response.status_code == 202
