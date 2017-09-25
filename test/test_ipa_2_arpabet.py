import unittest
from arpabetandipaconvertor.phoneticarphabet2arpabet import PhoneticAlphabet2ARPAbetConvertor
from arpabetandipaconvertor.model.syllable import Stress


class TestIPAToARPAbet(unittest.TestCase):

    def setUp(self):
        self._ipa_convertor = PhoneticAlphabet2ARPAbetConvertor()

    def test_convertor(self):
        f = self._ipa_convertor.convert('faʊ(hh)nd')
        self.assertEqual(f, 'F AW1 N D')
        # ri'trai
        f = self._ipa_convertor.convert('riˈtraɪ')
        self.assertEqual(f, 'R IY0 T R AY1')

        # ˈɛniˌwʌn, -wən
        f = self._ipa_convertor.convert('ˈɛniˌwʌn, -wən')
        self.assertEqual(f, 'EH1 N IY0 W AH2 N')
        #kʊd
        f = self._ipa_convertor.convert('kʊd')
        self.assertEqual(f, 'K UH1 D')

        f = self._ipa_convertor.convert("'wilkinsn")
        self.assertEqual(f, 'W IY1 L K IY0 N S N')




