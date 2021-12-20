# -*- coding: utf-8 -*-
import os
import re
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import numpy as np


def get_dict(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        text = re.sub(r'\W', ' ', str(text))
        text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
        text = re.sub(r'\^[a-zA-Z]\s+', ' ', text)
        text = re.sub(r'\s+', ' ', text, flags=re.I)
        text = re.sub(r'^b\s+', '', text)
        text = text.lower()
    return text


def save(kmeans):
    fw = open('k-means', 'wb')
    pickle.dump(kmeans, fw)
    fw.close()


def load():
    fr = open('k-means', 'rb')
    data = pickle.load(fr)
    fr.close()

    return data


def main():
    detective = []
    for i in os.listdir(r'D:\work_Denis\teach\detective'):
        detective.append(
            get_dict(r'D:\work_Denis\teach\detective\%s' % (i)).replace('\n', ''))
    fantastic = []
    for i in os.listdir(r'D:\work_Denis\teach\fantastic'):
        fantastic.append(
            get_dict(r'D:\work_Denis\teach\fantastic\%s' % (i)).replace('\n', ''))

    all_text = [str(i) for i in detective]
    [all_text.append(str(j)) for j in fantastic]
    tfidf_vectorizer = TfidfVectorizer(max_features=250)
    tfidf = tfidf_vectorizer.fit_transform(all_text)
    y = [0 for _ in range(20)]
    [y.append(1) for _ in range(20)]

    kmeans = KNeighborsClassifier(n_neighbors=2).fit(tfidf, y)

    return kmeans


save(main())


kmeans = load()
err = []
tfidf_vectorizer = TfidfVectorizer(max_features=250)
for i in os.listdir(r'D:\work_Denis\teach\valid'):
    valid = get_dict(r'D:\work_Denis\teach\valid\%s' % (i))
    tfidf_tf = tfidf_vectorizer.fit_transform([valid])
    if i.endswith('f.txt'):
        err.append([kmeans.predict(tfidf_tf)[0], 1])
    else:
        err.append([kmeans.predict(tfidf_tf)[0], 0])
err = np.array(err)
good = bad = 0
for i in err:
    print(i)
    if i[0] - i[1] == 0:
        good +=1
    else:
        bad += 1

print(good, bad)