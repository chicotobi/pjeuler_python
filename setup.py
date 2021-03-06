import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pjeuler-chicotobi",
    version="0.22.0",
    author="Chicotobi",
    author_email="tobias310788@googlemail.com",
    description="Tools in Python for Project Euler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chicotobi/pjeuler_python",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
