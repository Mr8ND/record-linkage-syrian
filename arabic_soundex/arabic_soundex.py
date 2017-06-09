# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
sys.path.append("../..")
from arabic_utils.general_utils_arabic import strip_accents
from arabic_names_parser.parser_utils import Astr, readjustSpacesInString

lookup_dict = {'\u0627\u0623\u0625\u0622\u062d\u062e\u0647\u0639\u063a\u0634\u0648\u064a\u0621': '0',
			   '\u0641\u0628\u0649': '1',
			   '\u062c\u0632\u0633\u0635\u0638\u0642\u0643': '2',
			   '\u062a\u062b\u062f\u0630\u0636\u0637\u0629': '3',
			   '\u0644': '4',
			   '\u0645\u0646': '5',
			   '\u0631': '6'
			   }

lookup_dict_arab = {u'ا': 0, u'أ': 0, u'إ': 0, u'آ': 0, u'ح': 0, u'خ': 0, u'ه': 0, u'ع': 0, u'غ': 0, u'ش': 0, u'و': 0, u'ي': 0, u'ء': 0,
                	u'ف': 1, u'ب': 1, u'ى': 1,
                    u'ج': 2, u'ز': 2, u'س': 2, u'ص': 2, u'ظ': 2, u'ق': 2, u'ك': 2,
                	u'ت': 3, u'ث': 3, u'د': 3, u'ذ': 3, u'ض': 3, u'ط': 3, u'ة':3,
                	u'ل': 4, 
                	u'م': 5, u'ن': 5,
                	u'ر': 6
                	}


def emptyStringError(arab_str):
	'''
	This function throws a TypeError when the input string is empty.
	'''
	if not arab_str:
		raise TypeError('The string passed into this function needs to be non-empty')
	else:
		pass


def arabic_soundex_main(arab_str, firstcharuniforming=True, firstletter_rem=True, accents_strip=True, lim=3):
	'''
	This is the main function for the soundex, and it has been coded thinking about a single word being passed as
	argument. Although, as soon as the string is not empty, it will also work for strings with more than one word
	in it.

	INPUT
	- arab_str: the string in arabic. Usually one arabic word, but can be multiple
	- firstcharuniforming: a logical flag. Heuristically the first character seems not to play an important role
		into the arabic soundex, if this flag is true then the first character is uniformly set to be a 'x'
		independently of the character
	- firstletter_rem: a logical flag. From a sound point of view, in arabic there are certain initial characters
		that are not pronounced when they are at the beginning of a sentence. The soundex removes them from the string
		if firstletter_rem is set to true
	- accents_strip: a logical flag. If true, removes the accents from the string
	- lim: numerical, integer. If not None, forces the soundex representation to be composed a number of numbers or
		characters equal to lim after the first character. If the soundex representation was longer, this would cut it.
		If it was shorter, it would fill the spaces with 0. E.g. with lim=3 : x7213 is set to x721 and x7 to x700.

	OUTPUT
	- transp: soundex representation of the arabic string.
	'''

	emptyStringError(arab_str)

	if isinstance(arab_str, str):
		arab_str = Astr(arab_str)

	if accents_strip:
		arab_str = strip_accents(arab_str)


	# The first thing to do is to exclude the first letter in the firstletter_rem option is activated.
	# This apparently improves the performances of the soundex, according  to Tamman Koujian's C# version of 
	# this soundex.

	if firstletter_rem and arab_str[0] in [u'\u0627',u'\u0623',u'\u0625',u'\u0622']:
		arab_str = arab_str[1:]


	# Now we need to convert the string into the relative sound.
	# Again according to Tamman Koujian's C# version, the first letter is not useful.
	# It firstcharpruning is True, than this happens, otherwise it does not.

	transp = ''
	if firstcharuniforming:
		transp += 'x'
	else:
		transp += arab_str[0]


	# We now proceed to the transposition.

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

	# Lim is a parameter which limits the total length of a soundex word.
	# If this is in place then the word is limited with a length which is equal to lim + 1
	# which implies the first letter + first 3 numbers/letters

	if lim:
		lim = lim +1
		n_transp = len(transp)
		transp = transp[:lim] if len(transp) >= lim else transp+ ''.join(['0' for x in range(lim-n_transp)])

	return transp


def arabic_soundex_names(arab_str, *args, **kwargs):
	'''
	This function is just a wrapper for the main arabic soundex function, which is arabic_soundex_main.
	This function checks whether the string is empty, readjust the spaces and then gets a soundex representation
	of the string word by word.

	INPUT:
	- arab_str: the arabic string, thought to be a multi-words string here
	- *args, **kwargs: arguments to be passed into the main arabic soundex function

	OUTPUT:
	- A word by word soundex representation of the string
	'''

	emptyStringError(arab_str)

	arab_str = readjustSpacesInString(arab_str)

	soundex_repr = []
	for arabname_part in arab_str.split(' '):
		soundex_repr.append(arabic_soundex_main(arabname_part,*args, **kwargs))

	return ' '.join(soundex_repr)


if __name__ == '__main__':
	print arabic_soundex_names(u'محمد')
