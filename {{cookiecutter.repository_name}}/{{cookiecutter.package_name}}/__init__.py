from pyramid.config import Configurator


def main(global_config, **settings):
    with Configurator(settings=settings) as config:
        includeme(config)
        config.scan('.views')
    return config.make_wsgi_app()


def includeme(config):
    {% if cookiecutter.security_package == 'users' -%}
    config.include('invisibleroads_users')
    {% elif cookiecutter.database_package == 'records' -%}
    config.include('invisibleroads_records')
    {% else -%}
    config.include('invisibleroads_posts')
    {% endif -%}
    config.include('.routes')
