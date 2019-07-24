from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='jxl',
    version='1.0.0',
    packages=['client', 'client.auth', 'client.home', 'client.errors', 'services'],
    url='',
    license='MIT',
    author='Alex Gagnon',
    author_email='',
    description='Exports project issues filtered by versions to an Excel spreadsheet.',
    install_requires=requirements,
)
