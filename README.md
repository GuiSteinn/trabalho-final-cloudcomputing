# Trabalho Final - Cloud Computing

Projeto-modelo de API REST com fluxo DevOps para a disciplina de Cloud Computing da UNIDAVI.

> Ajuste este README ao seu tema individual antes da entrega. O tema usado nesta base é "chamados de suporte em nuvem".

## Tecnologias

- Python 3.12
- Biblioteca padrão `http.server`
- Testes unitários com `unittest`
- GitHub Actions para Integração Contínua
- Docker para execução em container

## Rotas da API

| Método | Rota | Descrição |
|---|---|---|
| GET | `/status` | Retorna nome, versão e status da aplicação. |
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

## Observação sobre autoria e IA

Esta base foi produzida com apoio de Inteligência Artificial Generativa e deve ser estudada, adaptada e explicada pelo discente antes de qualquer entrega. Caso seja usada, o uso de IA deve ser identificado no Relatório Técnico Final e na Declaração de Autoria, conforme o enunciado do trabalho.
