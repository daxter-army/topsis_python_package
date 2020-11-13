from setuptools import setup, find_packages

def readme():
    with open('readme.md') as f:
        README = f.read()
    return README

setup(
    name = "calctopsis",
    version = "0.0.1",
    license = "MIT",
    description = "A Python package to find TOPSIS for multi-criteria decision analysis method",
    long_description = readme(),
    long_description_content_type = "text",
    author = "Mehul Singh Teya",
    author_email = "mehulsinghteya@gmail.com",
    url = "https://github.com/daxter-army/topsis_python_package",
    keywords = ['topsis', 'UCS538', 'TIET'],
    install_requires = [
        'pandas',
        'tabulate'
    ],
    include_package_data = True,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Student Developers',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3' 
    ]
)