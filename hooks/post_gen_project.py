from os.path import curdir, join
from shutil import rmtree


PACKAGE_FOLDER = join(curdir, '{{ cookiecutter.package_name }}')


if __name__ == '__main__':
    if '{{ cookiecutter.database_package }}' == 'none':
        rmtree(join(PACKAGE_FOLDER, 'migrations'))
        rmtree(join(PACKAGE_FOLDER, 'models'))
