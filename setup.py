# -*- coding: utf-8 -*-
# $Id$
import os
from setuptools import setup, find_packages

version = '1.1.dev0'

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except:  # doesn't work under tox/pip
    # Note: I wonder is that was because we tried to open CHANGES.rst
    # when the file was called CHANGES.txt.
    README = ''
    CHANGES = ''

setup(name='collective.collage.feedfeeder',
      version=version,
      description="Collage add-on that allows displaying RSS-feeds.",
      long_description="\n\n".join((README, CHANGES)),
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Development Status :: 5 - Production/Stable",
        ],
      keywords='collage plone rss feedfeeder',
      author='Malthe Borch',
      author_email='mborch@gmail.com',
      url='https://github.com/collective/collective.collage.feedfeeder',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.collage'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.Collage',
          'Products.feedfeeder',
          # -*- Extra requirements: -*-
      ],
      )
