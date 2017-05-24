# -*- coding: utf-8 -*-
import unittest2 as unittest
import sys
sys.path.append("..")

from arabic_parser import arabicNameParser
from tests import test_dict
from parser_utils import Astr

namepart_vec = ['ISM', 'LAQAB', 'NASAB', 'KUNYA', 'NISBAH', 'LAQAB/NISBAH', 'OTHER']

class MyTest(unittest.TestCase):

    def test_full(self):
    	result_first_test = [('ISM', u'\u0645\u062d\u0645\u062f'), ('LAQAB', u'\u062c\u0628\u0627\u0631'), ('NASAB', u'\u0628\u0646 \u0644\u0627\u062f\u0646'), ('KUNYA', u'\u0623\u0628\u0648 \u0623\u062d\u0645\u062f'), ('NISBAH', u'\u0627\u0644\u0623\u0641\u063a\u0627\u0646\u064a'), ('LAQAB/NISBAH', ''), ('OTHER', '')]
    	self.assertEqual(arabicNameParser('محمد جبار بن لادن أبو أحمد الأفغاني'), result_first_test)


    def test_posname_ism(self, namepart='ISM'):
    	index_np_ism = namepart_vec.index(namepart)

    	for i, k in enumerate(test_dict[namepart]):
    		print 'Testing the %s entry of the %s test list' %(str(i+1), namepart)
    		self.assertEqual(arabicNameParser(k[0])[index_np_ism][1], Astr(k[1]))


    def test_posname_nasab(self, namepart='NASAB'):
    	index_np_nasab = namepart_vec.index(namepart)

    	for i, k in enumerate(test_dict[namepart]):
    		print 'Testing the %s entry of the %s test list' %(str(i+1), namepart)
    		self.assertEqual(arabicNameParser(k[0])[index_np_nasab][1], Astr(k[1]))


    def test_posname_kunya(self, namepart='KUNYA'):
    	index_np_kunya = namepart_vec.index(namepart)

    	for i, k in enumerate(test_dict[namepart]):
    		print 'Testing the %s entry of the %s test list' %(str(i+1), namepart)
    		self.assertEqual(arabicNameParser(k[0])[index_np_kunya][1], Astr(k[1]))


    def test_posname_laqab(self, namepart='LAQAB'):
    	index_np_laqab = namepart_vec.index(namepart)

    	for i, k in enumerate(test_dict[namepart]):
    		print 'Testing the %s entry of the %s test list' %(str(i+1), namepart)
    		self.assertEqual(arabicNameParser(k[0])[index_np_laqab][1], Astr(k[1]))


    def test_posname_nisbah(self, namepart='NISBAH'):
    	index_np_nisbah = namepart_vec.index(namepart)

    	for i, k in enumerate(test_dict[namepart]):
    		print 'Testing the %s entry of the %s test list' %(str(i+1), namepart)
    		self.assertEqual(arabicNameParser(k[0])[index_np_nisbah][1], Astr(k[1]))



if __name__ == '__main__':
	unittest.main()