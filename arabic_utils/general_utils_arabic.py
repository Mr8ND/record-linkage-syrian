# -*- coding: utf-8 -*-

import sys
import unicodedata
sys.path.append("..")

from arabic_names_parser.parser_utils import Astr


tanwin_vec = (Astr('ً'), Astr('ٌ'), Astr('ٍ'))


def strip_accents(s, tanween_flag=False):

	if isinstance(s, str):
		s = Astr(s)

	if tanween_flag:
		tanween_vec = [1 if c in tanwin_vec else 0 for c in s]
		return ''.join(unicodedata.normalize('NFD', c) if (unicodedata.category(c) != 'Mn' and tanween_vec[i]==0) else c for i,c in enumerate(s))
	else:
		return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def test_stripfunction():
	#Tests taken from the examples at https://learnquranicarabic.wordpress.com/2010/07/26/three-types-of-tanwin/

	test_vec = (('محمدٌ','محمدٌ', 'محمد'), ('محمدٍ','محمدٍ','محمد'), ('محمداً','محمداً','محمدا'))

	for orig_str, tanw_str, stri_str in test_vec:
		print Astr(tanw_str) == strip_accents(orig_str, tanween_flag=True)
		print Astr(stri_str) == strip_accents(orig_str)


if __name__ == '__main__':
	test_stripfunction()