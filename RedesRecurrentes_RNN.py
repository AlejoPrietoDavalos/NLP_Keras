import numpy as np
np.random.seed(5)
from keras.layers import Input, Dense, SimpleRNN
from keras.models import Model
from keras.optimizers import SGD
from keras.utils import to_categorical
from keras import backend as K
from copy import copy

def string_to_array(string, separadores):
    """ Convierte el string en una lista separada por cada elemento del separadores."""
    lista = []
    i=0
    for j, l in enumerate(string):
        if l in separadores:
            palabra = string[i:j]
            if palabra!="":
                lista.append(palabra)
            lista.append(l)
            i = j+1
    return lista

char_common = {
    '\n':False,
    ' ':False,
    '!':False,
    '"':False,
    '(':False,
    ')':False,
    ',':False,
    '-':False,
    '.':False,
    '0':False,
    '1':False,
    '2':False,
    '3':False,
    '4':False,
    '5':False,
    '6':False,
    '7':False,
    '8':False,
    '9':False,
    ':':False,
    ';':False,
    '<':False,
    '>':False,
    '?':False,
    '[':False,
    ']':False,
    'a':True,
    'b':True,
    'c':True,
    'd':True,
    'e':True,
    'f':True,
    'g':True,
    'h':True,
    'i':True,
    'j':True,
    'k':True,
    'l':True,
    'm':True,
    'n':True,
    'o':True,
    'p':True,
    'q':True,
    'r':True,
    's':True,
    't':True,
    'u':True,
    'v':True,
    'w':True,
    'x':True,
    'y':True,
    'z':True,
}

indice = 0
word_to_index = {}      # Acá vamos a guardar cada palabra, asociado a su indice.
index_to_word = []      # Acá vamos a guardar para cada indice una palabra.
uncommon = []

for p in list(char_common.keys()):
    if not(char_common[p]):
        word_to_index[p] = indice
        index_to_word.append(p)
        indice += 1
uncommon = copy(index_to_word)


with open("el_quijote_lower.txt", "r", encoding="ascii", errors='ignore') as f:
    for line in f.readlines():
        i = 0
        for j, l in enumerate(line):
            if not(char_common[l]):
                palabra = line[i:j]
                if not(palabra in word_to_index) and palabra!="":
                    word_to_index[palabra] = indice
                    index_to_word.append(palabra)
                    indice += 1
                i = j+1

#print(string_to_array("y asi, estoy probando. Sale bien?\n", uncommon))










