import re
import nltk 
import spacy
from nltk.corpus import stopwords
from nltk import ngrams


text = 'A Sra. Rosa plantou uma rosa no jardim. O céu estava azul e a brisa era suave. Ela pensou: "Seria maravilhoso se todos os dias fossem assim, tão tranquilos quanto uma rosa em flor."'
tokens = re.findall(r'\w+', text.lower())
tokens_normalizados = [re.sub(r'é', 'e', token).lower() for token in tokens]
print(tokens_normalizados)

nltk.download('stopwords')

stop_words = set(stopwords.words('portuguese'))
filtered_tokens = [word for word in tokens_normalizados if word not in stop_words]
print(filtered_tokens)

unigramas = list(ngrams(filtered_tokens, 1))
bigrams = list(ngrams(filtered_tokens, 2))
trigrams = list(ngrams(filtered_tokens, 3))

print(unigramas)
print(bigrams)
print(trigrams)

#python -m spacy download pt_core_news_sm

nlp = spacy.load('pt_core_news_sm')
doc = nlp(" ".join(filtered_tokens))
lemmatized = [token.lemma_ for token in doc]
print(lemmatized)