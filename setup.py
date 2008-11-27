# -*- coding: utf-8 -*-
# $Id$
import os
from setuptools import setup, find_packages

version = '0.1'

setup(name='collective.collage.feedfeeder',
      version=version,
      description="Add-on that allows displaying RSS-feeds inside a Collage.",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Development Status :: 5 - Production/Stable",
        ],
      keywords='collage plone rss feedfeeder',
      author='Malthe Borch',
      author_email='mborch@gmail.com',
      url='http://www.plone.org/products/collective.collage.feedfeeder',
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
