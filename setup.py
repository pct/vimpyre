from setuptools import setup, find_packages

version = '0.2.7'

setup(name='vimpyre',
      version=version,
      description="Vim Scripts Manager (use pathogen, git, and python!)",
      long_description=open('README.rst').read(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='vim scripts manager',
      author='Daniel Lin',
      author_email='linpct@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests', 'README.rst']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plac>=0.7.4',
          'requests>=1.1.0',
          # -*- Extra requirements: -*-
      ],
      entry_points={
      'console_scripts': [
          'vimpyre = vimpyre.console:main',
          ],
      },
      )
