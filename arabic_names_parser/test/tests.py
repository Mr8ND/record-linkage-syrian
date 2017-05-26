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
			  ('بن عبد الجبار', 'بن عبد الجبار'),
			  ('محمد بنت جبار', 'بنت جبار')]

kunya_list = [('محمد أبو جبار', 'أبو جبار'),
			  ('محمد أبو أبو أبو أبو جبار', 'أبو أبو أبو أبو جبار'),
			  ('محمد بن لادن أبو جبار', 'أبو جبار'),
			  ('محمد أبو جبار بن لادن', 'أبو جبار'),
			  ('أبو جبار', 'أبو جبار'),
			  ('أبو جبار أبو تشوبار', 'أبو جبار أبو تشوبار'),
			  ('أبو جبار أبو تشوبار أبو برابدو أبو لوي', 'أبو جبار أبو تشوبار أبو برابدو أبو لوي'),
			  ('نيكوديمو بن فاليريو أبو نون آل إيطاليا', 'أبو نون'),
			  ('نيكوديمو بن فاليريو', ''),
			  ('محمد أم جبار', 'أم جبار'),
			  ('محمد أوم جبار', 'أوم جبار')]

laqab_list  = [('نيكوديمو بن فاليريو',''),
			   ('محمد الفاييت بن لادن', 'الفاييت'),
			   ('محمد الفاييت ابو لادن', 'الفاييت'),
			   ('محمد الفاييت بن جيوفاني أبو لادن','الفاييت'),
			   ('محمد الفاييت بن جيوفاني أبو لادن الأفغاني محامدي', 'الفاييت'),
			   ('محمد الفاييت العدواني', 'العدواني')]

nisbah_list = [('محمد الفاييت ابو لادن', ''),
			   ('محمد', ''),
			   ('محمد بن لادن الفياطي', 'الفياطي')]


laqab_nisbah_list = [('محمد جبار بن لادن', ''), #Mohammed jabbar ben laden, laqab/nisbah should be empty here.
					 ('محمد جبار لادن', 'جبار لادن'), #Mohammed jabbar laden, laqab/nisbah should be capturing aything after the ism up to two words
					 ('محمد جبار', 'جبار'), #Mohammed jabbar, Jabbar should be considered as laqab/nisbah
					 ('محمد جبار أفغاني كازاكي كاكوتاني', 'جبار أفغاني')] #Mohammed jabbar afghani kazaki kakutani, Jabbar Afghani should be considered as laqab/nisbah.

other_list = [('محمد جبار بن لادن', ''), #Mohammed jabbar ben laden, other should be empty here.
			  ('محمد جبار بن لادن أفغاني كازاكي كاكوتاني', 'كازاكي كاكوتاني'), #Mohammed jabbar ben laden afghani kazaki kakutani. In this case the kazaki kakutani should be in other 
			  ('محمد جبار أفغاني كازاكي كاكوتاني', 'كازاكي كاكوتاني')] #Mohammed jabbar afghani kazaki kakutani, in this case again kazaki kakutani should be in other

full_test_list = [('محمد جبار بن لادن أبو أحمد الأفغاني', [('ISM', u'\u0645\u062d\u0645\u062f'), 
														   ('LAQAB', u'\u062c\u0628\u0627\u0631'), 
														   ('NASAB', u'\u0628\u0646 \u0644\u0627\u062f\u0646'),
														   ('KUNYA', u'\u0623\u0628\u0648 \u0623\u062d\u0645\u062f'),
														   ('NISBAH', u'\u0627\u0644\u0623\u0641\u063a\u0627\u0646\u064a'),
														   ('LAQAB/NISBAH', ''), 
														   ('OTHER', '')] )
				]


test_dict = {'ISM': ism_list, 
			 'LAQAB': laqab_list, 
			 'NASAB': nasab_list,
			 'KUNYA': kunya_list,
			 'NISBAH': nisbah_list, 
			 'LAQAB/NISBAH':laqab_nisbah_list,
			 'OTHER':other_list,
			 'FULL_TEST': full_test_list}