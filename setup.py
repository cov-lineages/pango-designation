from setuptools import setup, find_packages
import glob
import os
import pkg_resources
from version import __version__

setup(name='pango_designation',
      version=__version__,
      packages=find_packages(),
      scripts=[],
      package_data={'aliases':['alias_key.json']},
      description='PANGO lineage designations for SARS-CoV-2',
      url='https://github.com/cov-lineages/pango-designation',
      author='cov-lineages group',
      include_package_data=True,
      keywords=[],
      zip_safe=False)
