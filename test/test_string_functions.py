# -*- coding: utf-8 -*-
import unittest2 as unittest
import sys
sys.path.append("..")

from utils import emptyStringsError, sameLengthError, differenceLengthError
from utils import identifyTypoFunction, identifyTranspositionFunction, identifyInsertionDeletionFunction, identifyWordAssociationFunction

class MyTest(unittest.TestCase):


	def test_emptystringerror1_function(self):
		self.assertRaises(TypeError, emptyStringsError, ('',''))
	def test_emptystringerror2_function(self):
		self.assertRaises(TypeError, emptyStringsError, ('abcd',''))
	def test_emptystringerror3_function(self):
		self.assertRaises(TypeError, emptyStringsError, ('','abcd'))
	def test_emptystringerror4_function(self):
		self.assertEqual(emptyStringsError('ciao','ciao'), None)


	def test_samelengtherror1_function(self):
		self.assertRaises(TypeError, sameLengthError, ('abc','abcd'))
	def test_samelengtherror2_function(self):
		self.assertRaises(TypeError, sameLengthError, ('abcde','abcd'))


	def test_differencelengtherror1_function(self):
		self.assertRaises(TypeError, differenceLengthError, ('abcd','abcd', 1))
	def test_differencelengtherror2_function(self):
		self.assertRaises(TypeError, differenceLengthError, ('abcde','abcde', 1))
	def test_differencelengtherror3_function(self):
		self.assertEqual(differenceLengthError('abcde','abcd', 1), None)
	def test_differencelengtherror4_function(self):
		self.assertEqual(differenceLengthError('abc','abcd', 1), None)


	def test_typo1_function(self):
		self.assertEqual(identifyTypoFunction('ciao','ciao'), [])
	def test_typo2_function(self):
		self.assertEqual(identifyTypoFunction('ciao','ciau'), [('o','u')])
	def test_typo3_function(self):
		self.assertEqual(identifyTypoFunction('ciaooo','ciauuu'), [('o','u'), ('o','u'), ('o','u')])
	def test_typo4_function(self):
		self.assertEqual(identifyTypoFunction('ceao','ciau'), [('e','i'), ('o','u')])
	def test_typo5_function(self):
		self.assertEqual(identifyTypoFunction('maybe','meyba'), [('a','e'), ('e','a')])


	def test_transposition1_function(self):
		self.assertEqual(identifyTranspositionFunction('ciao','ciao'), [])
	def test_transposition2_function(self):
		self.assertEqual(identifyTranspositionFunction('ciao','caio'), [('ia','ai')])
	def test_transposition3_function(self):
		self.assertEqual(identifyTranspositionFunction('maybetomorrow','mayebtomorrwo'), [('be','eb'), ('ow','wo')])
	def test_transposition4_function(self):
		self.assertEqual(identifyTranspositionFunction('i do not think so','i od nto thikn so'), [('do','od'), ('ot','to'), ('nk','kn')])


	def test_insertiondeletion1_function(self):
		self.assertRaises(TypeError, identifyInsertionDeletionFunction, ('abcd','abcd','insertion'))
	def test_insertiondeletion2_function(self):
		self.assertRaises(TypeError, identifyInsertionDeletionFunction, ('abcd','abcd',None))
	def test_insertiondeletion3_function(self):
		self.assertRaises(TypeError, identifyInsertionDeletionFunction, ('abcd','abcd','transposition'))
	def test_insertiondeletion4_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('ciao','iao','deletion'), [('cia','$ia')])
	def test_insertiondeletion5_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('cia','ia','deletion'), [('cia','$ia')])
	def test_insertiondeletion6_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('ci','i','deletion'), [('ci','$i')])
	def test_insertiondeletion7_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('iao','ciao','insertion'), [('cia','$ia')])
	def test_insertiondeletion8_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('ia','cia','insertion'), [('cia','$ia')])
	def test_insertiondeletion9_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('i','ci','insertion'), [('ci','$i')])
	def test_insertiondeletion10_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('maybe one day','aybe one day','deletion'), [('may','$ay')])
	def test_insertiondeletion11_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('aybe one day','maybe one day','insertion'), [('may','$ay')])
	def test_insertiondeletion12_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('maybe one day','maybe one da','deletion'), [('day','da$')])
	def test_insertiondeletion13_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('maybe one da','maybe one day','insertion'), [('day','da$')])
	def test_insertiondeletion14_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('day','da','deletion'), [('day','da$')])
	def test_insertiondeletion15_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('da','d','deletion'), [('da','d$')])
	def test_insertiondeletion16_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('da','day','insertion'), [('day','da$')])
	def test_insertiondeletion17_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('d','da','insertion'), [('da','d$')])
	def test_insertiondeletion18_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('maybe','mabe','deletion'), [('ayb','a$b')])
	def test_insertiondeletion19_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('mabe','maybe','insertion'), [('ayb','a$b')])
	def test_insertiondeletion20_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('tomorrow','tomorow','deletion'), [('rro','r$o')])
	def test_insertiondeletion21_function(self):
		self.assertEqual(identifyInsertionDeletionFunction('tomorow','tomorrow','insertion'), [('rro','r$o')])


	def test_association1_function(self):
		self.assertRaises(TypeError, identifyWordAssociationFunction, ('abcd',''))
	def test_association2_function(self):
		self.assertRaises(TypeError, identifyWordAssociationFunction, ('abcd',''))
	def test_association3_function(self):
		self.assertRaises(TypeError, identifyWordAssociationFunction, ('',''))
	def test_association4_function(self):
		self.assertEqual(identifyWordAssociationFunction('ciao','ciao', equality=True), [('ciao','ciao')])
	def test_association5_function(self):
		self.assertEqual(identifyWordAssociationFunction('maybe tomorrow','but not today', equality=True), [])
	def test_association6_function(self):
		self.assertEqual(identifyWordAssociationFunction('maybe today','maybe', equality=True), [('maybe','maybe')])
	def test_association7_function(self):
		self.assertEqual(identifyWordAssociationFunction('maybe today','maybe today', equality=True), [('maybe','maybe'), ('today','today')])
	def test_association8_function(self):
		self.assertEqual(identifyWordAssociationFunction('maybe today or not','maybe today', equality=True), [('maybe','maybe'), ('today','today')])
	def test_association9_function(self):
		self.assertEqual(identifyWordAssociationFunction('ciao','caro', equality=False), [('ciao','caro')])
	def test_association10_function(self):
		self.assertEqual(identifyWordAssociationFunction('maybe tomorrow','but not today', equality=False), [('maybe','but'),('tomorrow','not')])
	def test_association11_function(self):
		self.assertEqual(identifyWordAssociationFunction('maybe today','maybe', equality=False), [])
	def test_association12_function(self):
		self.assertEqual(identifyWordAssociationFunction('definitely tomorrow','maybe today', equality=False), [('definitely','maybe'), ('tomorrow','today')])
	def test_association13_function(self):
		self.assertEqual(identifyWordAssociationFunction('maybe tomorrow or not','maybe today', equality=False), [('tomorrow','today')])
		

if __name__ == '__main__':
	unittest.main()