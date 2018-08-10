# -*- coding: utf-8 -*-
import codecs

def text2stop(fileDir, stop):
	f = codecs.open(fileDir, 'r', 'utf-8')

	text = f.read()
	text = text.replace('\r\n', " ")
	text = text.split(' ')

	f.close()
	return text

stop = []

stop += text2stop("stopwords.txt", stop)
stop += text2stop("stop_words.txt", stop)
stop += text2stop("name_rus.txt", stop)

stop = set(stop)
text = ''
for i in stop:
	text += i + ' '

f = codecs.open("stop.txt", 'w', 'utf-8')
f.write(text)
f.close()