# importing all the required modules
import pdftotext
import nltk
import pandas as pd
from stop_words import get_stop_words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def run():
    FILE_PATH = 'demo/Debt The First 5,000 Years by David Graeber.pdf'
    dictionary = 250
    # creating an object 
    with open(FILE_PATH, mode='rb') as f:
        pdf = pdftotext.PDF(f)
        # How many pages?
        print(len(pdf))

        #nltk.download('stopwords')
        #nltk.download('punkt')
        #initialize the stop words
        stop_words = list(get_stop_words('en'))         #Have around 900 stopwords
        nltk_words = list(stopwords.words('english'))   #Have around 150 stopwords
        stop_words.extend(nltk_words)

        invalid_tokens = ['“','”',',','.','?','’','(',')',':',';','1','2','3','4','5','6','7','8','9','0','‘']
        
        pronouns = ['i','you','she','he','they','we','it','us','my','them']

        simplewords = ['one','two','three','four','five','six','seven','eight','nine','the','in','to','on','even','but','if','back','first','second','third','for','what','also',
        'put','form','men','new','else','actually','almost','really','often', 'almost', 'used', 'great', 'at','later','there','by',
        'much','way','a','true','and','say','might','case','thing','or','so','next','when','many','since','lot','start','mean','feel','well','far','from','get','come','set'
        'put','this','also','made','make','go','much','like','exchange','time','things','world','must','use','last','as','…','_____','pp','long','ever','never','sort','example','value',
        'why','away','end','another','people','take','comes','part','every','work','less','went','problem','fact', 'see', 'something', 'man','pay','became', 'social', 'become', 'took', 'hand'
        ]

        filtered_sentence = []

        for i in range(len(pdf)):
            word_tokens = word_tokenize(pdf[i])
            for w in word_tokens:
                if w not in stop_words and w not in invalid_tokens and w.lower() not in pronouns and w.lower() not in simplewords:
                    filtered_sentence.append(w)

        df_text = pd.Series(filtered_sentence)

        main_words = df_text.value_counts()[:dictionary].index.tolist()

        print(main_words)


        
        #print(word_tokens)
        #print(filtered_sentence)


        # Iterate over all the pages
        #for page in pdf:
         #   print(page)
 

 
            
    
if __name__ == '__main__':
    run()