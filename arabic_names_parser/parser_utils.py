def Astr(string):
    return unicode(string, encoding='utf-8')


def readjustSpacesInString(string):
    return ' '.join([x for x in string.split(' ') if x])


def cleanConcatFunction(string):
    return string.replace('_', ' ')


def isolateNextWordDictKeys(arab_string, dict_keys):
    extraction, before = '', ''
    
    for prefix in dict_keys:
        if prefix in arab_string:
            
            count_prefix = arab_string.count(prefix)
            n = len(prefix)
            
            for x in range(count_prefix):
                
                index = arab_string.find(prefix)
                remainder_first_word = readjustSpacesInString(arab_string[index+n:]).split(' ')[0]
                block_sel = readjustSpacesInString(' '.join([prefix, remainder_first_word]))
                extraction += block_sel + ' | '
                
                if x == 0: before += arab_string[:index]
                arab_string = arab_string[:index] + arab_string[index+n+len(remainder_first_word)+1:]

    return extraction, before, arab_string
            

def concatenateFunction(arab_string, elem_list, isolated_flag = True):
    
    mod_arab_string = arab_string
    
    def returnIsolated(elem, arab_string):
        output = True
        if elem in arab_string:
            index = arab_string.find(elem)
            if index >0:
                output = arab_string[index-1] == ' '
        return output
    
    for elem in elem_list:
        if elem in arab_string and (not isolated_flag or returnIsolated(elem, arab_string)):
            obtained, _ , _ = isolateNextWordDictKeys(arab_string, [elem])
            
            if obtained:
                for obt_elem in obtained.split('|'):
                    
                    obt_elem_sub = readjustSpacesInString(obt_elem)
                    mod_arab_string = mod_arab_string.replace(obt_elem_sub, '_'.join(obt_elem_sub.split(' ')))
    
    return mod_arab_string
