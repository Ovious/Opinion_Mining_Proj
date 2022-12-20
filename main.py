#librarys
import csv
import re
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string

# reading files to arrays


#Companies = ["Deloitte","Ey","Pwc","Accenture","Kpmg-0828bc85"]
#for company in Companies:
Deloitte = []
PwC = []
KPMG = []
Accenture = []
EY = []
Companies = ["Deloitte","Ey","Pwc","Accenture","Kpmg-0828bc85"]
i = 0
for company in Companies:
  with open(company+'.csv', 'r',encoding='utf-8') as f:
    reader = csv.reader(f,delimiter= '|')
    for row in reader:
      if not row:
        continue
      if company == 'Deloitte':
        Deloitte.append(row)
      elif company == 'Ey':
        EY.append(row)
      elif company == 'Pwc':
        PwC.append(row)
      elif company == 'KPMG':
        KPMG.append(row)
      else:
        Accenture.append(row)

# tabela [review1, review2, ..., review731]
compRevs = ["Jakis tam 555 teks?&%"]


stopwords = stopwords.words('english')


def preprocessing(compRevs):
    for review in compRevs:

        # Removing punctuation marks
        translator = str.maketrans('', '', string.punctuation)
        review = review.translate(translator)

        # Reemoving numbers
        pattern = r'\d+'
        review = re.sub(pattern, '', review)

        # Removing Stopwords
        newreview = ''
        wordsInReview = review.split()
        for word in wordsInReview:
            if word not in stopwords:
                newreview += word + ' '
        review = newreview

        # Lowercasing
        review.lower()

        # Stemming&stripping whiespaces
        stemmer = PorterStemmer()
        review_words = review.split()
        stemmed_words = []
        for word in review_words:
            stemmed_words.append(stemmer.stem(word))
        review = ' '.join(stemmed_words)

for i in range(len(EY)):
    print(EY[i][0])



