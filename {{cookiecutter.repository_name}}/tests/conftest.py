pytest_plugins = [
    'invisibleroads_posts.tests',
{%- if cookiecutter.database_package == 'records' %}
    'invisibleroads_records.tests',
{%- endif %}
{%- if cookiecutter.security_package == 'users' %}
    'invisibleroads_users.tests',
{%- endif %}
    '{{cookiecutter.package_name}}.tests',
]
