#!/usr/bin/env python
from setuptools import setup, find_packages
import sys, os
from babel.messages import frontend as babel
version = '0.00000000000001'

setup(name='nnmon',
      version=version,
      description="A network neutrality bugtracker",
      long_description="""reporting platform for the nnmon project""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='network-neutrality reporting form',
      author='Stefan Marsirske',
      author_email='stefan.marsiske@gmail.com',
      url='http://nnmon.lqdn.fr',
      license='AGPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      cmdclass = {'compile_catalog': babel.compile_catalog,
         'extract_messages': babel.extract_messages,
         'init_catalog': babel.init_catalog,
         'update_catalog': babel.update_catalog},
      )
