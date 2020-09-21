from pyramid.config import Configurator


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
    {% endif -%}
    config.include('.routes')
    config.scan('.views')
