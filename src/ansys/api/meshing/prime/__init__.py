# Copyright 2023 ANSYS, Inc.
# Unauthorized use, distribution, or duplication is prohibited.
import os

__all__ = ['__version__']
# Get version from version info
HERE = os.path.abspath(os.path.dirname(__file__))
__version__ = None
version_file = os.path.join(HERE, 'VERSION')
with open(version_file, mode='r') as fd:
    __version__ = fd.read().strip()