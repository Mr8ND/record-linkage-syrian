# -*- coding: utf-8 -*-
from parser_utils import Astr

#### Defining here the arabic names which define an arabic name part 

nasab_dict ={Astr('بن '): ['bin', 'ben', 'ibn'],
             Astr('بنت '): ['bint']}

kunya_dict = {Astr('أبو '): ['abu'],
              Astr('أم '): ['umm', 'oum']}

nisbah_dict = {Astr('من_ال_'): ['of the']}

name_part_dict = {'nasab': nasab_dict, 'kunya': kunya_dict, 'nisbah': nisbah_dict}


#### Defininig here the arabic words which should be aggregated to the following one

al_list = [Astr('آل '), Astr('ال '), Astr('من ')]
abdul_list = [Astr('عبد '), Astr('عبدو ')]
master_list = [Astr('السيد '), Astr('سيد '), Astr('السيدة ')]

concat_list = al_list + abdul_list + master_list