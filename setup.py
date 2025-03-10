from setuptools import setup, find_packages

setup(
    name="Pipeline",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="*",
    author_email="*",
    description="OCR Package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Atef-Magdy/OCR_Module",
    classifiers=[
        "Programming Language :: Python :: 3.6^",
    ],
    python_requires='>=3.6',
)