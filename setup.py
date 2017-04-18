#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


# TODO:
#   - Update license information in "classifiers"
#   - Need a license file?

setup(name="acq400_hapi",

      version='0.1',

      description='acq400_hapi',

      url="https://github.com/petermilne/acq400_hapi",

      classifiers=[
          'Development Status :: 4 - Beta',

          'Operating System :: MacOS :: MacOS X',
          'Operating System :: POSIX :: Linux',
          'Operating System :: Microsoft :: Windows',

          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Physics',

          'License :: Other/Proprietary License',

          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
      ],

      setup_requires=["numpy"],

      test_requires=['pytest'],

      ext_package="acq400_hapi",

      packages=find_packages(exclude=['tests']),

     )
