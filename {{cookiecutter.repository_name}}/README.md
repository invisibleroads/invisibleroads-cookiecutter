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
{%- if cookiecutter.database_package == 'records' %}
    invisibleroads initialize development.ini
{%- endif %}
    pserve development.ini --reload

## Deploy

    mkdir ~/Experiments/{{cookiecutter.repository_name}}
    cd ~/Projects/{{cookiecutter.repository_name}} \
    cp production.ini \
        ~/Experiments/{{cookiecutter.repository_name}}

    source ~/.virtualenvs/{{cookiecutter.repository_name}}/bin/activate
    cd ~/Experiments/{{cookiecutter.repository_name}}
{%- if cookiecutter.database_package == 'records' %}
    invisibleroads initialize production.ini
    # alembic -c production.ini revision --autogenerate -m 'Start'
    # alembic -c production.ini upgrade head
{%- endif %}
    pserve production.ini
