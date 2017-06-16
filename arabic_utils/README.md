## ARABIC UTILITY FUNCTIONS

This folder contains utility functions for Arabic which are important by different functions.
Functions have docstrings attached.
Here below a quick summary of the main functions in the general_utils_arabic.py file.

*Strip Accents function __stripAccents__. Removes the accents from an Arabic string.
	*Code inspired from: 
		*https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string
		*Tanwin Characters from Source code of PyArabic module: https://pypi.python.org/pypi/PyArabic/0.6.2
		*Tanwin Example: https://learnquranicarabic.wordpress.com/2010/07/26/three-types-of-tanwin/
	*Options:
		*tanween_flag: if True, Tanween accents are not removed

*Representation characters conversion function __convertReprFunct__. It converts Arabic characters in their representation function into common Arabic Characters.
