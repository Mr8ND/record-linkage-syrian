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

    def identifyNamePartFunction(arab_string, namepart_list):
        np_str, bef_np, arab_string = isolateNextWordDictKeys(arab_string, namepart_list)
        
        if np_str:
            np_str = readjustSpacesInString(np_str.replace('|',''))
        
        return np_str, bef_np, arab_string


    def identifyIsmFromNPFunction(before_string, arab_string, ism_part):

        if before_string and not ism_part:
            ism_part = before_string.split(' ')[0]
            arab_string = arab_string[len(ism_part)+1:]

        return ism_part, arab_string


    nasab, bef_nasab, arab_str = identifyNamePartFunction(arab_str, name_part_dict['nasab'].keys())
    ism, arab_str = identifyIsmFromNPFunction(bef_nasab, arab_str, ism)

    kunya, bef_kunya, arab_str = identifyNamePartFunction(arab_str, name_part_dict['kunya'].keys())
    ism, arab_str = identifyIsmFromNPFunction(bef_kunya, arab_str, ism)

    nisbah, bef_nisbah, arab_str = identifyNamePartFunction(arab_str, name_part_dict['nisbah'].keys())
    

    #If ISM has not been found now the fist word is taken to be the ism.
    #This is the time also to identify whether the ism does exist in the name.
    
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

	for x,y in arabicNameParser(Astr('محمد جبار بن لادن أبو أحمد الأفغاني')):
		print x,y

