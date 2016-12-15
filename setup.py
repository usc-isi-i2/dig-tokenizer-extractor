try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'digTokenizerExtractor',
    'description': 'digTokenizerExtractor',
    'author': 'Jason Slepicka',
    'url': 'https://github.com/usc-isi-i2/dig-tokenizer-extractor',
    'download_url': 'https://github.com/usc-isi-i2/dig-tokenizer-extractor',
    'author_email': 'jasonslepicka@gmail.com',
    'version': '0.3.1',
    # these are the subdirs of the current directory that we care about
    'packages': ['digTokenizerExtractor'],
    'scripts': [],
    'install_requires':['digExtractor>=0.3.2', 'digCrfTokenizer>=0.1.6']
}

setup(**config)
