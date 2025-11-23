import pytest
import requests
from pytest_bdd import scenarios, given, when, then
from dotenv import load_dotenv
import os

load_dotenv() 

scenarios('features/login.feature')

BASE_URL = os.getenv("BASE_URL")
HEADERS = {"x-api-key": os.getenv("X_API_KEY")}

@pytest.fixture
def context():
    return {}

@given('que a API de login está disponível')
def api_login_disponivel():
    pass

@when('faço uma requisição POST para "/api/login" com dados válidos')
def post_login_valido(context):
    payload = {"email": "heloisa.cativo@gmail.com", "password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/api/login", data=payload, headers=HEADERS)
    context['response'] = response

@when('faço uma requisição POST para "/api/login" com dados inválidos')
def post_login_invalido(context):
    payload = {"email": "heloisa.cativo@gmail.com"} 
    response = requests.post(f"{BASE_URL}/api/login", data=payload, headers=HEADERS)
    context['response'] = response

@then('o status da resposta deve ser 200')
def check_status_200(context):
    assert context['response'].status_code == 200

@then('o status da resposta deve ser 400')
def check_status_400(context):
    assert context['response'].status_code == 400