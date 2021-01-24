import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyViFlag",
    version="1.0.2",
    author="Stylix58Alt",
    author_email="lateman-jpeg@outlook.fr",
    description="A unofficial Python API wrapper for Flag.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Stylix58/pyviflag",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)