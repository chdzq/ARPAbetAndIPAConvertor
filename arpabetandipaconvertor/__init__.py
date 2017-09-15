#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
参考
https://en.wikipedia.org/wiki/ARPABET
'''

'''
ARPABET	IPA	Example(s)
1-letter	2-letter
a	AA	ɑ	balm, bot
@	AE	æ	bat
A	AH	ʌ	butt
c	AO	ɔ	bought
W	AW	aʊ	bout
x	AX	ə	about
N/A	AXR[4]	ɚ	letter
Y	AY	aɪ	bite
E	EH	ɛ	bet
R	ER	ɝ	bird
e	EY	eɪ	bait
I	IH	ɪ	bit
X	IX	ɨ	roses, rabbit
i	IY	i	beat
o	OW	oʊ	boat
O	OY	ɔɪ	boy
U	UH	ʊ	book
u	UW	u	boot
N/A	UX[4]	ʉ	dude
'''
vowels = [('AA', 'ɑ'),
          ('AE', 'æ'),
          ('AH', 'ʌ'),
          ('AO', 'ɔ'),
          ('AW', 'aʊ'),
          ('AX', 'ə'),
          ('AXR', 'ɚ'),
          ('AY', 'aɪ'),
          ('EH', 'ɛ'),
          ('ER', 'ɝ'),
          ('EY', 'eɪ'),
          ('IH', 'ɪ'),
          ('IX', 'ɨ'),
          ('IY', 'i'),
          ('OW', 'oʊ'),
          ('OY', 'ɔɪ'),
          ('UH', 'ʊ'),
          ('UW', 'u'),
          ('UX', 'ʉ')]

'''
Consonants[3]
ARPABET	IPA	Example
1-letter	2-letter
b	B	b	buy
C	CH	tʃ	China
d	D	d	die
D	DH	ð	thy
F	DX	ɾ	butter
L	EL	l̩	bottle
M	EM	m̩	rhythm
N	EN	n̩	button
f	F	f	fight
g	G	ɡ	guy
h	HH or H[4]	h	high
J	JH	dʒ	jive
k	K	k	kite
l	L	l	lie
m	M	m	my
n	N	n	nigh
G	NX or NG[4]	ŋ	sing
N/A	NX[4]	ɾ̃	winner
p	P	p	pie
Q	Q	ʔ	uh-oh
r	R	ɹ	rye   #应该为r
s	S	s	sigh
S	SH	ʃ	shy
t	T	t	tie
T	TH	θ	thigh
v	V	v	vie
w	W	w	wise
H	WH	ʍ	why
y	Y	j	yacht
z	Z	z	zoo
Z	ZH	ʒ	pleasure
'''
'''
在英语中，在一个单词的结尾音节中如果无发音的元音字母，或有元音字母也不发音而由l、m或n来充当元音字母，
那么该音节就叫做成音节（syllabic consonant）。在一些英文词典中，常在成音节中的/l/、/m/、/n/下方加上一点（.），写成/l̩/、/n̩/、/m̩/，
用来表示成音节辅音。例如：noodle/'nu:dl̩/、traveler/ˈtrævl̩ɚ/。
'''
consonants = [('B', 'b'),
              ('CH', 'tʃ'),
              ('D', 'd'),
              ('DH', 'ð'),
              ('DX', 'ɾ'),
              ('F', 'f'),
              ('G', 'ɡ'),
              ('HH', 'h'),
              ('JH', 'dʒ'),
              ('K', 'k'),
              ('L', 'l'),
              ('M', 'm'),
              ('N', 'n'),
              ('NG', 'ŋ'),
              ('P', 'p'),
              ('Q', 'ʔ'),
              ('R', 'r'),
              ('S', 's'),
              ('SH', 'ʃ'),
              ('T', 't'),
              ('TH', 'θ'),
              ('V', 'v'),
              ('W', 'w'),
              ('WH', 'ʍ'),
              ('Y', 'j'),
              ('Z', 'z'),
              ('ZH', 'ʒ')]

'''
Stress and auxiliary symbols[3]
AB	Description
0	No stress
1	Primary stress
2	Secondary stress
3...	Tertiary and futher stress
-	Silence
 !	Non-speech segment
+	Morpheme boundary
/	Word boundary
#	Utterance boundary
 :	Tone group boundary
 :1 or .	Falling or declining juncture
 :2 or ?	Rising or internal juncture
 :3 or .	Fall-rise or non-term juncture
'''

no_stress_arpabet = 0
primary_stress_arpabet = 1
secondary_stress_arpabet = 2

# ˈ
primary_stress_ipa = ["'", "ˈ"]
secondary_stress_ipa = ['ˌ']

ipa_stop_libs = {',', '-'}

class Phoneme:
    def __init__(self, vlaue, is_vowels):
        self._value = vlaue
        self._is_vowels = is_vowels

    def get_value(self):
        return self._value

    def is_vowels(self):
        return self._is_vowels