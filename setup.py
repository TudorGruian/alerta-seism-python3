import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alertaseism",
    version="0.0.5",
    author="Tudor Gruian",
    author_email="gruiantudor@hotmail.com",
    description="O librarie folosiind date XML de la INFP pentru a afla magnitudinea la secunda. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TudorGruian/alerta-seism-python3",
    packages=['alertaseism'],
    install_requires=[
        "beautifulsoup4",
        "requests",
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
