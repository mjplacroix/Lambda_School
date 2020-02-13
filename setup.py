from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata_mjplacroix",
    version="0.1",
    author="Michael LaCroix",
    author_email="michael.jp.lacroix@gmail.com",
    description="Practice Package for LS course",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/mjplacroix/Lambda_School", #TODO
    keywords="practice project",
    packages=find_packages() # ["my_lambdata"]
)