# -*- coding: utf-8 -*-
from arpabetandipaconvertor.model.phoneme import Phoneme

'''
参考
https://en.wikipedia.org/wiki/ARPABET
'''

'''
ARPABET	IPA	Example(s)
1-letter2-letter   修正 （美| 英）    音标                          ARPAbet
a	AA	    ɑ	balm,       AA   ɑ | ɒ ɑ:   英 [bɑ:m]     美 [bɑm]        B AA1 M
                bot                         英 [bɒt]      美 [bɑt]        B AA1 T
@	AE	    æ	bat         AE   æ          英 [bæt]      美 [bæt]        B AE1 T
A	AH	    ʌ	butt        AH   ʌ          英 [bʌt]      美 [bʌt]        B AH1 T
c	AO	    ɔ	bought      AO   ɔ | ɔ:     英 [bɔ:t]     美 [bɔt]        B AO1 T
W	AW	    aʊ	bout        AW   aʊ         英 [baʊt]     美 [baʊt]       B AW1 T
x	AX	    ə	about       AX   ə          英 [əˈbaʊt]   美 [əˈbaʊt]     AH0 B AW1 T
N/A	AXR[4]	ɚ   letter      ER   ɚ          英 [ˈletə(r)] 美 [ˈlɛtɚ]      L EH1 T ER0
Y	AY	    aɪ	bite        AY   aɪ         英 [baɪt]     美 [baɪt]       B AY1 T
E	EH	    ɛ	bet         EH   ɛ | e      英 [bet]      美 [bet]        B EH1 T
R	ER	    ɝ	bird        ER   ɜr | ɜ:    英 [bɜ:d]     美 [bɜrd]       B ER1 D
e	EY	    eɪ	bait        EY   eɪ         英 [beɪt]     美 [beɪt]       B EH1 T
I	IH	    ɪ	bit         IH   ɪ          英 [bɪt]      美 [bɪt         B IH1 T
X	IX	    ɨ	roses       IX   ɨ          英 ['rəʊzɪz]  美 ['roʊzɪz]    R OW1 Z
                rabbit                      英 [ˈræbɪt]   美 [ˈræbɪt]     R AE1 B AH0 T
i	IY	    i	beat        IY   i | i:     英 [bi:t]     美 [bit]        B IY1 T
o	OW	    oʊ	boat        OW   oʊ | əʊ    英 [bəʊt]     美 [boʊt]       B OW1 T
O	OY	    ɔɪ	boy         OY   ɔɪ         英 [bɔɪ]      美 [bɔɪ]        B OY1
U	UH	    ʊ	book        UH   ʊ          英 [bʊk]      美 [bʊk]        B UH1 K
u	UW	    u	boot        UW   u | u:     英 [bu:t]     美 [but]        B UW1 T
N/A	UX[4]	ʉ	dude        UW   ʉ          英 [du:d]     美 [dud, djud]  D UW1 D
'''
vowels = [Phoneme(arpabet='AA', american='ɑ',  english='ɑ:', ipa='ɑ',  is_vowel=True),
          Phoneme(arpabet='AE', american='æ',  english='æ',  ipa='æ',  is_vowel=True),
          Phoneme(arpabet='AH', american='ʌ',  english='ʌ',  ipa='ʌ',  is_vowel=True),
          Phoneme(arpabet='AO', american='ɔ',  english='ɔ:', ipa='ɔ',  is_vowel=True),
          Phoneme(arpabet='AW', american='aʊ', english='aʊ', ipa='aʊ', is_vowel=True),
          Phoneme(arpabet='AX', american='ə',  english='ə',  ipa='ə',  is_vowel=True),
          Phoneme(arpabet='ER', american='ɚ',  english='ər', ipa='ər', is_vowel=True),
          Phoneme(arpabet='AY', american='aɪ', english='aɪ', ipa='aɪ', is_vowel=True),
          Phoneme(arpabet='EH', american='ɛ',  english='e',  ipa='e',  is_vowel=True),
          Phoneme(arpabet='ER', american='ɝ',  english='ɜ:', ipa='ɜr', is_vowel=True),
          Phoneme(arpabet='EY', american='e',  english='eɪ', ipa='eɪ', is_vowel=True),
          Phoneme(arpabet='IH', american='ɪ',  english='ɪ',  ipa='ɪ',  is_vowel=True),
          Phoneme(arpabet='IX', american='ɨ',  english='ɨ',  ipa='ɨ',  is_vowel=True),
          Phoneme(arpabet='IY', american='i',  english='i:', ipa='i:', is_vowel=True),
          Phoneme(arpabet='OW', american='o',  english='əʊ', ipa='oʊ', is_vowel=True),
          Phoneme(arpabet='OY', american='ɔɪ', english='ɔɪ', ipa='ɔɪ', is_vowel=True),
          Phoneme(arpabet='UH', american='ʊ',  english='ʊ',  ipa='ʊ',  is_vowel=True),
          Phoneme(arpabet='UW', american='u',  english='u:', ipa='u',  is_vowel=True),
          Phoneme(arpabet='UX', american='ʉ',  english='ʉ',  ipa='ʉ',  is_vowel=True)]

'''
Consonants[3]
ARPABET	        IPA	        Example
1-letter	    2-letter      修正
b	B	        b	    buy          B   b      英 [baɪ]         美 [baɪ]             B AY1
C	CH	        tʃ	    China        CH  tʃ     英 ['tʃaɪnə]     美 [ˈtʃaɪnə]         CH AY1 N AH0
d	D	        d	    die          D   d      英 [daɪ]         美 [daɪ]             D AY1
D	DH	        ð	    thy          DH  ð      英 [ðaɪ]         美 [ðaɪ]             DH AY1
F	DX	        ɾ	    butter       T   t | ɾ  英 [ˈbʌtə(r)]    美 [ˈbʌtɚ]           B AH1 T ER0
L	EL	        l̩	    bottle       L   l      英 [ˈbɒtl]       美 [ˈbɑtl]           B AA1 T AH0 L
M	EM	        m̩	    rhythm       M   m      英 [ˈrɪðəm]      美 [ˈrɪðəm]          R IH1 DH AH0 M
N	EN	        n̩	    button       N   n      英 [ˈbʌtn]       美 [ˈbʌtn]           B AH1 T AH0 N
f	F	        f	    fight        F   f      英 [faɪt]        美 [faɪt]            F AY1 T
g	G	        ɡ	    guy          G   g      英 [gaɪ]         美 [ɡaɪ]             G AY1
h	HH or H[4]	h	    high         HH  h      英 [haɪ]         美 [haɪ]             HH AY1
J	JH	        dʒ	    jive         JH  dʒ     英 [dʒaɪv]       美 [dʒaɪv]           JH AY1 V
k	K	        k	    kite         K   k      英 [kaɪt]        美 [kaɪt]            K AY1 T
l	L	        l	    lie          L   l      英 [laɪ]         美 [lai]             L AY1
m	M	        m	    my           M   m      英 [maɪ]         美 [maɪ]             M AY1
n	N	        n	    nigh         N   n      英 [naɪ]         美 [naɪ]             N AY1
G	NX or NG[4]	ŋ	    sing         NG  ŋ      英 [sɪŋ]         美 [sɪŋ]             S IH1 NG
N/A	NX[4]	    ɾ̃	    winner                  英 [ˈwɪnə(r)]    美 [ˈwɪnɚ]           W IH1 N ER0
p	P	        p	    pie          P   p      英 [paɪ]         美 [paɪ]             P AY1      
Q	Q	        ʔ	    uh-oh        Q   ʔ      英 [ˈʌˈəu]       美 [ˈʌˌo]
r	R	        ɹ	    rye          R   r or ɹ 英 [raɪ]         美 [raɪ]             R AY1
s	S       	s	    sigh         S   s      英 [saɪ]         美 [saɪ]             S AY1
S	SH	        ʃ   	shy          SH  ʃ      英 [ʃaɪ]         美 [ʃaɪ]             SH AY1
t	T	        t	    tie          T   t      英 [taɪ]         美 [taɪ]             T AY1
T	TH	        θ	    thigh        TH  θ      英 [θaɪ]         美 [θaɪ]             TH AY1
v	V	        v      	vie          V   v      英 [vaɪ]         美 [vaɪ]             V AY1
w	W	        w	    wise         W   w      英 [waɪz]        美 [waɪz]            W AY1 Z
H	WH	        ʍ	    why          WH  ʍ      英 [waɪ]         美 [hwaɪ, waɪ]       HH W AY1, W AY1
y	Y	        j	    yachting     Y   j      英 [ˈjɒtɪŋ]      美 [ˈjɑtɪŋ]          Y AA1 T IH0 NG
z	Z	        z	    zoo          Z   z      英 [zu:]         美 [zu]              Z UW1  
Z	ZH	        ʒ	    pleasure     ZH  ʒ      英 [ˈpleʒə(r)]   美 [ˈplɛʒɚ]          P L EH1 ZH ER0
'''
'''
在英语中，在一个单词的结尾音节中如果无发音的元音字母，或有元音字母也不发音而由l、m或n来充当元音字母，
那么该音节就叫做成音节（syllabic consonant）。在一些英文词典中，常在成音节中的/l/、/m/、/n/下方加上一点（.），写成/l̩/、/n̩/、/m̩/，
用来表示成音节辅音。例如：noodle/'nu:dl̩/、traveler/ˈtrævl̩ɚ/。
'''
consonants = [Phoneme(arpabet='B',  american='b',  english='b',  ipa='b',  is_vowel=False),
              Phoneme(arpabet='CH', american='tʃ', english='tʃ', ipa='tʃ', is_vowel=False),
              Phoneme(arpabet='D',  american='d',  english='d',  ipa='d',  is_vowel=False),
              Phoneme(arpabet='DH', american='ð',  english='ð',  ipa='ð',  is_vowel=False),
              Phoneme(arpabet='DX', american='ɾ',  english='ɾ',  ipa='ɾ',  is_vowel=False),
              Phoneme(arpabet='F',  american='f',  english='f',  ipa='f',  is_vowel=False),
              Phoneme(arpabet='G',  american='g',  english='g',  ipa='ɡ',  is_vowel=False),
              Phoneme(arpabet='HH', american='h',  english='h',  ipa='h',  is_vowel=False),
              Phoneme(arpabet='JH', american='dʒ', english='dʒ', ipa='dʒ', is_vowel=False),
              Phoneme(arpabet='K',  american='k',  english='k',  ipa='k',  is_vowel=False),
              Phoneme(arpabet='L',  american='l',  english='l',  ipa='l',  is_vowel=False),
              Phoneme(arpabet='M',  american='m',  english='m',  ipa='m',  is_vowel=False),
              Phoneme(arpabet='N',  american='n',  english='n',  ipa='n',  is_vowel=False),
              Phoneme(arpabet='NG', american='ŋ',  english='ŋ',  ipa='ŋ',  is_vowel=False),
              Phoneme(arpabet='P',  american='p',  english='p',  ipa='p',  is_vowel=False),
              Phoneme(arpabet='Q',  american='ʔ',  english='ʔ',  ipa='ʔ',  is_vowel=False),
              Phoneme(arpabet='R',  american='r',  english='r',  ipa='ɹ',  is_vowel=False),
              Phoneme(arpabet='S',  american='s',  english='s',  ipa='s',  is_vowel=False),
              Phoneme(arpabet='SH', american='ʃ',  english='ʃ',  ipa='ʃ',  is_vowel=False),
              Phoneme(arpabet='T',  american='t',  english='t',  ipa='t',  is_vowel=False),
              Phoneme(arpabet='TH', american='θ',  english='θ',  ipa='θ',  is_vowel=False),
              Phoneme(arpabet='V',  american='v',  english='v',  ipa='v',  is_vowel=False),
              Phoneme(arpabet='W',  american='w',  english='w',  ipa='w',  is_vowel=False),
              Phoneme(arpabet='WH', american='ʍ',  english='ʍ',  ipa='ʍ',  is_vowel=False),
              Phoneme(arpabet='Y',  american='j',  english='j',  ipa='j',  is_vowel=False),
              Phoneme(arpabet='Z',  american='z',  english='z',  ipa='z',  is_vowel=False),
              Phoneme(arpabet='ZH', american='ʒ',  english='ʒ',  ipa='ʒ',  is_vowel=False)]

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

# ˈ
primary_stress_ipa = ["'", "ˈ"]
secondary_stress_ipa = ['ˌ']

ipa_stop_libs = {',', '-'}

skip_libs = [('(', ')'), ('（', '）')]

