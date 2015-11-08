from sys import argv
# .strip()
file_content = open(argv[1], "r").read()

lines = file_content.split("\n")

dicti = {}

#token = {'ecrire': ecrire, }



def var(variable):
	import pdb; pdb.set_trace()
	#dicti.clear()
	#splitl = []

	token = variable.split("=")
	token = map(lambda x: x.strip(), token)
	
	# verifier quelle type d'operateur arithmetique
	print(token[1])
	if '+' in token[1]:
		# splitter le '+'
		token = variable.split('+')
		#token = map(lambda x: x.strip(), token)
		print (token)
	elif '-' in token[1]:
		print ('soustraction')
	elif '*' in token[1]:
		print ('mult')
	elif '/' in token[1]:
		print ('division')
	else:
		dicti[token[0]] = token[1]

	
	
	

def ecrire(display):
	if display[0] == '"':
		print(display.strip('"'))
#dic 
# dict = {}
# dict = ['ma_var']

for line in lines :
	line = line.strip()
	if line:
		token = line.split(" ", 1)
		#token[0] = dicti
		if token[0] == "ecrire":
			ecrire(token[1])
		elif token[0] == '#':
			pass
		elif token[0] == 'var':

			var(token[1])
		#	add()	
	else:
		continue
