import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
LICENSE = (HERE / "LICENSE.md").read_text()

setup(
    name="cdas",
    version="0.0.1",
    description="Cybersecurity Decision Analysis Simulator",
    long_description=README,
    long_description_content_type="text/markdown",
    license=LICENSE,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["cdas"],
    include_package_data=True,
    package_data = {
        'cdas': ['config.json','data/*']
    },
    install_requires=["numpy","reportlab","drawSVG","stix"],
    entry_points={
        "console_scripts": [
            "cdas=cdas.__main__:main",
        ]
    },
)