try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Tools for handling icosahedral spheres',
    'version': '0.1.0',
    'install_requires': [],
    'packages': ['icosahedron'],
    'name': 'icosahedron'
}

setup(**config)
