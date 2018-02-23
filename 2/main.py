from binascii import a2b_hex, b2a_base64

# 1c0111001f010100061a024b53535009181c
# 686974207468652062756c6c277320657965
a = int('1c0111001f010100061a024b53535009181c',16)
b = int('686974207468652062756c6c277320657965',16)

XOR = str(hex(a^b))[2:-1]
print "Output XOR :", XOR



desired_XOR = '746865206b696420646f6e277420706c6179'
if XOR == desired_XOR:
	print("#Target accomplished")