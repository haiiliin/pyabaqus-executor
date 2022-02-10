import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyabaqus-executor",
    version="1.0.13",
    author="WANG Hailin",
    author_email="hailin.wang@connect.polyu.hk",
    description="Abaqus Executor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Haiiliin/.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=setuptools.find_packages()
)
