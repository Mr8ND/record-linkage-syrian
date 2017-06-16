## ARABIC NAME PARSER

This folder contains the code for the arabic parser, which is contained in arabic_parser.py.

* __arabicNameParser__ - main arabic name parser function.
	*  Principal *args and **kwargs are:
		* name_dict: imported by default from parser_objs.py, includes the words in Arabic which indicates the beginning of a particular name part;
		* conc_list: imported by default from parser_objs.py, includes the words which have to be traslated with the next word as a single word in Arabic names;
		* print_flag: if True, the parser will print whether certain characters in the string are not in Arabic. Defaulted to True.

The file parser_objs.py contains different objects useful for the arabic parser to run as a standalone function.

The file parser_utils.py contains utility functions for the Arabic parser to run. Main functions are:

* __Astr__ - function which encodes in utf-8 the string if it has not already been converted;
* __isolateNextWordDictKeys__ - use to understand which words follow and are before a word which is identified as flag of a specific name part;
* __concatenateFunction__ - use to attach together the words which needs to be translated with the following word to be considered as a name. E.g. "Mr. Red" will be considered as a single word, even though "Mr." and "Red" are two separate words.


### TESTING
The test folder here works a bit differently.
The file to be run is the main_test.py files, which is going to import a series of tests from the tests.py file, for each of the namepart being tested.
