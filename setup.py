from setuptools import setup, find_packages

setup(
    name="panda_math",  # Must be unique on PyPI
    version="0.1.1",
    packages=find_packages(),
    install_requires=["numpy"],
    author="Colin Politi",
    author_email="urboycolinthepanda@gmail.com",
    description="A Vector, Matrix, and transformation utilities for 2D, 3D graphics, and game development.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ColinThePanda/panda_math",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
