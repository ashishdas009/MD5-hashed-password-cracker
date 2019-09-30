import hashlib
import codecs

print ("\n")                                          
password = open('eharmony passwords.txt', 'r')
passread = open('wordlist.txt', 'r')             #reading the plaintext passwords from the dictionary rockyou.txt, which is publicly available
passout = open('eharmony_cracked.txt', 'r+')

hash_value = set()                               #loading the files for the program
for line in password:
  hash_value.add(line.replace("\n","")) 


for line in passread:                          #hash the dictionary and compare with the password set of eharmony
  unhashed = line.replace("\n","").upper()     #removing the newline character and converting the string from dictionary to upper case
  word = hashlib.md5(unhashed.encode('utf-8'))
  if word.hexdigest() in hash_value:
    passout.write(word.hexdigest()+ " " + unhashed + "\n")

print ("\n")
