import re
from setuptools import setup, find_packages


setup(
    name='dateparser',
    version="1.0.0-el2",
    description='Date parsing library designed to parse dates from HTML pages',
    long_description="forked version of dateparser for threading",
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    install_requires=[
        'python-dateutil',
        'pytz',
        # https://bitbucket.org/mrabarnett/mrab-regex/issues/314/import-error-no-module-named
        'regex !=2019.02.19',
        'tzlocal',
    ],
    extras_require={
        'calendars:python_version<"3.6"': ['convertdate'],
        'calendars:python_version>="3.6"': ['hijri-converter', 'convertdate'],
    },
    license="BSD",
    zip_safe=False,
    keywords='dateparser',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
