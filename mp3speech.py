#Importing required libraries
import nltk
from newspaper import Article
from gtts import gTTS
import os
#Selecting the article
post = Article('https://www.codingninjas.com/studio/library/building-a-qr-code-generator-in-python')

#Downloading and parsing the article
post.download()
post.parse()


#Downloading punkt package
nltk.download('punkt')
post.nlp()

#Getting the text
txt = post.text


#Choosing language of speech
language = 'en' 
#English

#Storing text in a variable
#Slow = falsewill allow the audio at high speed
obj = gTTS(text=txt, lang=language, slow=False)