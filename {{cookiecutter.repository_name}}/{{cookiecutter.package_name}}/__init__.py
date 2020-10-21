from pyramid.config import Configurator

{% if cookiecutter.database_package == 'records' -%}
from . import models as M  # noqa
{%- endif %}


def main(global_config, **settings):
    with Configurator(settings=settings) as config:
        includeme(config)
    return config.make_wsgi_app()


def includeme(config):
    config.include('invisibleroads_posts')
    {% if cookiecutter.database_package == 'records' -%}
    config.include('invisibleroads_records')
    {% endif -%}
    {% if cookiecutter.security_package == 'users' -%}
    config.include('invisibleroads_users')
    configure_models(config)
    {% endif -%}
    configure_views(config)


{% if cookiecutter.security_package == 'users' -%}
def configure_models(config):
    from invisibleroads_users.models import User
    M.User = User
{%- endif %}


def configure_views(config):
    config.include('.routes')
    config.scan('.views')
