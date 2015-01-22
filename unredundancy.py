import nltk,random
from nltk.corpus import PlaintextCorpusReader, nps_chat
corpus_root = '/Users/kevinzeidler/Documents/corpora/'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()

your_text = wordlists.words('YourTextFileHere.txt') #must be in same dir
#ij = wordlists.words('InfiniteJest.txt')



class Server():
	"A variation on The Unredundancy Exercise: takes a book, concatenates fixednum last words of each sentence"
	def __init__( self, contents ):
		#self.length = length
		self.contents = contents
		


	def is_valid_chunk( self, chunk ):
		for i in chunk[0:len(chunk)-1]:
			if len(i) < 2:
				return False
		return True
			

	def request( self, sents_to_fetch, words_to_fetch ):
		sentences_so_far = 0
		words_so_far = random.randint(1,len(self.contents))
		page = []
		this_word = ''
		result = ''
		this_sentence = []
		first_word = True

		while sentences_so_far < sents_to_fetch:
			this_word = ij[words_so_far]
			
			this_sentence.append(this_word)

			
			words_so_far += 1

			if this_word == '.' and self.is_valid_chunk(this_sentence[-int(words_to_fetch + 1):]):
				result +=' '.join(this_sentence[-int(words_to_fetch + 1):-1]).capitalize() + '. '
				
				sentences_so_far += 1
				first_word = True
				
				#page.append(this_sentence[-4:])
				
					
		return result

		

# Example output:
# InfiniteJest = Server(ij)

# print InfiniteJest.request(1,5).title()
# poemtext = InfiniteJest.request(10,3)
# print poemtext
# >> Hands Were Disfigured Or Something. 
# Out of control. Were in person. Of the market. Them without makeup. On the phone. End videophone tableaux. Broadcast television advertising. In consumer technology. For precipitant investors. Have to exert. 
# [Finished in 3.8s]


