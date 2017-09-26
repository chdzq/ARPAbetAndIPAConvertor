# -*- coding: utf-8 -*-

'''
音节
'''

from arpabetandipaconvertor.excepts import PhonemeError
from arpabetandipaconvertor.model.stress import Stress

class Syllable:

    def __init__(self):
        self._stress = None
        self._phoneme_list = []
        self._have_vowel = False

    @property
    def stress(self):
        return self._stress

    @stress.setter
    def stress(self, value):
        self._stress = value

    @property
    def have_vowel(self):
        return self._have_vowel

    def is_empty(self):
        return len(self._phoneme_list) <= 0

    def add_phoneme(self, phoneme):
        if not phoneme:
            return
        self._phoneme_list.append(phoneme)
        if phoneme.is_vowel:
            if not self.stress:
                self.stress = Stress.No
            self._have_vowel = True

    def translate_to_arpabet(self):
        '''
        转换成arpabet
        :return:
        '''

        translations = []

        for phoneme in self._phoneme_list:
            if phoneme.is_vowel:
                translations.append(phoneme.arpabet + self.stress.mark_arpabet())
            else:
                translations.append(phoneme.arpabet)

        return " ".join(translations)

    def translate_to_american_phonetic_alphabet(self, hide_stress_mark=False):
        '''
        转换成美音音。只要一个元音的时候需要隐藏重音标识
        :param hide_stress_mark:
        :return:

        '''

        translations = self.stress.mark_ipa() if (not hide_stress_mark) and self.have_vowel else ""

        for phoneme in self._phoneme_list:
            translations += phoneme.american

        return translations

    def translate_to_english_phonetic_alphabet(self, hide_stress_mark=False):
        '''
        转换成英音。只要一个元音的时候需要隐藏重音标识
        :param hide_stress_mark:
        :return:
        '''

        translations = self.stress.mark_ipa() if (not hide_stress_mark) and self.have_vowel else ""

        for phoneme in self._phoneme_list:
            translations += phoneme.english

        return translations

    def translate_to_international_phonetic_alphabet(self, hide_stress_mark=False):
        '''
        转换成国际音标。只要一个元音的时候需要隐藏重音标识
        :param hide_stress_mark:
        :return:
        '''

        translations = self.stress.mark_ipa() if (not hide_stress_mark) and self.have_vowel else ""

        for phoneme in self._phoneme_list:
            translations += phoneme.ipa

        return translations



