import os
from setuptools import find_namespace_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='fiduswriter-phplist',
    version='3.7.0rc1',
    packages=find_namespace_packages(),
    include_package_data=True,
    license='AGPL License',
    description='A Fidus Writer plugin to integrate with an emaillist using PHPList.',
    long_description=README,
    url='https://www.github.com/fiduswriter/fiduswriter-phplist',
    author='Johannes Wilm',
    author_email='johannes@fiduswriter.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
