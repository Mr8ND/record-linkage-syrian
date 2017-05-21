# -*- coding: utf-8 -*-
from parser_utils import Astr, readjustSpacesInString, isolateNextWordDictKeys, concatenateFunction, cleanConcatFunction
from parser_objs import name_part_dict, concat_list


def arabicNameParser(arab_str, name_dict = name_part_dict, conc_list = concat_list):
    
    ism, laqab, nasab, kunya, nisbah, laqnisb, other = '', '', '', '', '', '', ''
    
    #A little bit of pre-processing.
    #The words with ' ال' + another name are actually a single name. They should therefore be a single name.
    #Same goes for the word "", which translates FROM.
    #Same with the words that translates to Abdul or Abdel.
    #They should also be a single word.
    
    arab_str = concatenateFunction(arab_str, conc_list)
    
    
    #Now the first step for the name is to identify either the Nasab or Kunya.
    #If we identify any of them and there are words before, the first one is an ism.
    #This does not work for a Nisbah though, we will just include it the nisbah if we can
    #identify it.
    
    nasab_str, bef_nasab, arab_str = isolateNextWordDictKeys(arab_str, name_part_dict['nasab'].keys())
    if nasab_str:
        nasab = readjustSpacesInString(nasab_str.replace('|',''))
        if bef_nasab:
            ism = bef_nasab.split(' ')[0]
            arab_str = arab_str[len(ism)+1:]
    
    kunya_str, bef_kunya, arab_str = isolateNextWordDictKeys(arab_str, name_part_dict['kunya'].keys())
    if kunya_str:
        kunya = readjustSpacesInString(kunya_str.replace('|',''))
        if bef_kunya and (not ism):
            print 'entered'
            ism = bef_kunya.split(' ')[0]
            arab_str = arab_str[len(ism)+1:]
    
    
    nisbah_str, bef_nisbah, arab_str = isolateNextWordDictKeys(arab_str, name_part_dict['nisbah'].keys())
    if nisbah_str:
        nisbah = readjustSpacesInString(nisbah_str.replace('|',''))
    
        
    if not ism:
        if len(arab_str)==0:
            print 'The string does not seem to contain any ISM.'
        else:
            ism = arab_str.split(' ')[0]
    
    #Now we are left with identifying general nisbah or laqab.
    #We know what was before both the kunya and nasab, and that should be the laqab.
    #What was after is usually the nisbah.
    
    flag_names = int(nasab is not '') + int(kunya is not '')
    
    if flag_names>0:
        rem_bef = bef_kunya.replace(ism+' ', '') if flag_names==2 else bef_nasab.replace(ism+' ', '')
        after_str = arab_str.replace(bef_kunya+' ', '') if flag_names==2 else arab_str.replace(bef_nasab+' ', '')
        if rem_bef and len(rem_bef)>=1:
            laqab += rem_bef
        if after_str and len(after_str)>=1:
            nisbah += after_str.split(' ')[0]
            other += ' '.join(after_str.split(' '))[1:] if len(after_str.split(' '))>1 else ''
    
    else:
        
    #If no nasab or kunya, the two after the name should be either laqab/nisbah.
    #If there are more than two after the ism, then the rest goes in other.
        
        arab_str_noism = arab_str.replace(ism+' ', '')
        n = len(arab_str_noism.split(' '))
        if n<=2:
            laqnisb += arab_str_noism
        else:
            laqnisb += ' '.join(arab_str_noism.split(' ')[:2])
            other += ' '.join(arab_str_noism.split(' ')[2:])
        
    return [tuple(['ISM', cleanConcatFunction(ism)]),
            tuple(['LAQAB', cleanConcatFunction(laqab)]),
            tuple(['NASAB', cleanConcatFunction(nasab)]), 
            tuple(['KUNYA', cleanConcatFunction(kunya)]),
            tuple(['NISBAH', cleanConcatFunction(nisbah)]),
            tuple(['LAQAB/NISBAH', cleanConcatFunction(laqnisb)]),
            tuple(['OTHER', cleanConcatFunction(other)])]


if __name__ == "__main__":

	for x,y in arabicNameParser(Astr('من ال السهو')):
		print x,y

