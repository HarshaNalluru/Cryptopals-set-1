from binascii import b2a_hex, a2b_hex

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