''' setup for pentomino
'''
from setuptools import setup

setup(
    name='pentomino',
    version='1.0',
    packages=['pentomino'],
    python_requires='>=3.11',
    install_requires=[
        'matplotlib',
        'numpy',
        'scikit-image',
        'perftree',
    ]
)
