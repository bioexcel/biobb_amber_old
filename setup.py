import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_md",
    version="0.0.2",
    author="Biobb developers",
    author_email="pau.andrio@bsc.es",
    description="Biobb_md is the Biobb module collection to perform molecular dynamics simulations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Bioinformatics Workflows BioExcel Compatibility",
    url="https://github.com/bioexcel/biobb_md",
    project_urls={
        "Documentation": "http://biobb_md.readthedocs.io/en/latest/",
        "Bioexcel": "https://bioexcel.eu/"
    },
    packages=setuptools.find_packages(exclude=['docs', 'test', 'cwl','notebooks',]),
    install_requires=['biobb_common'],
    python_requires='~=3.6',
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
    ),
)