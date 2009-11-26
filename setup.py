from setuptools import setup, find_packages
import os

version = '0.2'

setup(name='chaoflow.testing.ipython',
      version=version,
      description="User ipython interactively in your doctest",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers = [
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Testing',
          ],
      keywords='',
      author='Florian Friesdorf',
      author_email='flo@chaoflow.net',
      url='http://github.com/chaoflow/chaoflow.testing.ipython',
      license='LGPL',
      packages = find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['chaoflow','chaoflow.testing'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'ipython',
      ],
      extras_require={
          'test': [
              'chaoflow.testing.crawler',
              ],
          },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
