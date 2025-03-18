import string
import random
from random import randint
import pytest


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
