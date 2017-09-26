# -*- coding: utf-8 -*-
from arpabetandipaconvertor import vowels, consonants

from arpabetandipaconvertor.excepts import PhonemeError
from arpabetandipaconvertor.model.syllable import Syllable
from arpabetandipaconvertor.model.word import Word
from arpabetandipaconvertor.model.stress import Stress

class ARPAbet2PhoneticAlphabetConvertor:

    def __init__(self):
        '''
        装配数据
        '''
        self._arpabet_tree = {}

        for o in vowels:
            self._arpabet_tree[o.arpabet] = o

        for o in consonants:
            self._arpabet_tree[o.arpabet] = o

        self._stress_libs_dic = {Stress.No.mark_arpabet(): Stress.No,
                                 Stress.Primary.mark_arpabet(): Stress.Primary,
                                 Stress.Secondary.mark_arpabet(): Stress.Secondary}

    def _is_stop(self, c):
        return self._stop_libs_dic.get(c, False)

    def _convert_to_word(self, arpabet):

        if not arpabet:
            return None

        arpabet_phoneme_list = arpabet.split()
        word = Word()           #单词
        syllable = Syllable()   #音节

        for arphabe_phoneme in arpabet_phoneme_list:
            phoneme = self._arpabet_tree.get(arphabe_phoneme)
            if phoneme:
                syllable.add_phoneme(phoneme=phoneme)
                if phoneme.is_vowel:
                    word.add_syllable(syllable=syllable)
                    syllable = Syllable()
            else:
                last_num = arphabe_phoneme[-1]
                if not last_num.isdigit():
                    raise PhonemeError("%s 匹配不到合适的音标" % arphabe_phoneme)

                stress = self._stress_libs_dic.get(last_num)

                before = arphabe_phoneme[:-1]

                phoneme = self._arpabet_tree.get(before)

                if phoneme:
                    syllable.add_phoneme(phoneme=phoneme)
                    if stress:
                        syllable.stress = stress
                    else:
                        raise PhonemeError("%s 的重音标识不对，标记成了 %s" % (before, last_num))

                    if phoneme.is_vowel:
                        word.add_syllable(syllable=syllable)
                        syllable = Syllable()
                    else:
                        raise PhonemeError("%s 重音标识位置不对，当前 %s 不是元音" % (arphabe_phoneme, before))
                else:
                    raise PhonemeError("%s 匹配不到合适的音标" % before)

        word.add_syllable(syllable=syllable)

        return word

    def convert_to_international_phonetic_alphabet(self, arpabet):
        '''
        转换成国际音标
        :param arpabet:
        :return:
        '''

        word = self._convert_to_word(arpabet=arpabet)

        if not word:
            return None

        return word.translate_to_international_phonetic_alphabet()

    def convert_to_american_phonetic_alphabet(self, arpabet):
        '''
        转换成美音
        :param arpabet:
        :return:
        '''

        word = self._convert_to_word(arpabet=arpabet)

        if not word:
            return None

        return word.translate_to_american_phonetic_alphabet()

    def convert_to_english_phonetic_alphabet(self, arpabet):
        '''
        转换成英音
        :param arpabet:
        :return:
        '''

        word = self._convert_to_word(arpabet=arpabet)

        if not word:
            return None

        return word.translate_to_english_phonetic_alphabet()

