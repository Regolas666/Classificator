import os
import re
import sys
from xml.dom.minidom import parse


import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.layers import Dense, Embedding, Conv1D, GlobalMaxPooling1D, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import pickle


class MainClassify:

   # def strings(string):
   #     string = re.sub(r'[^\w\s]+|[\d]+|км/ч|\b\w{0,2}\b', r' ', string)
   #     string = re.sub(r'\b\w{0,2}\b', r'', string)
   #     string = re.sub(r'\b\s+\b', r' ', string.strip())
   #     return string.lower()

    def choose_class(string):
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
        os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

        text_list = []
        class_list = []
        num_words = 2600  # максимальное число слов, которое будем использовать
        max_news_len = 100  # максимальная длина новости

        with open('main_Class/tokenizer_ver1.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)

        model = Sequential()
        model.add(Embedding(num_words, 64, input_length=max_news_len))  # создание плотных векторов (64 числа на вектор)
        model.add(Conv1D(250, 5, padding='valid', activation='relu'))  # свёрточная часть (1 свёрточный слой)
        model.add(GlobalMaxPooling1D())  # выбор макс. значений из набора поступающих данных
        model.add(Dense(128, activation='relu'))  # полносвязная часть для классификации
        model.add(Dropout(0.2))
        model.add(Dense(1, activation='sigmoid'))  # выходной нейрон

        model.compile(optimizer='adam',  # оптимизатор
              loss='binary_crossentropy',  # функция ошибки (бинарная перекрёстная энтропия)
              metrics=['accuracy'])  # доля правильных ответов


        model_save_path = 'main_Class/best_model.h5'
        # Загружаем модель с лучшей долей правильных ответов на проверочном наборе данных
        model.load_weights(model_save_path)

        text_test_case = string
      #  text_test_case = strings(text_test_case)
        string = re.sub(r'[^\w\s]+|[\d]+|км/ч|\b\w{0,2}\b', r' ', string)
        string = re.sub(r'\b\w{0,2}\b', r'', string)
        string = re.sub(r'\b\s+\b', r' ', string.strip())
        string = string.lower()
        sequence = tokenizer.texts_to_sequences([text_test_case])
        data = pad_sequences(sequence, maxlen=max_news_len)
        result = model.predict(data)
        if result < 0.5:
            return("Новость относится к pc")
        else:
            return("Новость относится к кино")
