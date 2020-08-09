# sentence tokenizer uses full stop to break the text into
#into different sentences

#importing sentence-tokenizer  from nltk
from nltk.tokenize import sent_tokenize

#Example text 
para = "Hii there this is my first code in Text-processing, feeling good . what about you, Hello boy"

#giving the example text to sentence tokenizer for tokenization 
print(sent_tokenize(para))


# The more efficient method to do this as below
import nltk.data
tokenizer = nltk.data