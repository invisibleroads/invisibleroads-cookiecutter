# {{cookiecutter.application_name}}

## Install

    virtualenv -p $(which python3) \
        ~/.virtualenvs/{{cookiecutter.repository_name}}
    source ~/.virtualenvs/{{cookiecutter.repository_name}}/bin/activate
    cd ~/Projects/{{cookiecutter.repository_name}}
    pip install -e .

## Prototype

    source ~/.virtualenvs/{{cookiecutter.repository_name}}/bin/activate
    cd ~/Projects/{{cookiecutter.repository_name}}
{%- if cookiecutter.database_package == 'sqlalchemy' %}
    invisibleroads initialize development.ini
{%- endif %}
    pserve development.ini

## Deploy

    mkdir ~/Experiments/{{cookiecutter.repository_name}}
    cp ~/Projects/{{cookiecutter.repository_name}}/production.ini \
        ~/Experiments/{{cookiecutter.repository_name}}

    source ~/.virtualenvs/{{cookiecutter.repository_name}}/bin/activate
    cd ~/Experiments/{{cookiecutter.repository_name}}
{%- if cookiecutter.database_package == 'sqlalchemy' %}
    invisibleroads initialize production.ini
    alembic -c production.ini revision --autogenerate -m 'Start'
    alembic -c production.ini upgrade head
{%- endif %}
    pserve production.ini
