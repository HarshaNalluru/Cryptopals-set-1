from binascii import a2b_hex, b2a_base64

String = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

string_in_alphabets = a2b_hex(String)
string_in_base64 = b2a_base64(string_in_alphabets).strip()
print '#string_in_base64 : ', string_in_base64




desired_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
print '#desired_string   : ', desired_string
if desired_string == string_in_base64:
	print("#Target accomplished")