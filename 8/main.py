from binascii import a2b_hex

def is_ECB_encoded(text):
	flag = 0
	text = a2b_hex(text)
	b_count = len(text)/16
	for i in range(b_count):
		for j in range(i+1,b_count):
			if text[i*16:(i+1)*16] == text[j*16:(j+1)*16]:
				print(i,j)
				flag = 1
	if flag == 1:
		return 1
	else:	
		return 0

k = 0
for line in open('8.txt'):
	k += 1 
	line = line[:-1]
	if is_ECB_encoded(line):
		print k
		print line