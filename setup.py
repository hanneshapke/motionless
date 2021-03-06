#!/usr/bin/python

__author__ = 'Ryan Cox <ryan.a.cox@gmail.com>'
__version__ = '1.1'

test_requirements = [
    # TODO: put package test requirements here
]

# Distutils version
METADATA = dict(
    name = "motionless",
    version = __version__,
    py_modules = ['setup', 'motionless'],
    author = 'Ryan Cox',
    author_email = 'ryan.a.cox@gmail.com',
    description = 'An easy way to generate Google Static Map URLs with Python.',
    license = 'Apache 2.0 License',
    url = 'http://github.com/ryancox/motionless',
    keywords = 'google static maps url api georss mapping gpx kml geo gis',
    test_suite='tests',
    tests_require=test_requirements,
)

# Setuptools version
SETUPTOOLS_METADATA = dict(
    install_requires = ['setuptools'],
    include_package_data = True,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
                'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Internet',
    ]
)

def Main():
    try:
        import setuptools
        METADATA.update(SETUPTOOLS_METADATA)
        setuptools.setup(**METADATA)
    except ImportError:
        import distutils.core
        distutils.core.setup(**METADATA)

if __name__ == '__main__':
  Main()
