from cltk.corpus.utils.importer import CorpusImporter
from cltk.tokenize.indian_tokenizer import *
from cltk.stem.sanskrit.indian_syllabifier import Syllabifier
import os

#Sanskrit corpous imported
c = CorpusImporter('sanskrit')
#c.list_corpora

#imported sanskrit_text_wikipedia
c.import_corpus('sanskrit_text_wikipedia')

#change current working directory to corpus data
os.chdir('/home/vabs/cltk_data/sanskrit/text/sanskrit_text_wikipedia/wiki_documents/ayurveds')

#total no of tokens
tokens = []

#total no of tokens
words = []

#total no of words per sentence. It is a list of numbers each representing
#no of words in that sentence
words_per_sen=[] 

#characters per word
chars_per_word=[]


with open('ashta.txt') as data:
	for each_line in data.readlines():
		words = indian_punctuation_tokenize_regex(each_line)
		tokens += words
		words_per_sen.append(len(words))


#unique tokens
uni_tokens = []

for each_token in tokens:
	chars_per_word.append(len(each_token))
	if each_token in uni_tokens:
		continue
	else:
		uni_tokens.append(each_token)

print(len(tokens))
print(len(uni_tokens))
print(words_per_sen)
print(chars_per_word)
