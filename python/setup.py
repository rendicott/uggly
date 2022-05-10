# This is purely the result of trial and error.

import sys

from setuptools import setup, find_packages

import uggly


def long_description():
    with open('../README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name='uggly',
    use_scm_version=True,
    #version=uggly.__version__,
    description=uggly.__doc__.strip(),
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://uggly.bytester.net/',
    download_url=f'https://github.com/rendicott/uggly/python/archive/{uggly.__version__}.tar.gz',
    author=uggly.__author__,
    author_email='rendicott@gmail.com',
    license=uggly.__licence__,
    packages=find_packages(include=['uggly', 'uggly.*']),
    entry_points={
        'console_scripts': [
            'http = uggly.__main__:main',
            'https = uggly.__main__:main',
            'uggly = uggly.manager.__main__:main',
        ],
    },
    python_requires='>=3.7',
    extras_require=extras_require,
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: System :: Networking',
        'Topic :: Terminals',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ],
    project_urls={
        'GitHub': 'https://github.com/rendicott/uggly',
        'Documentation': 'https://uggly.bytester.net/docs',
    },
    data_files=[
        ('share/man/man1', ['extras/man/http.1']),
        ('share/man/man1', ['extras/man/https.1']),
        ('share/man/man1', ['extras/man/uggly.1']),
    ]
)
