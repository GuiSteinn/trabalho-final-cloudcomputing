# Trabalho Final - Cloud Computing

Projeto-modelo de API REST com fluxo DevOps para a disciplina de Cloud Computing da UNIDAVI.

## Tecnologias

- Python 3.12
- Biblioteca padrão `http.server`
- Testes unitários com `unittest`
- GitHub Actions para Integração Contínua
- Docker para execução em container

## Rotas da API

| MÃ©todo | Rota | Descrção |
|---|---|---|
| GET | `/status` | Retorna nome, versÃ£o e status da aplicação. |
| GET | `/chamados` | Retorna ao menos 10 chamados simulados. |
| GET | `/chamados/{id}` | Retorna um chamado pelo identificador. |

## Executar localmente sem container

```bash
python api/app.py
```

Acesse:

```text
http://localhost:8000/status
http://localhost:8000/chamados
http://localhost:8000/chamados/1
```

## Executar testes

```bash
python -m unittest discover -s api/tests
```

## Executar com Docker

```bash
docker build -t api-chamados-cloud .
docker run --rm -p 8000:8000 api-chamados-cloud
```

## Estrutura

```text
api/
  app.py
  data/
    chamados.json
  tests/
    test_api.py
.github/
  workflows/
    ci.yml
Dockerfile
README.md
```

## Observação de execução
A API pode ser executada localmente com Python 3.12 ou superior.

## Pipeline CI
O workflow executa validacao de sintaxe e testes unitarios automaticamente.

## Dados simulados
Os registros ficam em arquivo JSON externo para facilitar manutencao e troca do tema.

## Testes
Os testes validam codigo HTTP, estrutura JSON, rota de status e caso de identificador inexistente.
