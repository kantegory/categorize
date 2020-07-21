import os
from setuptools import setup

classifiers_list = [
    "Development Status :: 4 - Beta",
    "Environment :: Plugins",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3.6",
    "Topic :: System",
    "Topic :: Utilities",
    {
        "alpha": "Development Status :: 3 - Alpha",
        "beta": "Development Status :: 4 - Beta",
        "stable": "Development Status :: 5 - Production/Stable"
    }["alpha"]
]

README = os.path.join(os.path.dirname(__file__), "README.md")

setup(
    name="file-sorter", 
    version="0.1.0",
    description="File sorter is a simple tool for automation sorting your files by their extensions.",
    long_description=open(README).read(),
    author="Dobryakov David",
    author_email="kantegory@etersoft.ru",
    url="https://github.com/kantegory/file-sorter",
    license="ISC",
    packages=['file_sorter'],
    entry_points={
        "console_scripts": [
            "file-sorter = file_sorter.file_sorter:main",
            "file-sorter-config = file_sorter.config:main",
        ]
    },
    classifiers=classifiers_list,
    include_package_data=True
)
