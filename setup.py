from setuptools import setup, find_packages
import glob
import os
import pkg_resources
from version import __version__, _program

setup(name='pango-designation',
      version=__version__,
      packages=find_packages(),
      scripts=[],
      package_data={'pango-designation':['alias_key.json']},
      description='PANGO lineage designations for SARS-CoV-2',
      url='https://github.com/cov-lineages/pango-designation',
      author='cov-lineages group',
      entry_points="""
      [console_scripts]
      {program} = pango-designation.command:main
      """.format(program = _program),
      include_package_data=True,
      keywords=[],
      zip_safe=False)
