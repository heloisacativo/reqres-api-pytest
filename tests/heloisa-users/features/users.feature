# language: pt
# Testes da API de Usuários

Funcionalidade: API de Usuários

  Cenário: Listar usuários da página 2
    Dado que a API está disponível
    Quando faço uma requisição GET para "/api/users" com o parâmetro "page=2"
    Então o status da resposta deve ser 200

  Cenário: Buscar usuário específico
    Dado que a API está disponível
    Quando faço uma requisição GET para "/api/users/2"
    Então o status da resposta deve ser 200

  Cenário: Criar novo usuário
    Dado que a API está disponível
    Quando faço uma requisição POST para "/api/users" com dados válidos
    Então o status da resposta deve ser 201

  Cenário: Atualizar usuário existente
    Dado que a API está disponível
    Quando faço uma requisição PATCH para "/api/users/2" com dados de atualização
    Então o status da resposta deve ser 200

  Cenário: Deletar usuário
    Dado que a API está disponível
    Quando faço uma requisição DELETE para "/api/users/2"
    Então o status da resposta deve ser 204

  Cenário: Resposta com delay
    Dado que a API está disponível
    Quando faço uma requisição GET para "/api/users" com o parâmetro "delay=3"
    Então o status da resposta deve ser 200