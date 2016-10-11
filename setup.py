from setuptools import setup
from cg import __version__

setup(
    name="Clebsh-Gordan",
    author="Olav Vahtras",
    author_email="olav.vahtras@gmail.com",
    version=__version__,
    url="https://github.com/vahtras/cg",
    py_modules=["cg"],
    install_requires=["numpy"],
)
