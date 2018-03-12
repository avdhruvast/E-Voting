from Crypto.Cipher import AES
def decrypt(ciphertext):
	
	obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
	output_message = obj.decrypt(ciphertext)
	output_message = output_message.replace('?','')
	return output_message
