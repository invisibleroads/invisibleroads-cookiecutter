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
    pserve development.ini

## Deploy

    mkdir ~/Experiments/{{cookiecutter.repository_name}}
    cp ~/Projects/{{cookiecutter.repository_name}}/production.ini \
        ~/Experiments/{{cookiecutter.repository_name}}

    source ~/.virtualenvs/{{cookiecutter.repository_name}}/bin/activate
    cd ~/Experiments/{{cookiecutter.repository_name}}
    pserve production.ini
