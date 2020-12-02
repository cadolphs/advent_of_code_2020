from setuptools import setup, find_packages

packages = find_packages(where=".")

setup(packages=packages, package_dir={"":"."})
