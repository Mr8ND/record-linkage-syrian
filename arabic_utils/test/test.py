# -*- coding: utf-8 -*-
import unittest2 as unittest
import sys
sys.path.append("..")
sys.path.append("../..")

from general_utils_arabic import convertReprFunct, stripAccents


class MyTest(unittest.TestCase):

	def testStripFunction(self):
		#Tests taken from the examples at https://learnquranicarabic.wordpress.com/2010/07/26/three-types-of-tanwin/

		self.assertEqual(stripAccents(u'محمدٌ', tanween_flag=True), u'محمدٌ')
		self.assertEqual(stripAccents(u'محمدٍ', tanween_flag=True), u'محمدٍ')
		self.assertEqual(stripAccents(u'محمداً', tanween_flag=True), u'محمداً')

		self.assertEqual(stripAccents(u'محمدٌ'), u'محمد')
		self.assertEqual(stripAccents(u'محمدٍ'), u'محمد')
		self.assertEqual(stripAccents(u'محمداً'), u'محمدا')

	def testConvertFunction(self):

		self.assertEqual(convertReprFunct(u'ﺹﺺﺻﺼ'), u'صصصص')
		self.assertEqual(convertReprFunct(u'ﺀﺁﺂﺃ'), u'اااا')
		self.assertEqual(convertReprFunct(u'اﺙﺚﺛﺜا'), u'اثثثثا')

if __name__ == '__main__':
	unittest.main()