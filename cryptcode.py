#small encrypter
import hashlib

fo = open("hsw.js","rb")#rb reads binary

file_name = input('File Name:')#input a file name so the program know what to encrypt
image = fo.read()
image = bytearray(image)
key = 48 # Valuws accepted bw 0 - 255
for index, value in enumerate(image): 
	image[index] = value ^ key # ^ is a XOR operator
fo = open("encrypted_subject.png","wb")
fo.write(image)
fo.close()
#the things up above are not needed for a encrypter, check out my multi encrypyer on my profile @Noburu-OS


#######starting a small simple hashlib encrypter######
wrd_enc = file_name.encode('utf-8')
digested = hashlib.md5(wrd_enc.strip()).hexdigest()
print('encryption started{}...')
print('file encrypted:' + (digested))
