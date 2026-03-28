from setuptools import setup, find_packages

setup(
    name="pic2pola",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Pillow>=12.1.1",
    ],
    entry_points={
        'console_scripts': [
            'pic2pola=src.main:main',
        ],
    },
    python_requires='>=3.11',
)
