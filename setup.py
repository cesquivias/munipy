#!/usr/bin/env python

from distutils.core import setup

setup(name='led_sign',
      version='0.1',
      description='NextBus times sent to LED sign',
      license='GNU GPLv3',
      url='https://github.com/cesquivias/muni-led-py',
      packages=['munipy',],
      package_dir={'munipy': 'src'},
      scripts=['bin/munipy'],
      )
