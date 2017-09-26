#!/usr/bin/env python
# -*- coding: utf-8 -*-

from arpabetandipaconvertor import vowels, consonants, primary_stress_ipa, \
    secondary_stress_ipa, ipa_stop_libs, skip_libs

from arpabetandipaconvertor.excepts import PhonemeError
from arpabetandipaconvertor.model.syllable import Syllable
from arpabetandipaconvertor.model.word import Word
from arpabetandipaconvertor.model.stress import Stress
from enum import Enum, unique

@unique
class ConvertPriority(Enum):
    American = 0
    English = 1
    IPA = 2

class PhoneticAlphabet2ARPAbetConvertor:

    def __init__(self):
        '''
        装配数据
        '''
        self._ipa_tree = {}
        self._kk_tree = {}
        self._dj_tree = {}

        for o in vowels:
            self._ipa_tree[o.ipa] = o
            self._kk_tree[o.american] = o
            self._dj_tree[o.english] = o

        for o in consonants:
            self._ipa_tree[o.ipa] = o
            self._kk_tree[o.american] = o
            self._dj_tree[o.english] = o

        self._stop_libs_dic = {}
        for str in ipa_stop_libs:
            self._stop_libs_dic[str] = True

        self._skip_dic = {}
        for skip in skip_libs:
            self._skip_dic[skip[0]] = skip[1]

        self._stress_libs_dic = {}
        for str in primary_stress_ipa:
            self._stress_libs_dic[str] = Stress.Primary

        for str in secondary_stress_ipa:
            self._stress_libs_dic[str] = Stress.Secondary

    def _is_stop(self, c):
        return self._stop_libs_dic.get(c, False)

    def _find_phoneme_in_arphabet_list(self, phoneme_string, arphabet_list):
        temp_phoneme = None
        for arphabet in arphabet_list:
            temp_phoneme = arphabet.get(phoneme_string, None)
            if temp_phoneme:
                break
        return temp_phoneme

    def _create_arphabet_list(self, priority):
        if ConvertPriority.American == priority:
            return [self._kk_tree, self._ipa_tree, self._dj_tree]

        if ConvertPriority.English == priority:
            return [self._dj_tree, self._ipa_tree, self._kk_tree]

        if ConvertPriority.IPA == priority:
            return [self._ipa_tree, self._kk_tree, self._dj_tree]

    def convert(self, arphabet, priority=ConvertPriority.American):
        if not arphabet:
            return None

        temp_ch = ''            #临时转换的字符串
        skip_stack = []         #跳过的栈。如（）

        arphabet_list = self._create_arphabet_list(priority=priority)

        last_phoneme = None     #上一次的音素

        word = Word()           #单词
        syllable = Syllable()   #音节
        temp_syllable_str = ""

        for index, ch in enumerate(arphabet):
            if self._is_stop(c=ch):
                break
            temp_syllable_str += ch
            if skip_stack:
                if ch == self._skip_dic.get(skip_stack[-1]):
                    skip_stack.pop()
                continue
            else:
                if self._skip_dic.get(ch):
                    skip_stack.append(ch)
                    continue

            stress = self._stress_libs_dic.get(ch, None)
            if stress:
                if (not last_phoneme) and index > 0:
                    raise PhonemeError('存在不能识别的音标 %s' % temp_ch)
                else:
                    '''
                    遇到重音标识，说明前面是是一个音节，添加到word中，并清空last_phoneme及temp_ch
                    '''
                    if last_phoneme:
                        syllable.add_phoneme(phoneme=last_phoneme)
                        if not syllable.have_vowel:
                            raise PhonemeError("%s 重音标识不合适，%s前一个音节没有元音！" % (temp_syllable_str, ch))
                        word.add_syllable(syllable=syllable)
                        syllable = Syllable()
                    last_phoneme = None
                    temp_ch = ''
                    temp_syllable_str = ch
                    syllable.stress = stress
                    continue

            temp_ch += ch
            temp_phoneme = self._find_phoneme_in_arphabet_list(phoneme_string=temp_ch,
                                                               arphabet_list=arphabet_list)

            if last_phoneme and (not temp_phoneme):
                '''
                说明前面是是一个完整音标
                '''
                syllable.add_phoneme(last_phoneme)
                if last_phoneme.is_vowel:
                    word.add_syllable(syllable)
                    syllable = Syllable()
                    temp_syllable_str = ch

                temp_ch = ch
                last_phoneme = self._find_phoneme_in_arphabet_list(phoneme_string=temp_ch,
                                                                   arphabet_list=arphabet_list)

            else:
                last_phoneme = temp_phoneme

        if last_phoneme:
            syllable.add_phoneme(last_phoneme)
            if syllable.stress and not syllable.have_vowel:
                raise PhonemeError("%s 有重音标识但并没有元音！" % temp_syllable_str)
            word.add_syllable(syllable)
        else:
            raise PhonemeError('存在不能识别的音标 %s' % temp_ch)

        return word.translate_to_arpabet()
