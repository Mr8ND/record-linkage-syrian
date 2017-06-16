# Advanced Data Analysis (ADA) Project

This is the repository for the code of the ADA project - Carnegie Mellon Statistics Department, in collaboration with Human Rights Data Analysis Group (HRDAG).

## Getting Started

The repository has three main subfolders:

* [Arabic Soundex](https://github.com/Mr8ND/ada_project/tree/master/arabic_soundex) - Folder dedicated to the implementation and testing of the arabic soundex
* [Arabic Parser](https://github.com/Mr8ND/ada_project/tree/master/arabic_names_parser) - Folder dedicated to the implementation and testing of the arabic parser
* [Arabic Utils](https://github.com/Mr8ND/ada_project/tree/master/arabic_utils) - Folder dedicated to general functions useful to deal with arabic characters and string.

The functions in main.py file are functions used to retrieve language agnostic features from strings - same for the functions in utils.py

### Prerequisites

Code has been written in Python 2.7.
Only "unittest2" would need to be installed as extra packages and it is imported in the following way when testing is needed:

```
import unittest2 as unittest
```

All files are coded in "utf-8" to support the unicode characters for Arabic.


## Running the tests

The "test" folder are where the tests are contained for each subfolder and for the main functions.
The tests are meant to be run within the folder - i.e. you should have to cd into the "test" folder in order to run the tests.

Tests are commented within the test files.
Names used are synthetical and do not represent any real individual.

## Authors

* **Nic Dalmasso**

## Acknowledgments

* Jared Murray, Jordan Rodu and Robin Mejia for pivotal feedbacks and discussions
* HRDAG
