# LuizaLabs Test

#### Objetivos

Desenvolver um sistema de cadastro de usuários

Requisitos

* O front deverá se conectar ao back­end por API
* API deve seguir os princípios REST
*Salvar as informações necessárias em um banco de dados relacional de sua escolha
* Desenvolvimento em Python | Node.Js | GO
* Utilizar uma ferramenta de versionamento
* Documentar como rodar o projeto


#### Dependências

* Python - v3.4.3
* Node.js
* MySQL


#### Instalação

Com as dependências já instaladas, abra o terminal e digite:

```sh
    $ git clone https://github.com.br/matheusho/luizalabs-test.git
    $ cd luiza-test
```


#### Dependências Back-End

Ainda no terminal, digite:

```sh
    pyvenv venv
    pip install -r requirements.txt
```

#### Dependências Front-End.

Ainda no terminal, digite:

```sh
    cd front_end
    npm install express express-load body-parser cookie-parser morgan serve-favicon ejs
```

## Rodando o projeto


#### Banco de dados

Vá até o arquivo env.py que se encontra

```sh
    cd front_end
    alembic upgrade head
```

#### Back-End

Abra um novo terminal e vá até pasta 'back_end', confira abaixo:

```sh
    cd luiza_labs/back_end
    python manage.py runserver
```


#### Front-End

Abra um novo terminal e vá até pasta 'front_end', confira abaixo:

```sh
    cd luiza_labs/front_end
    nodejs app.js
```

No navegador acesse: http://localhost
