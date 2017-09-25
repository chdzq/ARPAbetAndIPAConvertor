# -*- coding: utf-8 -*-


'''
音素
'''
class Phoneme:

    def __init__(self, arpabet, american, english, ipa, is_vowel):
        '''
        :param arpabet: ARPAbet
        :param american: 美音
        :param english: 英音
        :param ipa: 国际音标
        :param is_vowel: 是否是元音
        '''
        self._arpabet = arpabet
        self._american = american
        self._english = english
        self._is_vowel = is_vowel
        self._ipa = ipa

    @property
    def ipa(self):
        return self._ipa

    @property
    def english(self):
        return self._english

    @property
    def american(self):
        return self._american

    @property
    def arpabet(self):
        return self._arpabet

    @property
    def is_vowel(self):
        return self._is_vowel
