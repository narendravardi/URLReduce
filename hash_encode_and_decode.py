UNRESTRICTED_CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
BASE = len(UNRESTRICTED_CHARACTERS)

def encode(auto_increment_value):
	global UNRESTRICTED_CHARACTERS,BASE
	encoded_string = ''
	while auto_increment_value>0:
		encoded_string += UNRESTRICTED_CHARACTERS[auto_increment_value % BASE]
		auto_increment_value /= BASE
	return encoded_string[::-1]

def decode(encoded_string):
	global UNRESTRICTED_CHARACTERS,BASE
	auto_increment_value = 0
	for single_char in encoded_string:
		auto_increment_value = auto_increment_value * BASE + UNRESTRICTED_CHARACTERS.index(single_char)
	return auto_increment_value
