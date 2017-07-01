# -*- coding: utf-8 -*-
import sys
sys.path.append("..")

from arabic_names_parser.parser_utils import Astr
import unicodedata
import nltk.stem.isri as stemmer


def removeAlChars(string):
	'''
	This function removes the "AL" Arabic characters from an unicode strings.

	INPUT:
	- string: Unicode string, ideally in Arabic

	OUTPUT:
	The same string with the "AL" characters removed.
	'''
	al_list = [u'آل', u'ال', u'من']
	return string.replace(al_list[0], '').replace(al_list[1], '').replace(al_list[2], '')

tanween_chars = (Astr(u'ً'), Astr(u'ٌ'), Astr(u'ٍ'))


def stripAccents(s, tanween_flag=False):
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
		tanween_vec = [1 if c in tanween_chars else 0 for c in s]
		return ''.join(unicodedata.normalize('NFD', c) if (unicodedata.category(c) != 'Mn' and tanween_vec[i]==0) else c for i,c in enumerate(s))
	else:
		return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def removeSuffixesFunction(word):
	'''
	This function removes the suffixes due to plural, gender and personal pronouns in Arabic using the nltk stemmer in a single word.

	INPUT:
	word: expected to be an Arabic unicode string

	OUTPUT:
	same word without suffixes due to cases above.
	'''

	word_mod = stemmer.ISRIStemmer.suf1(stemmer.ISRIStemmer(), word)
	return stemmer.ISRIStemmer.suf32(stemmer.ISRIStemmer(), word_mod)


def removePrefixesFunction(word):
	'''
	This function removes the prefixes due to plural, gender and personal pronouns in Arabic using the nltk stemmer in a single word.

	INPUT:
	word: expected to be an Arabic unicode string

	OUTPUT:
	same word without prefixes due to cases above.
	'''

	word_mod = stemmer.ISRIStemmer.pre1(stemmer.ISRIStemmer(), word)
	return stemmer.ISRIStemmer.pre32(stemmer.ISRIStemmer(), word_mod)


def stemArabicWordFunction(word):
	'''
	This function removes the suffixes due to the case of the word. In other words, it gives back the root form of the word regardless of its logical meaning in a sentence. It is useful as names are usually diptotes - i.e. they might have multiple cases.

	INPUT:
	word: expected to be an Arabic unicode string

	OUTPUT:
	same word without suffixes due to word cases.
	'''
	
	return stemmer.ISRIStemmer.stem(stemmer.ISRIStemmer(), word)


def fullPrefSufRemFunction(string, quick=True):
	'''
	This function takes in input a string, which can be composed of multiple words, and removes all possible suffixes and prefixes due to plural, gender, personal pronouns and cases in the sentence, word by word.

	INPUT:
	- string: expected to be an Arabic unicode string, can be composed of multiple words
	- quick: logical flag, if True, makes the function a one-liner 

	OUTPUT:
	same string with prefixes and suffixes removed as indicated above.
	'''
	if not quick:
		string_vec = [removePrefixesFunction(removeSuffixesFunction(w)) for w in string.split(' ')]
		string_vec_stemmed = [stemArabicWordFunction(w) for w in string_vec]
		return ' '.join(string_vec_stemmed)
	else:
		return ' '.join([stemArabicWordFunction(removePrefixesFunction(removeSuffixesFunction(w))) for w in string.split(' ')])
