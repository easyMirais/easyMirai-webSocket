from setuptools import setup, find_packages
import easyMirais

setup(
    name="easyMirai-websocket",
    version=easyMirais.__version__(),
    author="HexMikuMax & ExMikuPro",
    author_email="sfnco-miku@outlook.com",
    python_requires=">=3.6.0",
    packages=find_packages(),
    license="GPLv3",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    project_urls={
        "Documentation": "https://easyMirai-websocket.readthedocs.io",
        "Source": "https://github.com/easyMirais/easyMirai-webSocket",
    },
)
