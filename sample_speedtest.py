import sys
sys.dont_write_bytecode=True

from word_search import search, goodsearch

#A sample speed test. For 1,000 random 4-character strings,
#print the valid words and the total number of valid words.

#runtime ~ 2.1 seconds
def new_randsearch():

	with open('randlist.txt','r') as g:
		count = 0
		for i in g:
			if goodsearch(i):
				count+=1
				print(i)
	print(count)

#runtime ~ 28.4 seconds
def classic_randsearch():
	with open('randlist.txt','r') as g:

		count = 0
		for i in g:



			if search(i,'wordlist.txt') == True:
				count+=1
				print(i)
	print(count)
