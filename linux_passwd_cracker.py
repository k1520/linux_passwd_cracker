#!/usr/bin/python2

from crypt import *
from time import sleep
from sys import argv

#Opening shadow_file to get values for variable todo manipulation

file=open(argv[1],"r")
for word in file.readlines():
	x=word
#print x
y=x.split(":")
#print y
z=y[1].split("$")
#print z
salt="$"+str(z[1])+"$"+str(z[2])
#print salt
encrypted_hash=str(z[3])
#print encrypted_hash
overall_hash=salt+"$"+encrypted_hash
#print overall_hash

print "[*]Cracking Password Of "+str(y[0])
sleep(2)

#Opening Dictionary to Compute Hash For Each and Every Password and check with encrypted hash to find passwd
dictionary=open("top1000","r")
passwd=False
for line in dictionary.readlines():
	word=line.strip('\n')
	hash=crypt(word,salt)
	print "/\\/\\/\\/\\",
	if hash==overall_hash:
		passwd=word
if passwd!=False:
	print "\n\n[+]Password Found=",passwd	
else:
	print "\n[-]Password NOT Found Try Another Dictionary"