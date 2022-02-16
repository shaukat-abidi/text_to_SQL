from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
#from jinja2 import Template

import numpy as np
import pickle
import psycopg2
import pycrfsuite

# Flask App
app = Flask(__name__)

# Global Variables
#global count_vect
#global tf_transformer
#global clf
#global tagger

categories = ['get_subjects', 'get_study']
sql_template = {'get_subjects': 'select subjectid from subject_listing where',
                'get_study': 'select studyid from study_listing where'}


def word2features(sent, i):
    word = sent[i][0]
    features = [
        'bias',
        'word.lower=' + word.lower(),
        'word[-3:]=' + word[-3:],
        'word[-2:]=' + word[-2:],
        'word.isupper=%s' % word.isupper(),
        'word.istitle=%s' % word.istitle(),
        'word.isdigit=%s' % word.isdigit(),
        ]
    if i > 0:
        word1 = sent[i-1][0]
        features.extend([
            '-1:word.lower=' + word1.lower(),
            '-1:word.istitle=%s' % word1.istitle(),
            '-1:word.isupper=%s' % word1.isupper(),
        ])
    else:
        features.append('BOS')
        
    if i < len(sent)-1:
        word1 = sent[i+1][0]
        features.extend([
            '+1:word.lower=' + word1.lower(),
            '+1:word.istitle=%s' % word1.istitle(),
            '+1:word.isupper=%s' % word1.isupper(),
        ])
    else:
        features.append('EOS')
                
    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [label for token, label in sent]

def sent2tokens(sent):
    return [token for token, label in sent]

@app.route("/")
def get_root():
    return render_template('swaggerui.html')

@app.route("/generateSQL", methods=['GET'])
def func_gensql():
    text = str(request.args.get('question'))
    docs_new = []
    docs_new.append(text)
    # Text classification 
    X_new_counts = count_vect.transform(docs_new)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)
    predicted = clf.predict(X_new_tfidf)
    sentence_category = categories[predicted[0]-1]
    print(docs_new, sentence_category)
    
    #NER Input and Output
    print(text.split())
    ner_input = [(tok, 'O') for tok in text.split()]
    print(ner_input)
    ner_output = tagger.tag(sent2features(ner_input))
    print(ner_output)
    
    #SQL Generator
    conditions = []
    for word, label in zip(ner_input, ner_output):
        if label != str("O"):
            conditions.append(str(label) + '=' + str('\'') + str(word[0]) + str('\''))
            
    final_sql_condition = " AND ".join(conditions)
    sql_query = str(sql_template[sentence_category]) + " " + final_sql_condition
    print(sql_query)
    
    # SQL Query
    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute(sql_query)

    # Retrieve query results
    records = cur.fetchall()

    # Close the connection
    conn.close()
    
    # Prepare the output
    output_str = ''
    tot_records = len(records)
    for _ind, _tuple in enumerate(records):
        print(_ind, _tuple)
        if _ind < tot_records - 1:
            output_str = output_str + str(_tuple[0]) + ','
        else:
            output_str = output_str + str(_tuple[0])
        

    #print(docs_new)
    #raw_sql = 'select * from all_tables'
    resp = {'question': text, "sentence_category": sentence_category, 'translated_sql': sql_query, 'output_text': str(output_str)}
    return jsonify(resp)

if __name__== '__main__':
    # Load Pickle objects
    # Text Classification
    global count_vect
    count_vect = CountVectorizer()
    
    global tf_transformer
    tf_transformer = TfidfTransformer(use_idf=False)
    
    global clf 
    clf = MultinomialNB()
    
    open_file = open("ml_models\\text_classification\\classification.pkl", "rb")
    count_vect, tfidf_transformer, clf = pickle.load(open_file)
    open_file.close()
    
    # NER
    global tagger 
    tagger = pycrfsuite.Tagger()
    tagger.open('ml_models\\ner\\test.crfsuite')

    # App running
    app.run(host='127.0.0.1', port=5000)
