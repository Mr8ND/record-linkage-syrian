# -*- coding: utf-8 -*-

import sys
import unicodedata
sys.path.append("..")

from arabic_names_parser.parser_utils import Astr

# Arabic representation form to classic Arabic lookup table, just for reference.
arabic_forms_toclassic_lookup = {u'ﺀﺁﺂﺃﺄﺅﺆﺇﺈﺉﺊﺋﺌﺍﺎ':u'ا',
								u'ﺏﺐﺑﺒ':u'ب',
								u'ﺓﺔ':u'ه',
								u'ﺕﺖﺗﺘ':u'ت',
								u'ﺙﺚﺛﺜ':u'ث',
								u'ﺝﺞﺟﺠ':u'ج',
								u'ﺡﺢﺣﺤ':u'ح',
								u'ﺥﺦﺧﺨ':u'خ',
								u'ﺩﺪ':u'د',
								u'ﺫﺬ':u'ذ',
								u'ﺭﺮ':u'ر',
								u'ﺯﺰ':u'ز',
								u'ﺱﺲﺳﺴ':u'س',
								u'ﺵﺶﺷﺸ':u'ش',
								u'ﺹﺺﺻﺼ':u'ص',
								u'ﺽﺾﺿﻀ':u'ض',
								u'ﻁﻂﻃﻄ':u'ط',
								u'ﻅﻆﻇﻈ':u'ظ',
								u'ﻉﻊﻋﻌ':u'ع',
								u'ﻍﻎﻏﻐ':u'غ',
								u'ﻑﻒﻓﻔ':u'ف',
								u'ﻕﻖﻗﻘ':u'ق',
								u'ﻙﻚﻛﻜ':u'ك',
								u'ﻝﻞﻟﻠ':u'ل',
								u'ﻡﻢﻣﻤ':u'م',
								u'ﻥﻦﻧﻨ':u'ن',
								u'ﻩﻪﻫﻬ':u'ه',
								u'ﻭﻮ':u'و',
								u'ﻯﻰﻱﻲﻳﻴ':u'ي',
								u'ﻵﻶﻷﻸﻹﻺﻻﻼ':u'لا'}


tanwin_vec = (Astr('ً'), Astr('ٌ'), Astr('ٍ'))

def strip_accents(s, tanween_flag=False):
	'''
	This function takes any unicode string and strips the accents. As this function has been created with arabic in mind, if the
	tanween_flag is True, it will normalize all accents apart from tanween accents.

	INPUT
	- s : this is the unicode string. The function was thought for arabic strings, but it could be any strings
	- tanween_flag : whether tanween accents should be excluded from normalization or not

	OUTPUT
	The string normalized from accents, excluding tanween if tanween_flag is True.
	'''

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