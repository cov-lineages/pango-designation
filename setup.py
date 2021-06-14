from setuptools import setup, find_packages
import glob
import os
import pkg_resources
# Note: the _program variable is set in __init__.py.
# it determines the name of the package/final command line tool.
from pango_designation import __version__, _program

setup(name='pango_designation',
      version=__version__,
      packages=find_packages(),
      scripts=[],
      package_data={'pango_designation':['alias_key.json']},
      description='PANGO lineage designations for SARS-CoV-2',
      url='https://github.com/cov-lineages/pango-designation',
      author='cov-lineages group',
      entry_points="""
      [console_scripts]
      {program} = pango_designation.command:main
      """.format(program = _program),
      include_package_data=True,
      keywords=[],
      zip_safe=False)
