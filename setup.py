"""Classes for help with game creation"""

from __future__ import print_function
from distutils.core import setup
from gameobjects.__init__ import __version__

print("Game Objects v" + __version__)

doc_lines = __doc__.split("\n")

classifiers = """\
Development Status :: 2 - Pre-Alpha
Intended Audience :: Developers
Programming Language :: Python
License :: Public Domain
Operating System :: OS Independent
Topic :: Games/Entertainment
"""

setup(
    name='gameobjects',
    version='0.0.3',
    author='Will McGugan',
    author_email='will@willmcgugan.com',
    license="public domain",
    url='https://github.com/computationalcore/gameobjects',
    download_url='https://github.com/computationalcore/gameobjects/releases',
    platforms=['any'],
    description=doc_lines[0],
    long_description='\n'.join(doc_lines[2:]),
    # package_dir = {'gameobjects': './gameobjects'},
    packages=['gameobjects'],
    classifiers=classifiers.splitlines(),
)
