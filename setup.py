''' setup for pentomino
python 3.12: Unbewusste Nutzung einiger neuer python-features
'''
from setuptools import setup

setup(
    name='pentomino',
    version='1.0',
    packages=['pentomino'],
    python_requires='>=3.12',
    install_requires=[
        'matplotlib',
        'numpy',
        'scikit-image',
        'perftree',
    ]
)
