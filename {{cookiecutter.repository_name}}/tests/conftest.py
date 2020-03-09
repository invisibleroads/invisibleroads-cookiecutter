from pytest import fixture
from webtest import TestApp

from {{cookiecutter.package_name}} import main as get_app


pytest_plugins = [
    'invisibleroads_posts.tests',
]


@fixture
def application(application_request):
    settings = application_request.registry.settings
    yield TestApp(get_app({}, **settings))


@fixture
def application_request(posts_request):
    yield posts_request
