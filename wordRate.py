# -*- coding: utf-8 -*-

import codecs
import pymorphy2
import operator

import IOFile as IO
import VK
import FB
from math import log

morph = pymorphy2.MorphAnalyzer()

f = codecs.open("files/input/stop.txt", 'r', 'utf-8')
stop_words = f.read()
stop_words = stop_words.split(' ')

f.close()


# функция, добавляющая слова из текста к рейтингу
def text2rate(text):
    rate = {}
    write = False  # записываем ли слово в данный момент
    htag = False
    word = ''

    text += ' '

    # для каждого символа текста
    for i in text:
        if (i == '#'):
            htag = True

        if write:
            # если буква, то записываем её в слово
            if (i.isupper() or i.islower()):
                word += i
            else:
                # не берем в счет слова, состоящие из 1-ой буквы, чтобы не включать лишний раз морфологический анализатор
                if (len(word) == 1):
                    word = ''
                    write = False
                    continue

                # получаем анализ слова
                p = morph.parse(word.lower())[0]

                # записываем только существительные, потому что они более информативны
                if ('NOUN' in p.tag) and (p.normal_form not in stop_words):
                    word = p.normal_form
                else:
                    word = ''
                    write = False
                    continue

                # увеличиваем рейтинг слова или заносим со значением 1
                if word in rate:
                    rate[word] += 1
                else:
                    rate[word] = 1

                word = ''
                write = False
        else:
            if (htag):
                if (i == ' '):
                    htag = False
            elif (i.isupper() or i.islower()):
                word += i
                write = True
    return rate


# сравнение двух словесных характеристик и выдача коэффициента подобности
def compareRate(rate1, rate2):
    counter = 0

    for i in rate1:
        if i in rate2:
            counter += min(rate1[i], rate2[i])

    return counter


def addRate(rateFrom, rateTo):
    for key in rateFrom:
        if key in rateTo:
            rateTo[key] += rateFrom[key]
        else:
            rateTo[key] = rateFrom[key]



def saveRate(fileDir, rate):
    f = codecs.open(fileDir, 'w', 'utf-8')

    for i in rate:
        output = i + " " + str(rate[i]) + '\r\n'
        f.writelines(output)

    f.close()

def loadRate(fileDir):
    f = codecs.open(fileDir, 'r', 'utf-8')

    rate = {}
    for line in f:
        line = line.split(' ')
        rate[line[0]] = float(str(line[1].strip("\n")))

    f.close()
    return rate

def sortRate(rate):
    rate = sorted(rate.items(), key=operator.itemgetter(1), reverse=True)
    return dict(rate)


def topWords(rate, top):
    new_rate = {}
    for i in rate:
        new_rate[i] = rate[i]
        if (top == len(new_rate)):
            break
    return new_rate

# Поиск цифрового ID
def searchUser(user_id):
    if not user_id.isdigit():
        user_id = VK.getId(user_id)

    return user_id

'''
def wordRate(collection):
    idf = {}        # сначала для каждого слова храниться кол-во документов, в котором оно встречается
    terms_doc_matrix = []

    # считаем количество входений слов в документ
    for doc in collection:
        termFreq = text2rate(doc)
        terms_doc_matrix.append(termFreq)

        for term in termFreq:
            if term in idf:
                idf[term] += 1
            else:
                idf[term] = 1

    col_len = len(collection)
    idf = {k: log(col_len/v) for k, v in idf.items()}
    wordRate = {k: 0 for k in idf.keys()}

    for doc in terms_doc_matrix:
        total_terms = sum(doc.values())

        for term, n in doc.items():
            wordRate[term] += n/total_terms * idf[term]

    wordRate = sortRate(wordRate)
    return topWords(wordRate, 100)
'''

def wordRate(collection):
    wordRate = {}

    # считаем количество входений слов в документ
    for doc in collection:
        termFreq = text2rate(doc)
        total_terms = sum(termFreq.values())

        for term, n in termFreq.items():
            if term in wordRate:
                wordRate[term] += n/total_terms
            else:
                wordRate[term] = n/total_terms

    wordRate = sortRate(wordRate)
    return topWords(wordRate, 100)

# функция возврата рейтинга слов
def wordRateVK(user_id):
    user_id = searchUser(user_id)

    # запрашиваем лист групп
    user_groups = VK.getGroupsUser(user_id)

    if (user_groups != 1):
        post_list = VK.getPost(user_groups, mode='group')
        post_list = [post['text'] for post in post_list]

        return wordRate(post_list)
    return {}

def wordRateFB(obj_id):
    feed = FB.getFeed(obj_id)

    # у каждой группы достаем посты
    col = [post['message'] for post in feed]
    return wordRate(col)