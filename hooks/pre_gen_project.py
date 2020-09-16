import re
import sys


PACKAGE_PATTERN = re.compile(r'^[_a-zA-Z][_a-zA-Z0-9]+$')


security_package = '{{ cookiecutter.security_package }}'
database_package = '{{ cookiecutter.database_package }}'
package_name = '{{ cookiecutter.package_name }}'


if security_package != 'none' and database_package == 'none':
    sys.exit(f'database_package: is required for security_package')
if not PACKAGE_PATTERN.match(package_name):
    sys.exit(f'package_name: is not valid')
