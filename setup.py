import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-bootstrap-ui',
    version='0.1-alpha1',
    packages=find_packages(),
    include_package_data=True,
    license='ISC License',
    description='This aims to be a powerful Django app to ease the integration of the popular Bootstrap UI framework'
                ' (http://getbootstrap.com).',
    long_description=README,
    url='https://github.com/timorieber/django-bootstrap-ui',
    author='Timo Rieber',
    author_email='dev@timorieber.de',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
