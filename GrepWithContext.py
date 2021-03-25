def grep(word,context_requested):
	words=['Rileyis','Is','a','b','c','d','Glad','It','Is','the']
	pointer=-1
	for idx, item in enumerate(words):
		if context_requested < 0:
			print('error')
		elif item == word and idx > pointer:
			for i in range(context_requested,0,-1):
				if idx-i >= 0 and idx-i>pointer:
					print(words[idx-i])
			print(item)
			for j in range(1, context_requested+1):
				if idx+j <= len(words)-1:
					pointer = idx+j
					print(words[idx+j])

grep('Is',1)
print("=========================")
grep('Is',3)




