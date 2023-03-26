# Aplicação REST API com Django e Django REST framework

Esta aplicação é uma REST API que utiliza o Django e o Django REST framework. A API permite a criação, leitura, atualização e exclusão de objetos em um banco de dados.

Requisitos

Antes de executar a aplicação, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Django 3.x
- Django REST framework

# Executando a aplicação

1. Clone este repositório:

`git clone https://github.com/seu-usuario/Trabalho_de_Redes.git
cd nome-do-repositorio
`

2. Instale as dependências:

`pip install -r requirements.txt
`

3. Execute as migrações do banco de dados:

`python manage.py migrate
`

4. Execute a aplicação:

`python manage.py runserver
`

5. Acesse a aplicação em **http://localhost:8000/**

# Utilizando a imagem Docker

Também é possível utilizar a aplicação através de uma imagem Docker. Siga as instruções abaixo:

1. Faça o download da imagem Docker:

`docker pull rigar/trabalho-python
`

ou

hub.docker.com/repository/docker/rigar/trabalho-python

2. Execute o container:

`docker run -p 8000:8000 rigar/trabalho-python
`

3. Acesse a aplicação em **http://localhost:8000/**




