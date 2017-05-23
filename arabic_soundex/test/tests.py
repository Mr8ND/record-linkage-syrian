# -*- coding: utf-8 -*-

import unittest2 as unittest
import sys
sys.path.append("..")

from arabic_soundex import arabic_soundex_main

class MyTest(unittest.TestCase):

	#Test0 makes sure that the function throws the correct expection when an empty string is given
	def test0(self):
		self.assertRaises(TypeError, arabic_soundex_main, '')


	#This first test will test non-arabic characters string
	def test1(self):
		self.assertEqual(arabic_soundex_main('ciao'), 'xiao')
		self.assertEqual(arabic_soundex_main('ciao!!!'), 'xiao!')
		self.assertEqual(arabic_soundex_main('_~|'), 'x~|')


	#Second test will work on non-arabic characters string with the the two toggles
	#in all the possible combinations
	def test2(self):
		self.assertEqual(arabic_soundex_main('ciao', firstcharuniforming=False), 'ciao')

	def test3(self):
		self.assertEqual(arabic_soundex_main('ابب'), 'x1')

#	def test4(self):
#		self.assertEqual(arabic_soundex_main('\u0627\u0641\u0628'), 'x1')

#	def test5(self):
#		self.assertEqual(arabic_soundex_main('\u0627\u0641\u0628'), 'x1')

#	def test6(self):
#		self.assertEqual(arabic_soundex_main('\u0627\u0641\u0628'), 'x1')

#	def test7(self):
#		self.assertEqual(arabic_soundex_main('\u0627\u0641\u0628'), 'x1')

#	def test8(self):
#		self.assertEqual(arabic_soundex_main('\u0627\u0641\u0628'), 'x1')

#	def test9(self):
#		self.assertEqual(arabic_soundex_main('\u0627\u0641\u0628'), 'x1')

#	def test10(self):
#		self.assertEqual(arabic_soundex_main('\u0627\u0641\u0628'), 'x1')

#	def test11(self):
#		self.assertEqual(arabic_soundex_main('\u0627\u0641\u0628'), 'x1')

#	def test12(self):
#		self.assertEqual(arabic_soundex_main('\u0627\u0641\u0628'), 'x1')

#	def test13(self):
#		self.assertEqual(arabic_soundex_main('\u0627\u0641\u0628'), 'x1')

#	def test14(self):
#		self.assertEqual(arabic_soundex_main('\u0627\u0641\u0628'), 'x1')

if __name__ == '__main__':
	unittest.main()