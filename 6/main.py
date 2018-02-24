from binascii import a2b_hex, b2a_hex, a2b_base64

##########################################################################################

def hamming_distance(string, string2):
  X = int(b2a_hex(string),16) ^ int(b2a_hex(string2),16)
  X = bin(X)[2:]
  # print X
  count = 0
  for x in X:
    if x=='1':
      count += 1
  return count

def normalized_distance (string, length): 
  ham_sum = 0
  for i in range(len(string)/length - 1):
    ham_sum += hamming_distance(string[(i+0)*length:(i+1)*length], string[(i+1)*length:(i+2)*length])
  return ((1.0 * ham_sum) / (len(string)/length - 1))/length

# print hamming_distance("this is a test","wokka wokka!!!")
# print normalized_distance("this is a testwokka wokka!!!",14)

##########################################################################################

# http://codegist.net/search/print-meaning-in-english/11
frequencies = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610, 'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513, 'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182 
}

def Decode(string, x = 0):
    def Score(string):
        score = 0
        for i in string.lower():
            if i in frequencies:
                score += frequencies[i]
        return score
    
    string = b2a_hex(string)
    l = len(string)
    string_hex = int(string,16)
    max_score = 0
    max_score_str = ""
    max_score_i = 0
    for i in range(256):
        #char_solo = int(("%02x" % i) * 2,16)
        char_string_hex = int(("%02x" % i) * l,16)
        #print "b:",b,("%02x" % i) * l
        
        c = "%X" % (string_hex^char_string_hex)
        #print "c:",c
        
        if len(c) % 2 == 1:
            c = "0%s" % c
        c = a2b_hex(c)[x:]  # first x chars -> garbage
        #print "c:",c
        
        if Score(c) > max_score:
          max_score = Score(c)
          max_score_str = c
          max_score_chr_i = chr(i)
          # cur_key = b_solo
    return max_score_chr_i, max_score_str

##########################################################################################

def XOR(stanza, key): 
  l = len(stanza)
  while len(key) != l:
    for i in range(len(key)):
      if len(key) == l:
        break
      key = key + key[i]

  xor_stanza_key = "%x" % ((int(b2a_hex(stanza),16))^(int(b2a_hex(key[0:l]),16)))
  append_zeroes = 2*l-len(xor_stanza_key)
  xor_stanza_key = "0"*(append_zeroes) + xor_stanza_key
  
  return a2b_hex(xor_stanza_key)

##########################################################################################



data = ""
for line in open('6.txt'):
  data += line.strip()
data = a2b_base64(data)

min_hamming_dist = 1.0 * (10*1000) 
for KEYSIZE in range(2,40):
  h = normalized_distance(data,KEYSIZE)
  if h < min_hamming_dist:
    min_hamming_dist = h
    min_keysize = KEYSIZE

KEYSIZE = min_keysize

print "KEYSIZE = " + str(KEYSIZE)


split_data = [data[i::KEYSIZE] for i in range(KEYSIZE)]

key = ''
for i in range(len(split_data)):
  temp = Decode(split_data[i], min(len(split_data[i]),200))
  key = key + temp[0]

Decoded_data = XOR(data, key)

# print decoded_data
print "Key =", key
print Decoded_data
