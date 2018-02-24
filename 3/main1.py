
from curses.ascii import isprint
from binascii import a2b_hex

def score(string):
  freq = dict()
  freq['a']=834
  freq['b']=154
  freq['c']=273
  freq['d']=414
  freq['e']=1260
  freq['f']=203
  freq['g']=192
  freq['h']=611
  freq['i']=671
  freq['j']=23
  freq['k']=87
  freq['l']=424
  freq['m']=253
  freq['n']=680
  freq['o']=770
  freq['p']=166
  freq['q']=9
  freq['r']=568
  freq['s']=611
  freq['t']=937
  freq['u']=285
  freq['v']=106
  freq['w']=234
  freq['x']=20
  freq['y']=204
  freq['z']=6
  freq[' ']=2320

  ret = 0

  for c in string.lower():
    if c in freq:
      ret += freq[c]

  return ret

def decoder(string):
  cur_best = 0
  cur_best_str = ""
  cur_key = ""
  l = len(string)
  a = int(string,16)
  print "a:",a
  for i in range(256):
    b_solo = int(("%02x" % i) * 2,16)
    b = int(("%02x" % i) * l,16)
    print "b:",b,("%02x" % i) * l
    c = "%X" % (a^b)
    print "c:",c
    if len(c) % 2 == 1:
      c = "0%s" % c
    c = a2b_hex(c)[34:]  # [34:] since we notice that first chars are waste
    print "c:",c
    c = filter(isprint,c)
    print "c:",c
    if score(c) > cur_best:
      cur_best = score(c)
      cur_best_str = c
      cur_key = b_solo
  return cur_best_str,b_solo

print decoder("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")