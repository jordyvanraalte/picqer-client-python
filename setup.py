import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="piqcer-client-jordyvanraalte",
    version="0.0.1",
    author="Jordy van Raalte",
    author_email="j.j.c.van.raalte@gmail.com",
    description="This package provides a picqer client which can be used in order to contact the piqcer API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jordyvanraalte/piqcer-client-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)