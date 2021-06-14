from setuptools import setup, find_packages
import glob
import os
import pkg_resources
from pango_designation import __version__, _program

setup(name=_program,
      version=__version__,
      package_data={'':['alias_key.json']},
      description='PANGO lineage designations for SARS-CoV-2',
      url='https://github.com/cov-lineages/pango-designation',
      author='cov-lineages group',
      include_package_data=True,
      zip_safe=False)
