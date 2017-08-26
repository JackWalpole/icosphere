try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Tools for handling icosahedral spheres',
    'author': 'Jack Walpole',
    'author_email' = 'j,walpole@gmail.com',
    'license' = 'MIT',
    'url' = 'https://github.com/JackWalpole/icosphere' 
    'version': '0.1.0',
    'install_requires': ['numpy >= 1.1'],
    'packages': ['icosphere'],
    'name': 'icosphere'
}

setup(**config)
