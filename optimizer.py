import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
class InputProcess:
    @staticmethod
    def get_wordnet_pos(word):
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}
        return tag_dict.get(tag, wordnet.NOUN)
    @staticmethod
    def optimizer(s):
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(w, InputProcess.get_wordnet_pos(w)) for w in nltk.word_tokenize(s)]
    @staticmethod
    def is_same(s1,s2):
        t= nltk.edit_distance(s1, s2)/(len(s1)+len(s2))
        if(t<0.15):
            return True
        else:
            return False