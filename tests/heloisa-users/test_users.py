import requests
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from dotenv import load_dotenv
import os

load_dotenv() 

scenarios('features/users.feature')

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("X_API_KEY")
HEADERS = {"x-api-key": API_KEY}

@pytest.fixture
def context():
    return {}

@given('que a API está disponível')
def api_disponivel():
    pass 

@when(parsers.parse('faço uma requisição GET para "{endpoint}" com o parâmetro "page=2"'))
def get_users_page2(context, endpoint):
    response = requests.get(f"{BASE_URL}{endpoint}", params={'page': 2}, headers=HEADERS)
    context['response'] = response

@when(parsers.parse('faço uma requisição GET para "{endpoint}"'))
def get_user(context, endpoint):
    response = requests.get(f"{BASE_URL}{endpoint}", headers=HEADERS)
    context['response'] = response

@when(parsers.parse('faço uma requisição POST para "{endpoint}" com dados válidos'))
def post_user(context, endpoint):
    payload = {"name": "heloisa", "job": "developer"}
    response = requests.post(f"{BASE_URL}{endpoint}", json=payload, headers=HEADERS)
    context['response'] = response

@when(parsers.parse('faço uma requisição PATCH para "{endpoint}" com dados de atualização'))
def patch_user(context, endpoint):
    payload = {"name": "heloisa", "job": "developer"}
    response = requests.patch(f"{BASE_URL}{endpoint}", json=payload, headers=HEADERS)
    context['response'] = response

@when(parsers.parse('faço uma requisição DELETE para "{endpoint}"'))
def delete_user(context, endpoint):
    response = requests.delete(f"{BASE_URL}{endpoint}", headers=HEADERS)
    context['response'] = response

@when(parsers.parse('faço uma requisição GET para "{endpoint}" com o parâmetro "delay=3"'))
def get_users_delay(context, endpoint):
    response = requests.get(f"{BASE_URL}{endpoint}", params={'delay': 3}, timeout=3.5, headers=HEADERS)
    context['response'] = response

@then(parsers.parse('o status da resposta deve ser {status_code:d}'))
def check_status_code(context, status_code):
    response = context['response']
    assert response.status_code == status_code, f"Esperado {status_code}, obtido {response.status_code}"