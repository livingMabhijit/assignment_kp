"""
This program is intended to find text similarity and match between 
an input word and the historical correct word of the company name. 
Here I have used python package 'fuzzywuzzy' due to time constraints 
and lack of time to explore more possiblities to find a better approach 
to the solution. This package uses Levenshtein distance to find the similar
word with sequesnce of letter/token and ratio of word being used in both words
for string matching and similarity ratio.
"""

import pandas as pd
from fuzzywuzzy import process
import string

#reading DataFrame
df = pd.read_csv('train_dataset.csv')
#print(df.head(20))

#simple text preprocessing
def clean_data(txt):
	txt = txt.lower()
	txt =txt.strip()
	txt = txt.translate(str.maketrans('', '', string.punctuation))
	return txt

"""This function takes input from user and provides the most expected word
that matches the user's given word from the historical company names in data."""

def best_match():
	try:
		print('Enter input word')
		input_word = input()
		input_word = clean_data(input_word)
		print('Enter the number of matches looking for e.g 2,3')
		limits= int(input())
		options = df['Company names'].unique()# to find the company names to compare with
		match = process.extract(input_word,options,limit = limits) 
		print('Probable best matches '+str(match)+' with score')
	except:
		print('someting went worng')
	
if __name__ == '__main__':
	best_match()