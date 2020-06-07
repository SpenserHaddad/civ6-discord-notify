from os import path
import setuptools

local_file_path = path.abspath(path.dirname(__file__))

with open(path.join(local_file_path, "README.md")) as f:
    long_description = f.read()

setuptools.setup(
    name="civ6-notify",
    version="0.0.1",
    author="Spenser Haddad",
    author_email="spenser.haddad@gmail.com",
    description="Notify players on Discord when it's their turn in a Civ VI Play-by-Cloud game",  # noqa: E501
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SpenserHaddad/civ6-discord-notify",
    packages=setuptools.find_namespace_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 3.8",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Turn Based Strategy",
    ],
    python_requires=">=3.8",
    install_requires=["quart", "discord.py", "click"],
    extras_require={"dev": ["black", "flake8", "mypy"]},
    entry_points={"console_scripts": ["civ6-notify = civ6_notify.cli:main"]},
)
