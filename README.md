mzml2isa for galaxy
===============

[![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat-square)](http://bioconda.github.io/recipes/mzml2isa/README.html) [![Build Status](https://travis-ci.org/ISA-tools/mzml2isa-galaxy.svg?branch=master)](https://travis-ci.org/ISA-tools/mzml2isa-galaxy)


This is a Galaxy wrapper for the mzml2isa python package tool.

- Full documentation: http://2isa.readthedocs.io/en/latest/
- Python PyPi package: https://pypi.python.org/pypi/mzml2isa/
- Github code: https://github.com/ISA-tools/mzml2isa

mzml2isa is a program that allows you to convert metabolomic studies in .mzML format to the open ISA-Tab standard supported by the MetaboLights database.

Installation
===============

The recommended installation is by means of the toolshed (https://toolshed.g2.bx.psu.edu/). Dependencies should be installed automatically when using Galaxy version >= 16.10. 

The dependencies are dealt with Bioconda. To ensure that Bioconda is working check to make sure the following settings are in the config/galaxy.ini file.

```
# dependencies before each job runs.
conda_auto_install = True
# Set to True to instruct Galaxy to install Conda from the web automatically
# if it cannot find a local copy and conda_exec is not configured.
conda_auto_init = True
```


Licence
===============
GNU General Public License v3 (GPLv3)
