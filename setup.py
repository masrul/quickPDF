from setuptools import setup

setup(
    name="quickPDF",
    version="0.1.0",
    description="A python toolkit to fit potential energy surface data",
    url="https://github.com/masrul/quickPDF",
    author="Masrul Huda",
    author_email="mmh568@msstate.edu",
    packages=["quickPDF"],
    install_requires=["numpy>=1.14",  "matplotlib>3.0"],
    python_requires=">=3.7",
    classifiers=[
        "Intended Audience :: General",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points = {
        'console_scripts': ['quickPDF=quickPDF.quickPDF:main'],
    }
)
