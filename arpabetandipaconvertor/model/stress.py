# -*- coding: utf-8 -*-

# no_stress_arpabet = 0
# primary_stress_arpabet = 1
# secondary_stress_arpabet = 2

from enum import Enum,unique

@unique
class Stress(Enum):
    No = 0,         '''无重音'''
    Primary = 1,    '''重音'''
    Secondary = 2,  '''次重音'''

    def mark_ipa(self):
        if Stress.No == self:
            return ''
        elif Stress.Primary == self:
            return 'ˈ'
        else:
            return 'ˌ'

    def mark_arpabet(self):
        return str(self.value[0])
