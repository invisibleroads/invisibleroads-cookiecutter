from {{cookiecutter.package_name}}.views import index


class TestIndex(object):

    def test_accept_parameters(self, application_request):
        d = index(application_request)
        assert d['text'] == 'whee!'
