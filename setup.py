from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup (
    name="spotifystats",
    version="0.1.0",
    author="Bernardo Jordão",
    author_email="bernardo.jordao@tecnico.ulisboa.pt",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        "pymongo",
        "spotipy"
    ],
    entry_points={
        "console_scripts": [
            "spotifystats = spotifystats:main"
        ]
    }
)