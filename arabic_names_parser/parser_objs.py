# -*- coding: utf-8 -*-
from parser_utils import Astr

#### Defining here which are the words which signal the beginning of a particular part of the name.

nasab_dict ={Astr('بن '): ['bin', 'ben', 'ibn'],
             Astr('بنت '): ['bint']}

kunya_dict = {Astr('أبو '): ['abu'], Astr('ابو '):['abu'],
              Astr('أم '): ['umm', 'oum']}

nisbah_dict = {Astr('من_ال_'): ['of the']}

name_part_dict = {'nasab': nasab_dict, 'kunya': kunya_dict, 'nisbah': nisbah_dict}


#### Defininig here the arabic words which should be aggregated to the following.

al_list = [Astr('آل '), Astr('ال '), Astr('من ')]
abdul_list = [Astr('عبد '), Astr('عبدو '), Astr('أبدول '), Astr('أبدل ')]
master_list = [Astr('السيد '), Astr('سيد '), Astr('السيدة ')]

concat_list = al_list + abdul_list + master_list