# Ansys Prime Server gRPC Interface Package

This Python package contains the auto-generated gRPC Python interface files for
Ansys Prime Server.  Contributions for this API will not be accepted.  Please
create an issue or discussion for questions or enhancements relating to this
project.

## Installation

Provided that these wheels have been published to public PyPI, they can be
installed with:

```bash
pip install ansys-api-meshing-prime
```

## Build

To build the gRPC packages, run:

```bash
pip install build
python -m build .
```

This will create both the source distribution containing just the protofiles
along with the wheel containing the protofiles and build Python interface
files.

Note that the interface files are identical regardless of the version of Python
used to generate them, but the last pre-built wheel was Python 3.10.

## Manual Deployment

After building the packages, manually deploy them with:

```bash
pip install twine
twine upload dist/*
```

Note that this is automatically done through CI/CD.

## Automatic Deployment

This repository contains GitHub CI/CD that enables the automatic building of
source and wheel packages for these gRPC Python interface files. By default,
these are built on PRs, the main branch, and on tags when pushing. Artifacts
are uploaded for each PR.

To publicly release wheels to PyPI, ensure your branch is up-to-date and then
push tags. For example, for the version ``v0.1.2``.

```bash
git tag v0.1.2
git push --tags
```
