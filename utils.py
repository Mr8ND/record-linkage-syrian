from itertools import izip, islice, tee


def ngramFunction(string, n):
	'''
	This function implements a sliding window of n characters wide on a string.

	INPUT:
	- string: the string on which the sliding window is going to be applied
	- n: the width of the window in characters

	OUTPUT:
	A list of tuples, each of which contains a list of the characters in each sliding window ngram.
	'''
	return list(izip(*(islice(j, i, None) for i,j in enumerate(tee(string,n)))))


def emptyStringsError(s1, s2):
	'''
	This function throws an error when one of the two string is empty or None.

	INPUT:
	- s1: the first string
	- s2: the second string
	'''
	if (not s1) or (not s2):
		raise TypeError("One of the string is empty. They both need to be not empty.")
	else:
		pass


def sameLengthError(s1,s2):
	'''
	This function throws an error when the two strings are not of the same length.

	INPUT:
	- s1: the first string
	- s2: the second string
	'''
	if (not len(s1)==len(s2)):
		raise TypeError("The two strings need to have the same length")
	else:
		pass


def differenceLengthError(s1, s2, diff):
	'''
	This function throws an error when the difference in length of the two strings is not equal to diff.

	INPUT:
	- s1: the first string
	- s2: the second string
	- diff: the difference between the two strings
	'''
	if not (len(s1)==len(s2)+diff or len(s2)==len(s1)+diff):
		raise TypeError("The two strings need to have a difference of %s in length"%(str(diff)))
	else:
		pass


def identifyTypoFunction(s1, s2):
	'''
	This function identifies all the typos made when considering two strings. The definition of typo in this case is two character being different while being in the same position in a string. The function checks
	whether the two strings are not empty and have the same length and it throws a TypeError exception otherwise.

	INPUT:
	- s1: the first string
	- s2: the second string

	OUTPUT:	
	A list of tuples, each tuple has two elements, one being the character in the first string and the other the character in the second string which are identified as typo.
	'''
	
	emptyStringsError(s1, s2)
	sameLengthError(s1,s2)

	return [(x,s2[i]) for i,x in enumerate(s1) if x!=s2[i]]


def identifyWordAssociationFunction(s1,s2,equality=False):
	'''
	This function identifies all the full words which occupy the same position in the string and are not the same. 
	The function checks	whether the two strings are not empty and it throws a TypeError exception otherwise.

	INPUT:
	- s1: the first string
	- s2: the second string

	OUTPUT:	
	A list of tuples, each tuple has two elements, which are two words which are associated in the strings
	'''

	emptyStringsError(s1,s2)

	output_vec = []
	s1_part, s2_part = s1.split(' '), s2.split(' ')
	n1, n2 = len(s1_part), len(s2_part)
	minlen = min([n1,n2])

	for i in range(minlen):
		flag = s1_part[i]==s2_part[i] if equality else s1_part[i] != s2_part[i]
		if flag:
			output_vec.append(tuple([s1_part[i], s2_part[i]]))

	return output_vec



def identifyTranspositionFunction(s1, s2):
	'''
	This function identifies all the transpositions made when considering two strings. The definition of transpositions in this	case is two character being swapped between two strings - i.e. "hello" and "Helol". The function checks	whether the two strings are not empty and have the same length and it throws a TypeError exception otherwise.

	INPUT:
	- s1: the first string
	- s2: the second string

	OUTPUT:	
	A list of tuples, each tuple has two elements, one being the pair of characters in the first string and the other the character in the second string which are identified as a transposition.
	'''

	emptyStringsError(s1, s2)
	sameLengthError(s1,s2)

	output_vec = []
	for i in range(len(s1)-1):
		if s1[i:i+2][::-1] == s2[i:i+2] and s2[i:i+2][0] != s2[i:i+2][1]:
			output_vec.append(tuple([s1[i:i+2],s2[i:i+2]]))
	return output_vec


def identifyInsertionDeletionFunction(s1, s2, mod, wd = 1, epsilon_sym='$'):
	'''
	This function identifies either one deletion or insertion made when considering two strings. Importantly the function will work	only when only a single deletion or insertion have been operated. The function will throw a TypeError exception if one of the two strings is empty or whether their difference in length is not 1. It will also throw an expection if the parameter "mod" is null or different from 'insertion' or 'deletion'.

	INPUT:
	- s1: the first string
	- s2: the second string
	- mod: parameter indication whether insertion or deletion
	- wd: optional, the width of the window in which the output is provided. A wd=1 will return windows with the insertion/deletion	character with 1 character to the left and one to the right.
	- epsilon_sym: optional, it's the symbol used to indicate the character which has been inserted/deleted

	OUTPUT:	
	A list of a single tuple in which the first element is the insertion/deletion character plus wd character to its left and to its right in the longer string, while the same is done using the epsilon_sym in the smaller string. I.e. "hello" and "hllo" as input will result in an output of [('hel','h$l')].
	'''

	emptyStringsError(s1, s2)
	differenceLengthError(s1, s2, 1)

	if (not mod) or (mod not in ['insertion', 'deletion']):
		raise TypeError("You need to include a mod which is either 'insertion' or 'deletion'")

	n1 = len(s1)
	n2 = len(s2)
	if mod == 'insertion' and not(n1>n2):
		s1, n1, s2, n2 = s2, n2, s1, n1

	output = []
	if s1[0] != s2[0]:
		output.append(tuple([s1[0:wd+2], epsilon_sym+ s2[0:wd+1]]))
	elif s1[n1-1] != s2[n2-1]:
		if n1<2+wd and n2<1+wd:
			output.append(tuple([s1, s2+epsilon_sym]))
		else:
			output.append(tuple([s1[n1-wd-2:n1], s2[n2-wd-1:n2]+epsilon_sym]))
	else:
		for j in range(1, n1-1):
			if s1[j] != s2[j] and not output:
				output.append(tuple([s1[j-wd:j+wd+1], s2[j-wd] + epsilon_sym + s2[j:j+wd]]))
	
	return output


if __name__ == '__main__':
	print identifyWordAssociationFunction('ciao bello', 'ciao bello', equality=True)