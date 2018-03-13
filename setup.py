from distutils.core import setup

setup(name='mockserver',
      version='1.0',
      py_modules=['mockserver'],
      tests_require=[
          'pytest',
      ],
      )
