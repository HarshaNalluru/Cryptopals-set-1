# length = len(stanza)
stanza = "asdfhjkl"
key = "abd"
l = len(stanza)
l_key = len(key)
# print l, l_key
times = (l+1)/l_key
print times
key2 = key[:]*times
l_key = len(key2)
# print key
# print l, l_key
print key2[0:l]

while len(key) != l:
	for i in range(len(key)):
		if len(key) == l:
			break
		key = key + key[i]
print key