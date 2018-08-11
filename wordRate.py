# -*- coding: utf-8 -*-

import codecs
import pymorphy2
import operator

import IOFile as IO
import VK

morph = pymorphy2.MorphAnalyzer()

f = codecs.open("files/input/stop.txt", 'r', 'utf-8')
stop_words = f.read()
stop_words = stop_words.split(' ')

f.close()

# функция, добавляющая слова из текста к рейтингу
def text2rate(text, rate):
	write = False # записываем ли слово в данный момент
	htag = False
	word = ''

	text += ' '

	# для каждого символа текста
	for i in text:
		if (i == '#'):
			htag = True

		if write:
			# если буква, то записываем её в слово
			if ( i.isupper() or i.islower()):
				word += i
			else:
				# не берем в счет слова, состоящие из 1-ой буквы, чтобы не включать лишний раз морфологический анализатор
				if (len(word) == 1):
					word = ''
					write = False
					continue

				# получаем анализ слова
				p = morph.parse(word.lower())[0]


				#записываем только существительные, потому что они более информативны
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
			elif ( i.isupper() or i.islower()):
				word += i
				write = True
	pass

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
			rateTo[key] += 1
		else:
			rateTo[key] = 1
	pass

def saveRate(fileDir, rate):
	f = codecs.open(fileDir, 'w', 'utf-8')

	for i in rate:
		output = i + " " + str(rate[i]) + '\r\n'
		f.writelines(output)

	f.close()
	pass

def loadRate(fileDir):
	f = codecs.open(fileDir, 'r', 'utf-8')

	rate = {}
	for line in f:
		line = line.split(' ')
		rate[line[0]] = float(str(line[1].strip("\n")))

	f.close()
	return rate

def sortRate(rate):
	rate = sorted(rate.items(), key = operator.itemgetter(1), reverse = True)
	return dict(rate)

def topWords(rate, top):
	new_rate = {}
	for i in rate:
		new_rate[i] = rate[i]
		if (top == len(new_rate)):
			break
	return new_rate


# # 			ТЕСТИРОВАНИЕ
#
# wordRate = {}
# buffRate = {} # временный рейтинг слов
#
# # чистим директории от файлов
# IO.clearDir("files/output")
#
#
# id_list = IO.getFromFile('input/static.txt', 1)
# if (id_list != 1):
#
# 	for user_id in id_list:
# 		print("Анализируем пользователя: ", str(user_id))
#
# 		# для каждого текущего человека запрашиваем лист его групп
# 		user_groups = VK.getGroupsUser(user_id)
#
# 		if (user_groups != 1):
# 			post_list = VK.getPost(user_groups, 'groups')
# 			# у каждой группы достаем посты
# 			for group in post_list:
# 				for post in group:
# 					text = post['text']
# 					# сохраненные посты добавляем в рейтинг слов
# 					text2rate(text, buffRate)
#
# 					# делим на кол-во слов в посте
# 					for i in buffRate:
# 						buffRate[i] /= len(buffRate)
#
# 					addRate(buffRate, wordRate)
# 					buffRate = {}
#
# 		# делим на количство групп, чтобы те, у кого их больше, не имели высшие оценки из-за больших соответствий слов
# 		for key in wordRate:
# 			wordRate[key] /= len(user_groups)
#
# 		wordRate = sortRate(wordRate)
# 		# сохраняем словесную характеристику
# 		saveRate('files/output/' + str(user_id) + ".txt", topWords(wordRate, 100))




def wordRateFlask(user_id):
	wordRate ={}
	buffRate = {}

	# для каждого текущего человека запрашиваем лист его групп
	user_groups = VK.getGroupsUser(user_id)

	if (user_groups != 1):
		post_list = VK.getPost(user_groups, 'groups')
		# у каждой группы достаем посты
		for group in post_list:
			for post in group:
				text = post['text']
				# сохраненные посты добавляем в рейтинг слов
				text2rate(text, buffRate)

				# делим на кол-во слов в посте
				for i in buffRate:
					buffRate[i] /= len(buffRate)

				addRate(buffRate, wordRate)
				buffRate = {}

		# делим на количство групп, чтобы те, у кого их больше, не имели высшие оценки из-за больших соответствий слов
		for key in wordRate:
			wordRate[key] /= len(user_groups)

		wordRate = sortRate(wordRate)
		# сохраняем словесную характеристику
		return topWords(wordRate, 100)