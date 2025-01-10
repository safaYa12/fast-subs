from setuptools import setup, find_packages

setup(
    name='fast-subs',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pyfiglet',
    ],
    entry_points={
        'console_scripts': [
            'fast-subs=fastsubs.main:run',
        ],
    },
)
