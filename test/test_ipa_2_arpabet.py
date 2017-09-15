import unittest
from arpabetandipaconvertor.ipa2arpabet import IPA2ARPAbetConvertor
class TestIPAToARPAbet(unittest.TestCase):

    def setUp(self):
        self._ipa_convertor = IPA2ARPAbetConvertor()

    def test_convertor(self):
        f = self._ipa_convertor.convert('faʊnd')
        self.assertEqual(f, 'F AW0 N D')
        # ri'trai
        f = self._ipa_convertor.convert('ri\'traɪ')
        self.assertEqual(f, 'R IY0 T R AY1')

        # ˈɛniˌwʌn, -wən
        f = self._ipa_convertor.convert('ˈɛniˌwʌn, -wən')
        self.assertEqual(f, 'EH1 N IY0 W AH2 N')
        #kʊd
        f = self._ipa_convertor.convert('kʊd')
        self.assertEqual(f, 'K UH0 D')


