# -*- coding: utf-8 -*-

lookup_dict = {'\u0627\u0623\u0625\u0622\u062d\u062e\u0647\u0639\u063a\u0634\u0648\u064a': '0',
			   '\u0641\u0628': '1',
			   '\u062c\u0632\u0633\u0635\u0638\u0642\u0643': '2',
			   '\u062a\u062b\u062f\u0630\u0636\u0637': '3',
			   '\u0644': '4',
			   '\u0645\u0646': '5',
			   '\u0631': '6'
			   }

lookup_dict_arab = {'ا': 0, 'أ': 0, 'إ': 0, 'آ': 0, 'ح': 0, 'خ': 0, 'ه': 0, 'ع': 0, 'غ': 0, 'ش': 0, 'و': 0, 'ي': 0,
                	'ف': 1, 'ب': 1,
                    'ج': 2, 'ز': 2, 'س': 2, 'ص': 2, 'ظ': 2, 'ق': 2, 'ك': 2,
                	'ت': 3, 'ث': 3, 'د': 3, 'ذ': 3, 'ض': 3, 'ط': 3,
                	'ل': 4, 
                	'م': 5, 'ن': 5,
                	'ر': 6
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
		keys_unicode = [Astr(x) for x in dict_chars.keys()]
		pos_vec = [1 if char in x else 0 for x in keys_unicode]
		return dict_chars.keys()[pos_vec.index(1)] if sum(pos_vec)>0 else None


	code, prevcode = None, None
	if len(arab_str)>1:
		for char in arab_str[1:]:

			key = charInDictKeys(char, lookup_dict_arab)

			if key and lookup_dict_arab[key]!='0': code = lookup_dict_arab[key]
			else: code = char

			if code != prevcode:
				transp += str(code)
				prevcode = code

	return transp


if __name__ == '__main__':
	print arabic_soundex_main('ciao')
