from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='vimpyre',
      version=version,
      description="Vim scripts installer written in python",
      long_description="""\
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
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
