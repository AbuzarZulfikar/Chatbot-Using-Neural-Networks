import streamlit as st
import numpy as np
import json
import random
import nltk
import pickle
from nltk.stem.lancaster import LancasterStemmer
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense

# Download NLTK resources
nltk.download('punkt')

# Load intents data
with open('./data/corpus.json') as json_data:
    intents = json.load(json_data)

# Initialize stemmer
stemmer = LancasterStemmer()

# Load model and training data
# Assuming you have saved 'model.h5' and 'training_data.pkl' files

# Load model
model = tf.keras.models.load_model('model.h5')

# Load training data
with open('training_data.pkl', 'rb') as f:
    data = pickle.load(f)
    words = data['words']
    classes = data['classes']

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    bag = [0]*len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

def classify(sentence):
    results = model.predict(np.array([bow(sentence, words)]))[0]
    results = [[i,r] for i,r in enumerate(results) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    return return_list

ERROR_THRESHOLD = 0.25

st.title("Chatbot")

user_input = st.text_input("You- ")

if user_input:
    results = classify(user_input)
    if results:
        for i in intents['intents']:
            if i['tag'] == results[0][0]:
                response = random.choice(i['responses'])
                st.text("Bot- " + response)
