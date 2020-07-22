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
    name="categorize", 
    version="0.1.0",
    description="Categorize is a simple, customizable CLI-tool for automation sorting your files by their extensions.",
    long_description=open(README).read(),
    long_description_content_type='text/markdown',
    author="Dobryakov David",
    author_email="kantegory@etersoft.ru",
    url="https://github.com/kantegory/categorize",
    license="ISC",
    packages=['categorize'],
    entry_points={
        "console_scripts": [
            "categorize = categorize.sorter:main",
            "categorize-config = categorize.config:main",
        ]
    },
    classifiers=classifiers_list,
    include_package_data=True
)
