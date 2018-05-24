import spacy
nlp = spacy.load('en')                       # load model with shortcut link "en"
#nlp = spacy.load('en_core_web_sm')           # load model package "en_core_web_sm"

doc = nlp(u'This is a sentence.')
print([(w.text, w.pos_) for w in doc])