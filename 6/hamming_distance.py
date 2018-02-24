from binascii import b2a_hex

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