import unittest
from arpabetandipaconvertor.arpabet2phoneticalphabet import ARPAbet2PhoneticAlphabetConvertor
from arpabetandipaconvertor.model.syllable import Stress


class TestIPAToARPAbet(unittest.TestCase):

    def setUp(self):
        self._arpabet_convertor = ARPAbet2PhoneticAlphabetConvertor()

    def test_convertor_ipa(self):
        f = self._arpabet_convertor.convert_to_american_phonetic_alphabet('F AW1 N D')
        self.assertEqual(f, 'faʊnd')
        # ri'trai
        f = self._arpabet_convertor.convert_to_american_phonetic_alphabet('R IY0 T R AY1')
        self.assertEqual(f, 'riˈtraɪ')

        # ˈɛniˌwʌn, -wən
        f = self._arpabet_convertor.convert_to_american_phonetic_alphabet('EH1 N IY0 W AH2 N')
        self.assertEqual(f, 'ˈɛniˌwʌn')
        #kʊd
        f = self._arpabet_convertor.convert_to_american_phonetic_alphabet('K UH1 D')
        self.assertEqual(f, 'kʊd')

        f = self._arpabet_convertor.convert_to_american_phonetic_alphabet("W IY1 L K IY0 N S N")
        self.assertEqual(f, 'ˈwilkinsn')
