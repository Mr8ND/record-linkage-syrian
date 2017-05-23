# -*- coding: utf-8 -*-

ism_list = [('أبو الله', ''),
			('محمد أبو الله', 'محمد'),
			('ابو الله محمد', 'محمد'),
			('عبد الجبار', 'عبد الجبار'),
			('أبدول أبدول أبدول أبدول عبد جبار', 'أبدول أبدول أبدول أبدول عبد جبار'),
			('محمد بن لادن', 'محمد'),
			('أبدل آل كا', 'أبدل آل كا')]

nasab_list = [('بن لادن', 'بن لادن'),
			  ('بن بن لادن', 'بن بن لادن'),
			  ('بن بن بن لادن', 'بن بن بن لادن'),
			  ('بن بن بن بن بن بن بن بن لادن', 'بن بن بن بن بن بن بن بن لادن'),
			  ('بن عبد الجبار', 'بن عبد الجبار')]



test_dict = {'ISM': ism_list, 'LAQAB':[], 'NASAB': nasab_list, 'KUNYA':[], 'NISBAH':[], 'LAQAB/NISBAH':[], 'OTHER':[]}