# -*- coding: utf-8 -*-
import unittest2 as unittest
import sys
sys.path.append("..")

from arabic_parser import arabicNameParser
from tests import test_dict

class MyTest(unittest.TestCase):

    def test_AP_ISM(self):
    	result_first_test = [('ISM', u'\u0645\u062d\u0645\u062f'), ('LAQAB', u'\u062c\u0628\u0627\u0631 '), ('NASAB', u'\u0628\u0646 \u0644\u0627\u062f\u0646'), ('KUNYA', u'\u0623\u0628\u0648 \u0623\u062d\u0645\u062f'), ('NISBAH', u'\u062c\u0628\u0627\u0631'), ('LAQAB/NISBAH', ''), ('OTHER', u'\u0628\u0627\u0631 \u0627\u0644\u0623\u0641\u063a\u0627\u0646\u064a')]
    	self.assertEqual(arabicNameParser('محمد جبار بن لادن أبو أحمد الأفغاني'), result_first_test)

if __name__ == '__main__':
	unittest.main()