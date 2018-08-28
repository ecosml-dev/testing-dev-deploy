import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "testing_dev_deploy",
    # update version whenever you create a new release
    version = "{{version}}",
    author = "jrmerz",
    description = ("this is a test, this is only a test"),
    license = "MIT",
    keywords = "",
    url = "http://localhost:3000/package/17839221-e174-4368-a40a-75c43d78c4bc",
    packages=[
        'testing_dev_deploy',
        'testing_dev_deploy.main'
    ],
    package_data={
      'testing_dev_deploy' : ['resources/*']
    },
    long_description=read('README.md'),
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
)