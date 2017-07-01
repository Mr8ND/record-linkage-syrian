# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

from arabic_names_parser.parser_utils import Astr, readjustSpacesInString

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


def convertReprFunction(s):
	'''
	This function is a lookup function for representation characters in unicode. Arabic a series of different characters, which can be translated in common arabic. The function replaces these	characters with common arabic characters.

	INPUT
	s: unicode string. It does not have to be in Arabic, but the function will likely not to do	anything othwewise

	OUTPUT
	The same string in which every character which was in its representation form has been translated to its common arabic character.
	'''

	if isinstance(s, str):
		s = Astr(s)
		
	output = ''
	for i,xpart in enumerate(s):
		flag = False
		for k,v in arabic_forms_toclassic_lookup.iteritems():
			if xpart in k and not flag:
				output += v
				flag = True
		if not flag:
			output += xpart
	return output


def nameCleanerFunction(s):
	'''
	This function is just a wrapper for two other functions, such that the names gets its spaces adjusted first and also the representation function unicode characters replaced afterward as well.

	INPUT:
	s: unicode string, expected to be in the Arabic range

	OUTPUT:
	The same string in which spaces are adjusted (one space only between words) and representation forms are not included.
	'''
	return convertReprFunction(readjustSpacesInString(s))
