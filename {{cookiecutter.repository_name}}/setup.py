from os.path import abspath, dirname, join
from setuptools import find_packages, setup


ENTRY_POINTS = '''
[paste.app_factory]
main = {{cookiecutter.package_name}}:main
'''
APPLICATION_CLASSIFIERS = [
    'Programming Language :: Python',
    'Framework :: Pyramid',
    'Framework :: Pyramid :: InvisibleRoads',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
]
APPLICATION_REQUIREMENTS = [
    # web
    'plaster-pastedeploy',
    'pyramid',
    'pyramid-ipython',
    'waitress',
    # architecture
    'invisibleroads-posts >= 0.7.3',
{%- if cookiecutter.database_package == 'sqlalchemy' %}
    'invisibleroads-records >= 0.5.2',
{%- endif %}
]
TEST_REQUIREMENTS = [
    'pytest',
    'pytest-cov',
    'webtest',
]
FOLDER = dirname(abspath(__file__))
DESCRIPTION = '\n\n'.join(open(join(FOLDER, x)).read().strip() for x in [
    'README.md', 'CHANGES.md'])


setup(
    name='{{cookiecutter.package_name.replace('_', '-')}}',
    version='0.0.0',
    description='{{cookiecutter.application_name}}',
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    classifiers=APPLICATION_CLASSIFIERS,
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    url='{{cookiecutter.application_url}}',
    keywords='web wsgi bfg pylons pyramid invisibleroads',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={'test': TEST_REQUIREMENTS},
    install_requires=APPLICATION_REQUIREMENTS,
    entry_points=ENTRY_POINTS)
