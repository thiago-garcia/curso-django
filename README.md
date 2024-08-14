# Curso Django
Código desenvolvido no módulo de Django do https://www.dev.pro.br/

[![codecov](https://codecov.io/gh/thiago-garcia/curso-django/branch/main/graph/badge.svg?token=0EDNV110P8)](https://codecov.io/gh/thiago-garcia/curso-django)

Projeto desenvolvido com Django e utiliza Pipenv como gerenciador de dependências e Python Decouple para configurações.

Requisitos para executar localmente:

- Git
- Python >= 3.10
- Docker e Docker Compose

Clonar e instalar dependências:

```bash
git clone https://github.com/thiago-garcia/curso-django.git
cd curso-django
cp contrib/env-sample .env
python -m pip install pipenv
pipenv sync -d
```

Necessário editar a linha do arquivo ```.env``` para ```DEBUG=True```

O projeto utiliza Postgres como banco de dados. Com docker compose, executar:

```bash
docker compose up -d
```

Aplicar migrações no banco de dados e criar usuário:

```bash
# necesário estar no virtualenv, caso não esteja ativo, executar:
pipenv shell 

# aplicar migrações e criar usuário
python manage.py migrate
python manage.py createsuperuser
```

Rodar o servidor localmente:
```bash
# necesário estar no virtualenv, caso não esteja ativo, executar:
pipenv shell 

python manage.py runserver
```