from setuptools import setup

requires = ['bcrypt']

setup(
    name = "nc30-dummiy",
    version = '0.0.1',
    install_requires = requires,
    author = 'Himura Asahi',
    author_email = 'himura@nitolab.com',
    packages = ["dummies"],
    description = "generate dummy string",
    url = "https://github.com/nc30/nc30-dummy"
)

