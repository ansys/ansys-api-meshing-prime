"""Version of ansys-api-meshing-prime library.

On the ``main`` branch, use 'dev0' to denote a development version.
For example:

version_info = 0, 1, 0, 'dev0'

Examples
--------
Print the version

>>> from ansys.product import library
>>> print(library.__version__)
0.1.5.dev1

"""

# major, minor, patch
version_info = 0, 1, 5, 'dev1'

# Nice string for the version
__version__ = '.'.join(map(str, version_info))

