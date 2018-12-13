import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "yypget",
    version = "0.0.1",
    author = "ysouyno",
    author_email = "ysouyno@163.com",
    description = "Download online video from the web",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ysouyno/yypget",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
