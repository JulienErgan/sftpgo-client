from setuptools import setup, find_packages


def get_description():
    with open("README.md") as file:
        return file.read()


setup(
    name="sftpgo-client",
    version="0.3.1",
    url="https://github.com/ramnes/sftpgo-client",
    author="Guillaume Gelin",
    author_email="contact@ramnes.eu",
    description="Python client for the SFTPGo API",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.6, <4",
    install_requires=[
        "httpx >= 0.15.0, < 0.18.0",
        "attrs >= 20.1.0",
        "python-dateutil >= 2.8.0, < 3",
    ],
    package_data={"sftpgo_client": ["py.typed"]},
)
