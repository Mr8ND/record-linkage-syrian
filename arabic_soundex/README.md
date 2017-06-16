## ARABIC SOUNDEX

This is the repository for the code of the arabic soundex.

The main function for the soundex is __arabicSoundexMain__. It is thought to work on a single word, but it would work with multiple words as well - it was not thought for that though.
Main arguments are:
* firstcharuniforming: according to both the implementations cited below, the first characters in Arabic strings do not really matter, in contrast with what happends in the English language. If this is set to True, the first character of the word is ignored and assign a placeholder value (currently 'x'). Default is True;
* firstletter_rem: There are three first letters which are not pronounced if they are at the beginning of the word in Arabic. If this is True, these letters are ignored;
* accents_strip: If True, the string is stripped for accents. Soundex should be already account for accents in the lookup, it is an extra layer of security for that. Defaulted is True;
* lim: Integer value. If not None, forces the soundex representation to be composed a number of numbers orcharacters equal to lim after the first character. If the soundex representation was longer, this would cut it. If it was shorter, it would fill the spaces with 0. E.g. with lim=3 : x7213 is set to x721 and x7 to x700.


The function __arabicSoundexNames__ is just a wrapper for multiple words string. It will get the soundex representation for each of the words of the string. The *args and **kwargs for the main Arabic Soundex function can be passed in there.


### DISCLAIMER

This arabic soundex implementation is a mix of both Google Chromium Repository, which was itself translated from Tamman Koujian's C# version.
Both link below:

* https://chromium.googlesource.com/external/googleappengine/python/+/4709197c830fd17d9a9f0f80e1533a8f0597153b/lib/whoosh/whoosh/lang/phonetic.py
* https://www.codeproject.com/Articles/26880/Arabic-Soundex

Pronunciation and sounds of unicode characters not included in the above sites, more explicitely u0641, u0629 and u621 were taken from https://codepoints.net/.