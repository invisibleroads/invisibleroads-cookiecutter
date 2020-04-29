pytest_plugins = [
    'invisibleroads_posts.tests',
{%- if cookiecutter.database_package == 'sqlalchemy' %}
    'invisibleroads_records.tests',
{%- endif %}
    '{{cookiecutter.package_name}}.tests',
]
