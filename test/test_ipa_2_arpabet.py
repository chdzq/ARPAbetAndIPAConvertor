import unittest
from arpabetandipaconvertor.phoneticarphabet2arpabet import PhoneticAlphabet2ARPAbetConvertor
from arpabetandipaconvertor.excepts import PhonemeError


class TestIPAToARPAbet(unittest.TestCase):

    def setUp(self):
        self._ipa_convertor = PhoneticAlphabet2ARPAbetConvertor()

    def test_convertor(self):
        # 单音节及()
        f = self._ipa_convertor.convert('faʊ(hh)nd')
        self.assertEqual(f, 'F AW1 N D')

        # ri'trai 双音节
        f = self._ipa_convertor.convert('riˈtraɪ')
        self.assertEqual(f, 'R IY0 T R AY1')

        # ˈɛniˌwʌn, -wən 三音节
        f = self._ipa_convertor.convert('ˈɛniˌwʌn, -wən')
        self.assertEqual(f, 'EH1 N IY0 W AH2 N')

        #kʊd
        f = self._ipa_convertor.convert('kʊd')
        self.assertEqual(f, 'K UH1 D')

        # wilkinsn 双音节
        f = self._ipa_convertor.convert("'wilkinsn")
        self.assertEqual(f, 'W IY1 L K IY0 N S N')

        # 边缘测试 重音标识位置不对
        with self.assertRaises(PhonemeError) as cm:
            f = self._ipa_convertor.convert("wilkins'n")
        the_exception = cm.exception
        self.assertEqual(the_exception.message, 'ns\' 重音标识不合适，\'前一个音节没有元音！')

        # 边缘测试 重音标识隔断完整的音符
        with self.assertRaises(PhonemeError) as cm:
            f = self._ipa_convertor.convert("wilkins'n")
        the_exception = cm.exception
        self.assertEqual(the_exception.message, 'ns\' 重音标识不合适，\'前一个音节没有元音！')

        # 边缘测试 重音标识不对，并没有元音
        with self.assertRaises(PhonemeError) as cm:
            f = self._ipa_convertor.convert("wilkia'ʊsn")
        the_exception = cm.exception
        self.assertEqual(the_exception.message, '存在不能识别的音标 a')

        # 边缘测试 最后一个音节美音找完整
        with self.assertRaises(PhonemeError) as cm:
            f = self._ipa_convertor.convert("wilki'sna")
        the_exception = cm.exception
        self.assertEqual(the_exception.message, '存在不能识别的音标 a')

        # 边缘测试 中间一个不完整的音节连带到做好匹配不到合适的音标
        with self.assertRaises(PhonemeError) as cm:
            f = self._ipa_convertor.convert("wilki'san")
        the_exception = cm.exception
        self.assertEqual(the_exception.message, '存在不能识别的音标 an')






