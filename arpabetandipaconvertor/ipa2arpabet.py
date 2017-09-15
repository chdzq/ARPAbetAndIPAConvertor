#!/usr/bin/env python
# -*- coding: utf-8 -*-

from arpabetandipaconvertor import vowels, consonants, no_stress_arpabet, primary_stress_arpabet, primary_stress_ipa, \
    secondary_stress_arpabet, secondary_stress_ipa, Phoneme, ipa_stop_libs

from arpabetandipaconvertor.excepts import KeyError

class IPA2ARPAbetConvertor:

    def __init__(self):
        '''
        装配数据
        '''
        self._ipa_tree = {}
        for o in vowels:
            self._ipa_tree[o[1]] = Phoneme(o[0], True)

        for o in consonants:
            self._ipa_tree[o[1]] = Phoneme(o[0], False)

        self._stop_libs_dic = {}

        for str in ipa_stop_libs:
            self._stop_libs_dic[str] = True

        self._stress_libs_dic = {}
        for str in primary_stress_ipa:
            self._stress_libs_dic[str] = primary_stress_arpabet

        for str in secondary_stress_ipa:
            self._stress_libs_dic[str] = secondary_stress_arpabet

    def _is_stop(self, c):
        return self._stop_libs_dic.get(c, False)

    def _deal_arpabet_ifneed(self, temp_arpabet_list, stress_list):
        '''
        临时缓存arpabet最后一个arpabet就是合法完整音符。压进去的重音表示在元音之后，没有重音，元音后面加上0，
        :param temp_arpabet_list:
        :param stress_list:
        :return:
        '''
        if temp_arpabet_list:
            temp_arpabet = temp_arpabet_list[-1]
            arpabet = temp_arpabet.get_value()
            if temp_arpabet.is_vowels():
                stress_arpabet = 0
                if stress_list:
                    stress_arpabet = stress_list[-1]
                    stress_list.clear()
                arpabet += str(stress_arpabet)
            return arpabet
        return None

    def convert(self, ipa):
        if not ipa:
            return None
        temp_arpabet_list = []
        temp_ipa = ''
        stress_list = []
        arpabet_list = []

        '''
        1、是重音标识，入lifo
        '''
        found_arpabet = None
        for index, ch in enumerate(ipa):
            print(ch, index)
            if self._is_stop(c=ch):
                break

            stress_arpabet = self._stress_libs_dic.get(ch, None)
            if stress_arpabet:
                if (not found_arpabet) and index > 0:
                    raise KeyError('存在不能识别的音标')
                else:
                    arpabet = self._deal_arpabet_ifneed(temp_arpabet_list, stress_list)
                    if arpabet:
                        arpabet_list.append(arpabet)
                        temp_arpabet_list.clear()
                        print(temp_ipa, arpabet)
                    temp_ipa = ''
                    stress_list.clear()
                    stress_list.append(stress_arpabet)
                    continue
            temp_ipa += ch
            find_arpabet = self._ipa_tree.get(temp_ipa, None)

            if found_arpabet and (not find_arpabet):
            #说明前面存的是一个正常的音符
                arpabet = self._deal_arpabet_ifneed(temp_arpabet_list, stress_list)
                if arpabet:
                    arpabet_list.append(arpabet)
                    print(temp_ipa, arpabet)
                    temp_arpabet_list.clear()
                    temp_ipa = ch
                    find_arpabet = self._ipa_tree.get(ch, None)
                    found_arpabet = find_arpabet
                    if find_arpabet:
                        temp_arpabet_list.append(find_arpabet)
                else:
                    found_arpabet = find_arpabet
                    if find_arpabet:
                        temp_arpabet_list.append(find_arpabet)
            else:
                found_arpabet = find_arpabet
                if find_arpabet:
                    temp_arpabet_list.append(find_arpabet)

        if found_arpabet:
            arpabet = self._deal_arpabet_ifneed(temp_arpabet_list, stress_list)
            if arpabet:
                arpabet_list.append(arpabet)
                print(temp_ipa, arpabet)
                temp_arpabet_list.clear()
        else:
            raise KeyError('存在不能识别的音标')

        return " ".join(arpabet_list)
