#!/usr/bin/env python

from distutils.core import setup

setup(name='munipy',
      version='0.2',
      description='NextBus times sent to LED sign',
      license='GNU GPLv3',
      url='https://github.com/cesquivias/muni-led-py',
      packages=['munipy',],
      package_dir={'munipy': 'src'},
      scripts=['bin/munipy'],
      )
