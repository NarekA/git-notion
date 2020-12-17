#!/usr/bin/env python

from setuptools import setup, find_packages
import os

base_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join('requirements.in')) as f:
    requirements = [l.strip() for l in f.readlines() if l.strip()]

with open(os.path.join(base_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="NarekA",
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Syncs Github Mmarkdown files to Notion",
    entry_points={
        'console_scripts': [
            'git-notion=git_notion.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='git_notion',
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='git_notion',
    packages=find_packages(include=['git_notion', 'git_notion.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/NarekA/git-notion',
    version='0.2.3',
    zip_safe=False,
)
