from distutils.core import setup
from setuptools import find_packages

setup(
    name='emdb_schemas',
    version='1.0',
    packages=find_packages(),
    package_dir={'current': 'emdb_schemas/current'},
    package_data={'current': ['emdb.xsd', 'emdb.py', 'emdb_relaxed.xsd', 'emdb_relaxed.py']},
    url='',
    license='',
    author='sanja',
    author_email='sanja@ebi.ac.ik',
    description='EMDB schema files',
    zip_safe=False
)
