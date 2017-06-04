# -*- coding: utf-8 -*-

ism_list = [('أبو الله', ''), #Abu Allah, the ism should be empty here as Abu is a Kunya
			('محمد أبو الله', 'محمد'), #Mohammed Abu Allah, the ism should be mohammed
			('ابو الله محمد', 'محمد'), #Abu Allah Mohammed, the ism should be again mohammed
			('عبد الجبار', 'عبد الجبار'), #Abdul Jabbar, the ism should be Abdul Jabbar as Abdul by itself it's not a name but needs to be associated to the next time, as it means "Servant of"
			('أبدول أبدول أبدول أبدول عبد جبار', 'أبدول أبدول أبدول أبدول عبد جبار'), #Abdul abdul abdul abdul abdul Jabbar, all the Abduls should be considered together with Jabbar (Edge Case)
			('محمد بن لادن', 'محمد'),#Mohammed Ben Laden, Ben is a nasab so mohammed should be the ism 
			('أبدل آل كا', 'أبدل آل كا'), #Abdul Al Ka, they should all be part of the ism, so ism should be Abdul Al Ka as well
			('محمد جبار باروبارو', 'محمد')] #Mohammed Jabbar Barubaru, Mohammed should be the ism as there are no kunya or nasab into the string

nasab_list = [('بن لادن', 'بن لادن'), #Ben Laden, being composed by Ben + word, with Ben indicating "son of", the nasab should be Ben Laden
			  ('بن بن لادن', 'بن بن لادن'), #Ben Ben Laden, they should all be concatenated together, and hence the nasab should be Ben Ben Laden
			  ('بن بن بن لادن', 'بن بن بن لادن'), #Ben (x3) Laden, same as above
			  ('بن بن بن بن بن بن بن بن لادن', 'بن بن بن بن بن بن بن بن لادن'), #Ben (x8) Laden, same as above
			  ('بن عبد الجبار', 'بن عبد الجبار'), #Ben Abdul Jabbar, the name Abdul should be attached to the next name, so the nasab should be Ben Abdul Jabbar
			  ('محمد بنت جبار', 'بنت جبار'), #Mohammed Bint Jabbar, so Bint Jabber should be nasab in this case
			  ('محمد باروبارو بنت جبار أفغاني كاكوتاني', 'بنت جبار')] #Mohammed Barubaru Bint Jabbar Afghani Kakutani, so the nasab should be Bint Jabbar

kunya_list = [('محمد أبو جبار', 'أبو جبار'), #Mohammed Abu Jabbar, Abu Jabbar should be the Kunya
			  ('محمد',''), #Mohammed, there should be no Kunya here 
			  ('محمد أبو أبو أبو أبو جبار', 'أبو أبو أبو أبو جبار'), #Mohammed Abu(x4) Jabbar, Abu(x4) Jabbar should be the Kunya (Edge Case)
			  ('محمد بن لادن أبو جبار', 'أبو جبار'), #Mohammed Ben Laden Abu Jabbar, Abu Jabbar should be the Kunya here
			  ('محمد أبو جبار بن لادن', 'أبو جبار'), #Mohammed Abu Jabbar Ben Laden, Abu Jabbar should be the Kunya here
			  ('أبو جبار', 'أبو جبار'), #Abu Jabbar, it is by itself a Kunya
			  ('أبو جبار أبو تشوبار', 'أبو جبار أبو تشوبار'), #Abu Jabbar Abu Chubar, both of them are Kunya and should be included as such 
			  ('أبو جبار أبو تشوبار أبو برابدو أبو لوي', 'أبو جبار أبو تشوبار أبو برابدو أبو لوي'), #Abu Jabbar Abu Chubar Abu Baradu Abu Lui, they should all be included as Kunya (Edge Case)
			  ('نيكوديمو بن فاليريو أبو نون آل إيطاليا', 'أبو نون'), #Nicodemo Ben Valario Abu Nun of Atali, Abu Nun is the kunya in this case
			  ('نيكوديمو بن فاليريو', ''), #Nicodemo Ben Valario, no kunya here as there is an ism and a nasab
			  ('محمد أم جبار', 'أم جبار'), #Mohammed Um Jabbar, Um Jabbar should the Kunya (for the mother)
			  ('محمد أوم جبار', 'أوم جبار')] #Mohammed Oum Jabbar, Oum Jabbar should the Kunya (for the mother)

laqab_list  = [('نيكوديمو بن فاليريو',''), #Nicodemo Ben Valario, no laqab here as there is an ism and a nasab
			   ('محمد الفاييت بن لادن', 'الفاييت'), #Mohammed al Fayette ben Laden, Al Fayette should be the laqab here
			   ('محمد الفاييت بن جيوفاني أبو لادن','الفاييت'), #Mohammed al Fayette ben Giovani ben Laden, Al Fayette should be the laqab here
			   ('محمد الفاييت بن جيوفاني أبو لادن الأفغاني محامدي', 'الفاييت'), #Mohammed al Fayette ben Giovani abu Laden al Afghani Muhamadi, Al Fayette should be the laqab here
			   ('محمد الفاييت العدواني', 'العدواني')] #Muhammad al-Fayyat al-Adwani, al-Adwani should be the laqab here as it is one of the names which we are sure of being a laqab and included in the laqab_list in the pars_obj.py

nisbah_list = [('محمد الفاييت ابو لادن', ''), #Mohammed al-Fayyat Abu-Ladin, there is no nisbah as there is one ism, one laqab and one kunya
			   ('محمد', ''), #Mohammed, there should be no nisbah here as Mohammed is just the ism
			   ('محمد بن لادن الفياطي', 'الفياطي'), #Mohammed Ben Laden al-Fayati, Al-Fayati should be the nisbah as it follows the nasab
			   ('محمد أبو لادن الفاتي','الفاتي'), #Mohammed abu Laden Al-Fayati, Al-Fayati should be the nisbah as it follows the nkunya
			   ('محمد أبو لادن بن غاريون الفاتي','الفاتي'), #Mohammed abu Laden ben garion al-Fayati, al-Fayati should be identified as the nisbah here after both a kunya and a nasab
			   ('محمد أبو لادن بن غاريون الفاتي الأفغاني','الفاتي')] #Mohammed abu Laden ben garion al-Fayati afghani, al-Fayati should be identified as the nisbah


laqab_nisbah_list = [('محمد جبار بن لادن', ''), #Mohammed jabbar ben laden, laqab/nisbah should be empty here.
					 ('محمد جبار لادن', 'جبار لادن'), #Mohammed jabbar laden, laqab/nisbah should be capturing aything after the ism up to two words
					 ('محمد جبار', 'جبار'), #Mohammed jabbar, Jabbar should be considered as laqab/nisbah
					 ('محمد جبار أفغاني كازاكي كاكوتاني', 'جبار أفغاني'), #Mohammed jabbar afghani kazaki kakutani, Jabbar Afghani should be considered as laqab/nisbah.
					 ('محمد جبار باروبارو', 'جبار باروبارو')] #Mohammed Jabbar Barubaru, Jabbar Barubaru should be the included in the laqab/nisbah part

other_list = [('محمد جبار بن لادن', ''), #Mohammed jabbar ben laden, other should be empty here.
			  ('محمد جبار بن لادن أفغاني كازاكي كاكوتاني', 'كازاكي كاكوتاني'), #Mohammed jabbar ben laden afghani kazaki kakutani. In this case the kazaki kakutani should be in other 
			  ('محمد جبار أفغاني كازاكي كاكوتاني', 'كازاكي كاكوتاني'), #Mohammed jabbar afghani kazaki kakutani, in this case again kazaki kakutani should be in other
			  ('محمد أبو لادن بن غاريون الفاتي الأفغاني','الأفغاني')] #Mohammed abu Laden ben garion al-Fayati afghani, afghani should be identified as in the "other" category

full_test_list = [('محمد جبار بن لادن أبو أحمد الأفغاني', [('ISM', u'محمد'), 
														   ('LAQAB', u'جبار'), 
														   ('NASAB', u'بن لادن'),
														   ('KUNYA', u'أبو أحمد'),
														   ('NISBAH', u'الأفغاني'),
														   ('LAQAB/NISBAH', ''), 
														   ('OTHER', '')] ),
				#Mohammed Jabbar ben Laden Abu Ahmed Afghani, Mohammed should be the ism, Jabbar the laqab, ben Laden should be the nasab, abu Ahmed the kunya and Afghani the nisbah. LAQAB/NISBAH and OTHER category should hence be empty
				('محمد جبار بن لادن أبو أحمد الأفغاني كاكوتاني', [('ISM', u'محمد'), 
														   ('LAQAB', u'جبار'), 
														   ('NASAB', u'بن لادن'),
														   ('KUNYA', u'أبو أحمد'),
														   ('NISBAH', u'الأفغاني'),
														   ('LAQAB/NISBAH', ''), 
														   ('OTHER', u'كاكوتاني')] )
				#Mohammed Jabbar ben Laden Abu Ahmed Afghani Kakutani, Mohammed should be the ism, Jabbar the laqab, ben Laden should be the nasab, abu Ahmed the kunya, Afghani the nisbah and Kakutani should end up in "Other". LAQAB/NISBAH category should hence be empty
				]


test_dict = {'ISM': ism_list, 
			 'LAQAB': laqab_list, 
			 'NASAB': nasab_list,
			 'KUNYA': kunya_list,
			 'NISBAH': nisbah_list, 
			 'LAQAB/NISBAH':laqab_nisbah_list,
			 'OTHER':other_list,
			 'FULL_TEST': full_test_list}