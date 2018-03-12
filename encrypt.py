from Crypto.Cipher import AES
def encrypt(input_message):
	input_len = len(input_message)
	if input_len % 16 != 0:
		extra_append = 16 - (input_len % 16)
		for i in range (0,extra_append):
			input_message = input_message + '?' 
	obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
	ciphertext = obj.encrypt(input_message)
	return ciphertext



