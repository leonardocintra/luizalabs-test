# LuizaLabs Test


##### Objetivos

Desenvolver um cadastro de usuários com integração com o Facebook.

A primeira etapa consiste em coletar informações do facebook utilizando um Facebook ID informado pelo usuário, ou cadastrando com uma conta já existente. Após a primeira etapa concluída, é apresentado um formulário para complementar o cadastro.

Na listagem de usuários, os mesmos poderão ser alterados ou removidos.

##### Requisitos

* O front deverá se conectar ao back­end por API
* API deve seguir os princípios REST
* Salvar as informações necessárias em um banco de dados relacional de sua escolha
* Desenvolvimento em Python | Node.Js | GO
* Utilizar uma ferramenta de versionamento
* Documentar como rodar o projeto



## Projeto

##### Tecnologias

Aplicação desenvolvida em dois módulos:

* Front-End: [Node.js], [Vue.js], [jQuery] e [Bootstrap].
* Back-End: [Python], [Bottle], [SQLAlchemy] - ORM, [Alembic] - Database migrations, e [MySQL].


##### Instalação

Antes de fazer o download do projeto, verifique se já possui as dependências abaixo. Caso não possua alguma delas, clique no nome da dependência para ser redirecionado ao site da mesma:

* [Python] - v3.4
* [Node.js] - v0.10.25
* [MySQL]


#### Download do projeto

Com as dependências já instaladas, abra o terminal para que possamos baixar nosso projeto:

```sh
    $ git clone https://github.com/matheusho/luizalabs-test.git
    $ cd luizalabs-test
```


### Back-End


Acesse a pasta 'back_end' para começar a instalação:


```sh
    cd back_end
```

##### Ambiente virtual e instação dependências

```sh
    pyvenv venv
    source venv/bin/activate
    pip install -r requirements.txt
```


##### Banco de Dados

No MySQL crie um schema com o nome luizalabs.

```
mysql -u your_user -p
create schema luizalabs
```

No arquivo env.py configure as seguintes variáveis de ambiente com os dados da sua instalação local.

```
os.environ['DB_NAME'] = 'luizalabs'
os.environ['DB_USER'] = 'user'
os.environ['DB_PASSWORD'] = 'pass'
os.environ['DB_HOST'] = 'localhost'
os.environ['DB_PORT'] = '5432'
```

Configuração efetuada no env.py, precisamos configurar nosso sistema de versionamento de banco de dados. Abra o arquivo alembic.ini, vá até a linha 32 e substitua user e password com o seu usuário e senha do MySQL.

```
sqlalchemy.url = mysql://user:pasword@localhost/luizalabs
```

##### Gerandos as tabelas

```
alembic upgrade head
```

##### Iniciando o servidor

Após ter executado com sucesso os processos anteriores, é hora de rodar nosso back-end.

```
python manage.py runserver
```

##### Executando Testes

```
python manage.py test
```

##### Acessando a aplicação

Acesse no link: http://127.0.0.1:8080/


### Front-End

Em uma nova janela do terminal acesse o diretório do projeto e vá até a pasta 'front_end'.

##### Dependências

```
npm install express express-load body-parser cookie-parser serve-favicon morgan ejs
```

##### Iniciando o servidor

Linux:

```
nodejs app.js
```

Mac OS X
```
node app.js
```

##### Acessando a aplicação

Acesse no link: http://localhost:3000/

[Node.js]: http://nodejs.org/download
[Vue.js]: http://vuejs.org
[jQuery]: http://jquery.com
[Bootstrap]: http://getbootstrap.com
[Python]: http://python.org/downloads
[Bottle]: http://bottlepy.org
[SQLAlchemy]: http://sqlalchemy.org
[Alembic]: http://bitbucket.org/zzzeek/alembic
[MySQL]: http://dev.mysql.com/downloads/mysql

