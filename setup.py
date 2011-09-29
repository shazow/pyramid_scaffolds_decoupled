#!/usr/bin/env python

from distutils.core import setup


try:
    import setuptools
except ImportError, _:
    pass # No 'develop' command, oh well.


version = '1.0'
long_description = open('README.rst').read()

requirements = []
tests_requirements = requirements

setup(name='pyramid_scaffolds_decoupled',
      version=version,
      description="Scaffolds for Pyramid which try to separate web-specific code from the rest so it can be used independently.",
      long_description=long_description,
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          "Framework :: Pylons",
      ],
      author='Andrey Petrov',
      author_email='andrey.petrov@shazow.net',
      license='MIT',
      packages=['pyramid_scaffolds_decoupled'],
      requires=requirements,
      tests_require=tests_requirements,
      )
