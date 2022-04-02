import nltk 
from gensim.summarization import summarize
from nltk.text import word_tokenize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import re
import string
def summarize_lexRank(text):
    parser = PlaintextParser.from_string(text,Tokenizer('english'))
    lex_summarizer = LexRankSummarizer()
    summary =lex_summarizer(parser.document,3)
    summary_list =[str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result
def get_norm_sentense(text):
    words = word_tokenize(text)
    res = []
    for word in words:
        word = re.sub(f'{string.punctuation}')


def summarize_gensim(text):
    chunks = get_norm_sentense(text)
    return summarize(text)
    

def summarize_text(text):
    results = []

    

