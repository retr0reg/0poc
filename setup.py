from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='zer0poc',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
    license='MIT',
    description='PoC generater thats fast and pretty for your vulnerabilty.',
    long_description=open('README.md').read(),
    url='https://github.com/retr0reg/zer00poc',
    author='0reg',
    author_email='0reg@0reg.dev'
)