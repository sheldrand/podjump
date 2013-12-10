try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Corp info and a destination in, range of med clone stations that are closest',
    'author': 'Sheld Rand',
    'url': '',
    'download_url': 'github.com/sheldrand/podJump',
    'author_email': 'joyfulflyer@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'MySQLdb', 'networkx'],
    'packages': ['podJump'],
    'scripts': [],
    'name': 'podJump'
}

setup(**config)
