from distutils.core import setup
from setuptools import find_packages

setup(
    name='emdb_schemas',
    version='1.0',
    packages=find_packages(),
    package_dir={'emdb_schemas': 'emdb_schemas/current'},
    package_data={'emdb_schemas': ['emdb.xsd', 'emdb_relaxed.xsd']},
    url='',
    license='',
    author='sanja',
    author_email='sanja@ebi.ac.ik',
    description='EMDB schema files',
    zip_safe=False,
    include_package_data=True
)
