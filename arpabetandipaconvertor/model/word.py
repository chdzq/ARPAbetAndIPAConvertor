# -*- coding: utf-8 -*-
from arpabetandipaconvertor.model.stress import Stress

class Word:

    def __init__(self):
        self._syllable_list = []
        self._stress_count = 0

    def add_syllable(self, syllable):
        if (not syllable) or syllable.is_empty():
            return
        self._syllable_list.append(syllable)
        if syllable.have_vowel:
            self._stress_count += 1

    def translate_to_arpabet(self):
        translations = []

        for syllable in self._syllable_list:
            if syllable.have_vowel and self._stress_count <= 1:
                syllable.stress = Stress.Primary
            translations.append(syllable.translate_to_arpabet())

        return " ".join(translations)

    def translate_to_american_phonetic_alphabet(self):
        translations = ""

        for i, syllable in enumerate(self._syllable_list):
            translations += syllable.translate_to_american_phonetic_alphabet(hide_stress_mark=0 == i and 1 >= self._stress_count)

        return translations

    def translate_to_english_phonetic_alphabet(self, need_show_stress=False):
        translations = ""

        for i, syllable in enumerate(self._syllable_list):
            translations += syllable.translate_to_english_phonetic_alphabet(hide_stress_mark=0 == i and 1 >= self._stress_count)

        return translations

    def translate_to_international_phonetic_alphabet(self, need_show_stress=False):
        translations = ""

        for i, syllable in enumerate(self._syllable_list):
            translations += syllable.translate_to_english_phonetic_alphabet(hide_stress_mark=0 == i and 1 >= self._stress_count)

        return translations