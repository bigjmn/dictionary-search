
def search(word,file):
	word = word.upper()
	word = word.rstrip()

	with open(file,'r') as f:
		for x in f:
			x = x.rstrip()

			if x == word:

				return True

	return False




def goodsearch(word):

	wordlet = word[0].upper()

	return search(word,'letter_dicts/'+wordlet+'words.txt')
