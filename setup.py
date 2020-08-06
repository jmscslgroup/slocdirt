import setuptools
from distutils.dir_util import copy_tree

PACKAGE_NAME='strym'
import shutil, os
shutil.copy('README.md', PACKAGE_NAME + '/README.md')

copy_tree('./examples', PACKAGE_NAME + '/examples')

def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description

setuptools.setup(
    name='strym',
    version='0.1.13',
    author="Rahul Bhadani",
    author_email="rahulbhadani@email.arizona.edu",
    description="A real time CAN data logging and visualization tool to work with USB-CAN Interface.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/jmscslgroup/strym",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'matplotlib>=3.0.3',
        'cantools>=32.20.1',
        'libusb1>=1.7.1',
        'pyserial>=3.4',
        'seaborn>=0.9.0',
        'ipython',
        'Sphinx==2.4.4',
        'bitstring>=3.1.6',
        'sphinx_rtd_theme',
        'sphinx_autodoc_typehints',
        'recommonmark',
        'pandas',
        'rinohtype',
        'pathlib',
        'ytsphinx',
        'mkdocs',
        'sphinx_bootstrap_theme',
        'sphinx-markdown-parser',
        'pymdown-extensions',
        'm2r',
        'gmplot',
        'gmaps',
        'googlemaps',
        'python-dotenv',
        'bokeh',
        'selenium',
        'webdriver-manager',
        'vin_parser',
        'tensorflow==2.2.0',
        'sphinxcontrib-fulltoc'
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: AsyncIO",
        "Topic :: Communications",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: MIT License",
        ],
    keywords='candata, can, autonomous vehicle, ACC, adaptive cruise control, USB, Panda, Traffic, Transportation, visualization',
    include_package_data=True,
    package_data={'strym': ['README.md', 'examples/*.*']},
    zip_safe=False
        )

os.remove('strym/README.md')
shutil.rmtree(PACKAGE_NAME + '/examples')
