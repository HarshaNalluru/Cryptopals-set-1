from binascii import a2b_hex

# From http://www.data-compression.com/english.html
frequencies = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610, 'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513, 'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182 
}

def Decode(string):
    def Score(string):
        score = 0
        for i in string.lower():
            if i in frequencies:
                score += frequencies[i]
        return score

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
        c = a2b_hex(c)[34:]  # first 34 chars -> garbage
        #print "c:",c
        
        if Score(c) > max_score:
          max_score = Score(c)
          max_score_str = c
          max_score_i = i
          # cur_key = b_solo
    return max_score_str, "key:", max_score_i

encodedS = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
decodedS = Decode(encodedS)
print decodedS[0]