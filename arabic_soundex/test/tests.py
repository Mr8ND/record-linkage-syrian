# -*- coding: utf-8 -*-

import unittest2 as unittest
import sys
sys.path.append("..")

from arabic_soundex import arabicSoundexNames, arabicSoundexMain


class MyTest(unittest.TestCase):
	'''
	All the tests below are written for both the main function (arabicSoundexMain) and the wrapper for
	multi-words strings (arabicSoundexNames)
	'''

	# Test0 makes sure that the function throws the correct expection when an empty string is given
	def test0(self):
		self.assertRaises(TypeError, arabicSoundexMain, '')

	def test0_w(self):
		self.assertRaises(TypeError, arabicSoundexNames, '')


	# This first test will test non-arabic characters string
	def test1(self):
		self.assertEqual(arabicSoundexMain('ciao'), u'xiao')
		self.assertEqual(arabicSoundexMain('ciao!!!'), u'xiao')
		self.assertEqual(arabicSoundexMain('ciao!!! maybe'), u'xiao')
		self.assertEqual(arabicSoundexMain('_~|'), u'x~|0')

	def test1_w(self):
		self.assertEqual(arabicSoundexNames('ciao'), u'xiao')
		self.assertEqual(arabicSoundexNames('ciao!!!'), u'xiao')
		self.assertEqual(arabicSoundexNames('ciao!!! maybe'), u'xiao xayb')
		self.assertEqual(arabicSoundexNames('_~|'), u'x~|0')


	# Second test will work on non-arabic characters string with the toggles.
	# اابب are just random characters here, they are not a name.
	def test2(self):
		self.assertEqual(arabicSoundexMain('ciao', firstcharuniforming=False), u'ciao')
		self.assertEqual(arabicSoundexMain('ciao', firstcharuniforming=True), u'xiao')
		self.assertEqual(arabicSoundexMain('ciao', lim=1), u'xi')
		self.assertEqual(arabicSoundexMain('ciao', lim=2), u'xia')
		self.assertEqual(arabicSoundexMain('ciao', lim=3), u'xiao')
		self.assertEqual(arabicSoundexMain('ciao', lim=4), u'xiao0')
		self.assertEqual(arabicSoundexMain('ciao', lim=6), u'xiao000')
		self.assertEqual(arabicSoundexMain(u'اابب', firstletter_rem=True), u'x100')
		self.assertEqual(arabicSoundexMain(u'اابب', firstletter_rem=True, lim=2), u'x10')
		self.assertEqual(arabicSoundexMain(u'اابب', firstletter_rem=False), u'x010')
		self.assertEqual(arabicSoundexMain(u'اابب', firstletter_rem=False, lim=2), u'x01')

	def test2_w(self):
		self.assertEqual(arabicSoundexNames('ciao', firstcharuniforming=False), u'ciao')
		self.assertEqual(arabicSoundexNames('ciao', firstcharuniforming=True), u'xiao')
		self.assertEqual(arabicSoundexNames('ciao', lim=1), u'xi')
		self.assertEqual(arabicSoundexNames('ciao', lim=2), u'xia')
		self.assertEqual(arabicSoundexNames('ciao', lim=3), u'xiao')
		self.assertEqual(arabicSoundexNames('ciao', lim=4), u'xiao0')
		self.assertEqual(arabicSoundexNames('ciao', lim=6), u'xiao000')
		self.assertEqual(arabicSoundexNames(u'اابب', firstletter_rem=True), u'x100')
		self.assertEqual(arabicSoundexNames(u'اابب', firstletter_rem=True, lim=2), u'x10')
		self.assertEqual(arabicSoundexNames(u'اابب', firstletter_rem=False), u'x010')
		self.assertEqual(arabicSoundexNames(u'اابب', firstletter_rem=False, lim=2), u'x01')


	# Third test will work on some easy full names of which we know the soundex of.
	# محمد translated as Mohammed, محمد بن لادن أفغاني كاكوتاني as Mohammed ben Laden Afghani
	# Kakutani.
	def test3(self):
		self.assertEqual(arabicSoundexMain(unicode('ابب', 'utf-8')), u'x100')
		self.assertEqual(arabicSoundexMain(unicode('ابب ابب', 'utf-8')), u'x1 0')
		self.assertEqual(arabicSoundexMain(unicode('محمد', 'utf-8')), u'x053')
		self.assertEqual(arabicSoundexMain(unicode('محمد محمد', 'utf-8'), lim=8), u'x053 5053')
		self.assertEqual(arabicSoundexMain(unicode('محمد بن لادن أفغاني كاكوتاني', 'utf-8')), u'x053')
		self.assertEqual(arabicSoundexMain(unicode('محمد بن لادن أفغاني كاكوتاني', 'utf-8'), lim=20), u'x053 15 4035 01050 20')
		self.assertEqual(arabicSoundexMain(unicode('محمد بن لادن أفغاني كاكوتاني', 'utf-8'), lim=30), u'x053 15 4035 01050 202030500000')

	def test3_w(self):
		self.assertEqual(arabicSoundexNames(unicode('ابب', 'utf-8')), u'x100')
		self.assertEqual(arabicSoundexNames(unicode('ابب ابب', 'utf-8')), u'x100 x100')
		self.assertEqual(arabicSoundexNames(unicode('محمد', 'utf-8')), u'x053')
		self.assertEqual(arabicSoundexNames(unicode('محمد محمد', 'utf-8')), u'x053 x053')
		self.assertEqual(arabicSoundexNames(unicode('محمد بن لادن أفغاني كاكوتاني', 'utf-8')), u'x053 x500 x035 x050 x020')
		self.assertEqual(arabicSoundexNames(unicode('بن لادن محمد أفغاني كاكوتاني', 'utf-8')), u'x500 x035 x053 x050 x020')
		self.assertEqual(arabicSoundexNames(unicode('أفغاني كاكوتاني محمد بن لادن', 'utf-8')), u'x050 x020 x053 x500 x035')
		self.assertEqual(arabicSoundexNames(unicode('بن أفغاني كاكوتاني', 'utf-8')), u'x500 x050 x020')


if __name__ == '__main__':
	unittest.main()