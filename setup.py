#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('requirements.in') as f:
    requirements = [l.strip() for l in f.readlines() if l.strip()]

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
    name='git_notion',
    packages=find_packages(include=['git_notion', 'git_notion.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/NarekA/git-notion',
    version='0.2.0',
    zip_safe=False,
)
