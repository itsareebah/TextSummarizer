import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
 
def read(file):
    with open(file, "r") as data:
        article = data.read()
    paragraphs = article.split("\n\n")  # Split text into paragraphs
    sentences = [sentence.strip() for paragraph in paragraphs for sentence in nltk.sent_tokenize(paragraph)]
    return sentences

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = set(stopwords.words('english'))

    vector1 = [w.lower() for w in sent1.split() if w.lower() not in stopwords]
    vector2 = [w.lower() for w in sent2.split() if w.lower() not in stopwords]

    all_words = list(set(vector1 + vector2))

    vector1 = [1 if w in vector1 else 0 for w in all_words]
    vector2 = [1 if w in vector2 else 0 for w in all_words]

    return 1 - cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: #ignore if both are same sentences
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix

def generate_summary(file_name, top_n=5):
    nltk.download("stopwords")
    stop_words = set(stopwords.words('english'))
    summarize_text = []

    sentences = read(file_name)
    sentence_similarity_matrix = build_similarity_matrix(sentences, stop_words)
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)[:top_n]

    for score, sentence in ranked_sentences:
        summarize_text.append(sentence)

    print("Summarized Text:\n", "\n".join(summarize_text))

generate_summary("test.txt", 5)
