'''Installation file for ansys-api-meshing-prime-v1'''

from setuptools import find_namespace_packages, setup
import os
from ansys.tools.protoc_helper import CMDCLASS_OVERRIDE

HERE = os.path.abspath(os.path.dirname(__file__))

product = 'meshing'
library = 'prime'
package_info = ['ansys', 'api', product, library]
with open(os.path.join(HERE, 'src', 'ansys', 'api', product, library, 'VERSION'), encoding='utf-8') as f:
    version = f.read().strip()

package_name = 'ansys-api-meshing-prime'
dot_package_name = '.'.join(filter(None, package_info))

description = f'Autogenerated python gRPC interface package for {package_name}'

if __name__ == '__main__':
    setup(
        name=package_name,
        version=version,
        author='ANSYS, Inc.',
        author_email='support@ansys.com',
        description=description,
        url=f'https://github.com/ansys/{package_name}',
        license='MIT',
        python_requires='>=3.7, <4',
        install_requires=[
            'grpcio>=1.26.0',  
            'protobuf>=3.12.2, <4',  # minimum required based on meta-package
        ],
        packages=find_namespace_packages('src', include=('ansys.*',)),
        package_dir={'': 'src'},
        package_data={
            '': [ '*.proto', '*.pyi', 'py.typed', 'VERSION' ]
        },
        entry_points={
            'ansys.tools.protoc_helper.proto_provider': [
                f'{dot_package_name}={dot_package_name}'
            ],
        },
        cmdclass=CMDCLASS_OVERRIDE
    )
