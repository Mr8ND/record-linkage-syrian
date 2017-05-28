# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from arabic_utils.general_utils_arabic import strip_accents

lookup_dict = {'\u0627\u0623\u0625\u0622\u062d\u062e\u0647\u0639\u063a\u0634\u0648\u064a': '0',
			   '\u0641\u0628': '1',
			   '\u062c\u0632\u0633\u0635\u0638\u0642\u0643': '2',
			   '\u062a\u062b\u062f\u0630\u0636\u0637': '3',
			   '\u0644': '4',
			   '\u0645\u0646': '5',
			   '\u0631': '6'
			   }

lookup_dict_arab = {u'ا': 0, u'أ': 0, u'إ': 0, u'آ': 0, u'ح': 0, u'خ': 0, u'ه': 0, u'ع': 0, u'غ': 0, u'ش': 0, u'و': 0, u'ي': 0,
                	u'ف': 1, u'ب': 1,
                    u'ج': 2, u'ز': 2, u'س': 2, u'ص': 2, u'ظ': 2, u'ق': 2, u'ك': 2,
                	u'ت': 3, u'ث': 3, u'د': 3, u'ذ': 3, u'ض': 3, u'ط': 3,
                	u'ل': 4, 
                	u'م': 5, u'ن': 5,
                	u'ر': 6
                	}

def Astr(string):
	'''
	This function encodes in utf-8 a ASCII string with Arabic character in order for it to be
	compatible with the string formatting in Python.

	INPUT
	string - ASCII string with arabic characters

	OUTPUT
	The input string encoded with utf-8
	'''

	return unicode(string, encoding='utf-8')


def arabic_soundex_main(arab_str, firstcharuniforming=True, firstletter_rem=True):

	if not arab_str:
		print 'The string passed into this function needs to be non-empty'
		raise TypeError

	if isinstance(arab_str, str):
		arab_str = Astr(arab_str)

	arab_str = strip_accents(arab_str)


	#The first thing to do is to exclude the first letter in the firstletter_rem option is activated.
	#This apparently improves the performances of the soundex, according  to Tamman Koujian's C# version of 
	#this soundex.


	if firstletter_rem and arab_str[0] in '\u0627\u0623\u0625\u0622':
		arab_str = arab_str[1:]


	#Now we need to convert the string into the relative sound.
	#Again according to Tamman Koujian's C# version, the first letter is not useful.
	#It firstcharpruning is True, than this happens, otherwise it does not.

	transp = ''
	if firstcharuniforming:
		transp += 'x'
	else:
		transp += arab_str[0]


	#We now proceed to the transposition.

	def charInDictKeys(char, dict_chars):
		keys_unicode = [x for x in dict_chars.keys()]
		pos_vec = [1 if char in x else 0 for x in keys_unicode]
		return dict_chars.keys()[pos_vec.index(1)] if sum(pos_vec)>0 else None


	code, prevcode = None, None
	if len(arab_str)>1:
		for char in arab_str[1:]:

			key = charInDictKeys(char, lookup_dict_arab)

			if key and lookup_dict_arab[key]!='0': code = str(lookup_dict_arab[key])
			else: code = char

			if code != prevcode:
				transp += code
				prevcode = code

	return transp


if __name__ == '__main__':
	print arabic_soundex_main(Astr('ًالسلميٌلسلميٍٍٍلسلمي'))
