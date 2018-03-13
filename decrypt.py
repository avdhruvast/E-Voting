from Crypto.Cipher import AES
def decrypt(ciphertext , user_id):
	extra_append = 16 - len(user_id)
	for i in range (0,extra_append):
		user_id = user_id + '?' 
	obj = AES.new( user_id , AES.MODE_CBC, user_id )
	output_message = obj.decrypt(ciphertext)
	output_message = output_message.replace('?','')
	return output_message
