# Flask Microservice Example

Um exemplo de um serviço flask usando rest-plus.

## Como começar?

1. Clone  repositório.

### Para Instalar
* Tenha o python 3.7 instalado
* Instale o poetry `pip install poetry`
* Instale as dependências usando o comando `poetry install`
* Configure a instância .env usando o exemplo da pasta contrib (vai precisar ter um banco de dados postgres)
* Execute com  `poetry run flask run`

###Examplo de json pra teste

* Ir pra localhost:5000
* Clicar em "try it out"
* Escrever o json abaixo:
*
`
{
  "email_type": "ticket_email",
  "user_id": 1,
  "to_mail": "contato@jonatasoliveira.me",
  "subject": "Teste",
  "params": "{'param1': 'one', 'param2': 'two'}"
}
`

## Routes
Para capturar as rotas existentes usar o comando abaixo.
```
flask routes
```

