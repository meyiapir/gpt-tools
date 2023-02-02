from setuptools import setup

version = '0.0.1'

long_description = '''
Various interesting tools based on GPT-3.
'''

setup(
    name='gpt-tools',

    version=version,

    packages=['gptools', 'gptools.modules'],
    install_requires=['openai'],

    url='https://github.com/meyiapir/gpt-tools',

    license='Apache License, Version 2.0, see LICENSE file',

    author='meyap',

    author_email='mmeyiapir@gmail.com',

    description='Various interesting tools based on GPT-3.',

    description_content_type='text/markdown',

    long_description=long_description,
    long_description_content_type='text/markdown',
)
