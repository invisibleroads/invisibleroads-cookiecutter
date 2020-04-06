import re
import sys


PACKAGE_PATTERN = re.compile(r'^[_a-zA-Z][_a-zA-Z0-9]+$')
package_name = '{{ cookiecutter.package_name }}'


if not PACKAGE_PATTERN.match(package_name):
    print('ERROR: %s is not a valid Python package name!' % package_name)
    sys.exit(1)
