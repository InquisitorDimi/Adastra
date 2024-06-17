from setuptools import setup, find_packages

setup(
    name='MovieDataset',
    version='0.1.0',
    description='Package for analyzing movie datasets.',
    packages=find_packages(),
    author="Dimitar Ivanov",
    install_requires=[
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'movie-dataset=main:main',
        ],
    },
)
