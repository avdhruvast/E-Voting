from Crypto.Cipher import AES
def encrypt(input_message , user_id):
	input_message = input_message + user_id 
	input_len = len(input_message)
	if input_len % 16 != 0:
		extra_append = 16 - (input_len % 16)
		for i in range (0,extra_append):
			input_message = input_message + '?' 
	extra_append = 16 - len(user_id)
	for i in range (0,extra_append):
		user_id = user_id + '?'
	obj = AES.new( user_id , AES.MODE_CBC, user_id)
	ciphertext = obj.encrypt(input_message)
	return ciphertext




