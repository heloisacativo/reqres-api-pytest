# language: pt

Funcionalidade: Login na API

  Cenário: Login com dados válidos
    Dado que a API de login está disponível
    Quando faço uma requisição POST para "/api/login" com dados válidos
    Então o status da resposta deve ser 200

  Cenário: Login com dados inválidos
    Dado que a API de login está disponível
    Quando faço uma requisição POST para "/api/login" com dados inválidos
    Então o status da resposta deve ser 400