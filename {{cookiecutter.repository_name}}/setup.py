from os.path import abspath, dirname, join
from setuptools import find_packages, setup


ENTRY_POINTS = '''
[paste.app_factory]
main = {{cookiecutter.package_name}}:main
'''
APP_CLASSIFIERS = [
    'Programming Language :: Python',
    'Framework :: Pyramid',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
]
APP_REQUIREMENTS = [
    # web
    'plaster-pastedeploy',
    'pyramid',
    'pyramid-ipython',
    'waitress',
    # test
    'pytest>=3.7.4',
]
TEST_REQUIREMENTS = [
    'pytest-cov',
]
FOLDER = dirname(abspath(__file__))
DESCRIPTION = '\n\n'.join(open(join(FOLDER, x)).read().strip() for x in [
    'README.md', 'CHANGES.md'])


setup(
    name='{{cookiecutter.repository_name}}',
    version='0.0.0',
    description='{{cookiecutter.application_name}}',
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    classifiers=APP_CLASSIFIERS,
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    url='{{cookiecutter.application_url}}',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={'test': TEST_REQUIREMENTS},
    install_requires=APP_REQUIREMENTS,
    entry_points=ENTRY_POINTS)
