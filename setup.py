from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='vimpyre',
      version=version,
      description="Vim Scripts Manager (use pathogen, git, and python!)",
      long_description="""\
              Vim Scripts Manager (use pathogen, git, and python!)

              Actions:
              install, search, remove, update, init, syncdb, remove_all, update_all, list_installed
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='vim python installer',
      author='Daniel Lin',
      author_email='linpct@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plac>=0.7.4',
          'lxml>=2.2',
          'simplejson>=2'
          # -*- Extra requirements: -*-
      ],
      entry_points={
      'console_scripts': [
          'vimpyre = vimpyre.vimpyre:main',
          ],
      },
      )
