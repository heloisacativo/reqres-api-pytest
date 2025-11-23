# Regres API Pytest

Testes de integração na API pública [ReqRes](https://reqres.in/) utilizando **pytest**, **pytest-bdd** (BDD/Gherkin) e **requests**.

## Pré-requisitos

- Python 3.8+
- [Poetry](https://python-poetry.org/)

- [ReqRes](https://reqres.in/) para obter sua API Key

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/heloisacativo/reqres-api-pytest.git
   cd regres-api-pytest
   ```

2. Instale as dependências:
   ```sh
   poetry install
   ```

3. Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
   ```
   BASE_URL=https://reqres.in
   X_API_KEY=reqres-free-v1
   ```

## Estrutura do Projeto

```
regres-api-pytest/
│
├── tests/ 
│   └── heloisa-users/
│       ├── features/
│       │   ├── users.feature    # cenários de teste de usuários em Gherkin
│       │   └── login.feature    # cenários de teste de login em Gherkin
│       ├── test_users.py        # steps dos cenários de usuários
│       └── test_login.py        # steps dos cenários de login
├── README.md
└── pyproject.toml
```

## Como rodar os testes

1. Ative o ambiente virtual:
   ```sh
   poetry env activate
   ```

2. Execute todos os testes:
   ```sh
   pytest -v
   ```

3. Para rodar um teste específico:
   ```sh
   pytest tests/heloisa-users/test_users.py
   ```

## Observações

- Certifique-se de que sua API Key está correta no `.env`.
- Os testes cobrem cenários de usuários e login, incluindo casos válidos e inválidos.
- Os testes usam o padrão BDD.

## Referências

- [ReqRes API Docs](https://reqres.in/)
- [pytest](https://docs.pytest.org/)
- [pytest-bdd](https://pytest-bdd.readthedocs.io/)
- [requests](https://docs.python-requests.org/)