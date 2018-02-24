from binascii import a2b_hex, b2a_hex

def XOR(stanza, key):
	l = len(stanza)
	l_key = len(key)
	# print l, l_key
	
	key = str(key*((l+1)/l_key))[0:l]
	l_key = len(key)
	# print key
	# print l, l_key

	xor_stanza_key = "%x" % ((int(b2a_hex(stanza),16))^(int(b2a_hex(key),16)))
	append_zeroes = 2*l-len(xor_stanza_key)
	xor_stanza_key = "0"*(append_zeroes) + xor_stanza_key

	return str(xor_stanza_key)

stanza = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"
output = XOR(stanza,key)
print output


desired_output = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
if output == desired_output:
	print("#Target accomplished")