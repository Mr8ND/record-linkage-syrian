from collections import Counter
from arabic_soundex.arabic_soundex import arabicSoundexNames
import icu
from functools import partial


def CompContainedFunction(s1,s2):
	'''
	This function returns 1 if one of the two strings in input is completely contained into the other.
	It will return 1 if the two strings are exactly the same.

	INPUT:
	- s1, s2: two strings, not necessarily Arabic or Unicode

	OUTPUT:
	1 if s1 is completely contained in s2 or viceversa (s2 contained in s1), 0 if not.
	'''
	output = 0
	s1_part, s2_part = s1.split(' '), s2.split(' ')
	n1, n2 = len(s1_part), len(s2_part)
	if n1 >= n2:
		output= int(all(x in s1_part for x in s2_part))
	elif n2 > n1:
		output = int(all(x in s2_part for x in s1_part))
	return output


def exactMatchFunction(s1,s2):
	'''
	This function returns 1 if two strings are exactly the same, 0 if not.

	INPUT:
	- s1, s2: two strings, not necessarily Arabic or Unicode.

	OUTPUT:
	1 if s1 is exactly equal to s2, 0 if not.
	'''
	return int(s1==s2)


def soundexMatchFunction(s1,s2):
	'''
	This function returns 1 if the two strings have the same Soundex representation, 0 if not.

	INPUT:
	- s1, s2: two strings, have to be in Arabic unicode characters.

	OUTPUT:
	1 if their Soundex representation is exactly the same, 0 if not.
	'''
	return int(arabicSoundexNames(s1)==arabicSoundexNames(s2))


def noSpaceMatchFunction(s1,s2):
	'''
	This function returns 1 if the two strings are the same when removing spaces, 0 if not.

	INPUT:
	- s1, s2: two strings,  not necessarily Arabic or Unicode.

	OUTPUT:
	1 if the two strings are exactly the same when removing spaces, 0 if not.
	'''
	return int(s1.replace(' ','')==s2.replace(' ',''))


def ShuffleMatchFunction(s1,s2):
	'''
	This function returns 1 if the two strings are composed of exactly the same words in the same amount, just shuffled around, 0 if not.
	It will return 1 if the two strings are exactly the same.

	INPUT:
	- s1, s2: two strings, not necessarily Arabic or Unicode. The two strings are ideally composed by multiple words. If strings are composed by a single word, this function will return 1 if the two strings are the same simply.

	OUTPUT:
	1 if the two strings are composed by exactly the same words, just shuffled arounds, 0 if not.
	'''
	return int(Counter(s1.split(' ')) == Counter(s2.split(' ')))


def firstCharFunction(s1,s2,n):
	'''
	This function returns whether the two strings have the same first n characters or not.

	INPUT:
	- s1: first string
	- s2: second string
	- n: number of characters checked

	OUTPUT:
	True/False (Logical)
	'''
	return int(s1[:n]==s2[:n])


def lastCharFunction(s1,s2,n):
	'''
	This function returns whether the two strings have the same last n characters or not.

	INPUT:
	- s1: first string
	- s2: second string
	- n: number of characters checked

	OUTPUT:
	True/False (Logical)
	'''
	return int(s1[::-1][:n]==s2[::-1][:n])


def sameWordFunction(s1,s2,idx=0):
	'''
	This function returns whether the two strings have the same n-th word.

	INPUT:
	- s1: first string
	- s2: second string
	- idx: index of the word that needs to be checked

	OUTPUT:
	True/False (Logical)
	'''
	try:
		return int(s1.split(' ')[idx]==s2.split(' ')[idx])
	except IndexError:
		return 0


def sameFirstWordsFunction(s1,s2,n=2):
	'''
	This function returns whether the two strings have the same first n words or not.

	INPUT:
	- s1: first string
	- s2: second string
	- n: number of words checked

	OUTPUT:
	True/False (Logical)
	'''
	try:
		return int(s1.split(' ')[:2]==s2.split(' ')[:2])
	except IndexError:
		return 0


def sameNWordsFunction(s1,s2,n=3):
	'''
	This function returns whether the two strings have at least n words in common or not.

	INPUT:
	- s1: first string
	- s2: second string
	- n: number of words in common to make the output true

	OUTPUT:
	True/False (Logical)
	'''
	s1_w, s2_w = s1.split(' '), s2.split(' ')
	s_short, s_long = obtainLongerShorterFunction(s1_w, s2_w)
	counter =0
	for ss in s_short:
		counter += int(ss in s_long)
	return int(counter>=n)
	
	
def charThresholdFunction(s1,s2,threshold=0.5):
	'''
	This function returns whether the two strings have at least a percentage of characters aligned.

	INPUT:
	- s1: first string
	- s2: second string
	- threshold: percentage of characters aligned such that the output is True (not included)

	OUTPUT:
	True/False (Logical)
	'''
	min_l = min([len(s1), len(s2)])
	eq_vec = [int(s1[j]==s2[j]) for j in range(min_l)]
	return int((sum(eq_vec)/float(min_l))>threshold)


def wordThresholdFunction(s1,s2,threshold=0.5):
	'''
	This function returns whether the two strings have at least a percentage of words aligned - i.e. same words in the same position.

	INPUT:
	- s1: first string
	- s2: second string
	- threshold: percentage of words aligned such that the output is True (not included)

	OUTPUT:
	True/False (Logical)
	'''
	s1_w, s2_w = s1.split(' '), s2.split(' ')
	min_l = min([len(s1_w), len(s2_w)])
	eq_vec = [int(s1_w[j]==s2_w[j]) for j in range(min_l)]
	return int((sum(eq_vec)/float(min_l))>threshold)


def sortedArabicFunction(s1, s2, collator=icu.Collator.createInstance(icu.Locale('de_DE.UTF-8'))):
	'''
	This function returns whether the two strings are the same if the Unicode characters are sorted.

	INPUT:
	- s1: first string
	- s2: second string

	OUTPUT:
	True/False (Logical)
	'''
	s1_s = ''.join(sorted(list(s1), key=collator.getSortKey))
	s2_s = ''.join(sorted(list(s2), key=collator.getSortKey))
	return int(s1_s==s2_s)


def obtainLongerShorterFunction(s1,s2):
	'''
	This function returns which of the two strings in input is shorter first and the longer one as second output. If they have the same length, the first string is returned first.

	INPUT:
	- s1: first string
	- s2: second string

	OUTPUT:
	- s_short: shorter string (first)
	- s_long: longer string (second)
	'''
	if len(s1) >= len(s2):
		s_short, s_long = s2, s1
	else:
		s_short, s_long = s1, s2
	return s_short, s_long

	
def samePrefixWordsFunction(s1, s2, n=3):
	'''
	This function returns whether in the first n characters of each word in the shorter string are present in one of the words of the longer strings. Removing some edge cases which are not considered problematic, the function checks whether the prefixes of the words of the two strings are the same. n stands for the number of characters of each prefix (custom).

	INPUT:
	- s1: first string
	- s2: second string
	- n: number of characters of each prefix

	OUTPUT:
	True/False (Logical)
	'''
	s1_w, s2_w = s1.split(' '), s2.split(' ')
	s_short, s_long = obtainLongerShorterFunction(s1_w, s2_w)
	
	same_suff = []
	for ss in s_short:
		same_suff.append(sum([int(ss[:n]==sl[:n]) for sl in s_long])>=1)
	return all(same_suff)


def sameSuffixWordsFunction(s1, s2, n=3):
	'''
	This function returns whether in the last n characters of each word in the shorter string are present in one of the words of the longer strings. Removing some edge cases which are not considered problematic, the function checks whether the suffixes of the words of the two strings are the same. n stands for the number of characters of each prefix (custom).

	INPUT:
	- s1: first string
	- s2: second string
	- n: number of characters of each suffix

	OUTPUT:
	True/False (Logical)
	'''
	s1_w, s2_w = s1.split(' '), s2.split(' ')
	s_short, s_long = obtainLongerShorterFunction(s1_w, s2_w)
	
	same_suff = []
	for ss in s_short:
		same_suff.append(sum([int(ss[::-1][:n]==sl[::-1][:n]) for sl in s_long])>=1)
	return all(same_suff)


feature_dict = {

	'deterministic_features':{
		'comp_contained_match': CompContainedFunction,
		'exact_match': exactMatchFunction,
		'soundex_match': soundexMatchFunction,
		'nospace_match': noSpaceMatchFunction,
		'shuffle_match': ShuffleMatchFunction
	},

	'general_binary_features':{
		'first_5_char': partial(firstCharFunction, n=5),
		'first_10_char': partial(firstCharFunction, n=10),
		'first_15_char': partial(firstCharFunction, n=15),
		'last_5_char': partial(lastCharFunction, n=5),
		'last_10_char': partial(lastCharFunction, n=10),
		'last_15_char': partial(lastCharFunction, n=15),
		'same_first_word': partial(sameWordFunction, idx=0),
		'same_second_word': partial(sameWordFunction, idx=1),
		'same_third_word': partial(sameWordFunction, idx=2),
		'same_first2_words': sameFirstWordsFunction,
		'3_common_words': sameNWordsFunction,
		'align_char_morethanhalf': charThresholdFunction,
		'align_words_morethanhalf': wordThresholdFunction,
		'same_sorted_string': sortedArabicFunction,
		'same_prefixes': samePrefixWordsFunction,
		'same_suffixes': sameSuffixWordsFunction
	}
}


