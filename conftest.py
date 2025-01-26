import pytest
from selenium import webdriver
import urls
import string
import random
import requests


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        driver_name = 'chrome'
        driver = webdriver.Chrome()
    else:
        driver_name = 'firefox'
        driver = webdriver.Firefox()
    driver.get(urls.BASE_URL)

    yield driver, driver_name

    driver.quit()

def create_new_user_and_return_auth_data():
    def generate_random_string(length=10):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    email = generate_random_string() + '@gmail.com'
    password = generate_random_string()
    name = generate_random_string()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload

@pytest.fixture(scope='function')
def create_and_delete_user():
    payload = create_new_user_and_return_auth_data()
    response = requests.post(f'{urls.BASE_URL}{urls.NEW_USER_URL}', data=payload)
    response_data = response.json()
    yield payload, response_data
    access_token = response.json().get('accessToken')
    requests.delete(f'{urls.BASE_URL}{urls.DELETE_USER_URL}', headers={'Authorization': access_token})

@pytest.fixture
def create_user_order_and_delete(create_and_delete_user):
    access_token = create_and_delete_user[1]['accessToken']
    headers = {"Authorization": access_token}
    ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]}
    response = requests.post(f'{urls.BASE_URL}{urls.ORDER_URL}',
                             headers=headers,
                             json=ingredients)
    yield access_token, response
    requests.delete(f'{urls.BASE_URL}{urls.DELETE_USER_URL}', headers=headers)

@pytest.fixture
def use_token(driver, create_and_delete_user):
    driver[0].get(urls.BASE_URL)
    user = create_and_delete_user[1]
    access_token = user.get('accessToken')
    refresh_token = user.get('refreshToken')
    driver[0].execute_script(f'window.localStorage.setItem("accessToken", "{access_token}");')
    driver[0].execute_script(f'window.localStorage.setItem("refreshToken", "{refresh_token}");')