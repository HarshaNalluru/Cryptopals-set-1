from Crypto.Cipher import AES
from binascii import a2b_base64

def Decrypt(text, key):
	_mode = AES.MODE_ECB
	cipher = AES.new(key, _mode)
	return cipher.decrypt(text)

key = 'YELLOW SUBMARINE'
text = ''
for line in open('7.txt'):
	text = text + a2b_base64(line[:-1])

print Decrypt(text, key)