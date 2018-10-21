"""
create plot points and silly stories
"""

import markovify
import random
from os import listdir
from os.path import isfile, join


books = 'books/'
onlyfiles = [f for f in listdir(books) if isfile(join(books, f))]
some_book = random.choice(onlyfiles)
# Get raw text as string.
with open('books/'+some_book) as f:
        text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())
