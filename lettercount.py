from sys import argv

script, filename = argv

open_file= open(filename)

book=open_file.read()
num_letters=[0]*26
letters=range(97,123)

letter_dict=dict(zip(letters,num_letters))

for i in book:
	i=ord(i.lower())
	if i in range(97,123):
		letter_dict[i]=letter_dict[i]+1
	else:
		pass

for i in letter_dict.values():
	print i



	#if the character is equal to the key, value += 1


#s_dictionary={[ord(i),1]}
#for i in s:
#	if ord(i) in range (97, 123):
		#s_dictionary{ord(i)} = n

