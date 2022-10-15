#! python3
# -*- coding: utf-8 -*-

import random
#import docx
#from . import docxprint
#code: pip install PyHyphen
from hyphen import Hyphenator
de_DE = Hyphenator('de_DE')

def syl_shuffle(some_nouns):
	try:
		import docxprint
	except ImportError:
		from learny import docxprint
	#python-docx module code: pip install python-docx
	import docx
	Aufgabe = {
		"Kopfzeile": "Name: 				Klasse: 				Datum:  \n ",
		"Titel": "",
		"1. Aufgabe": "Finde die Wörter aus den Lücken!\n",
		"Hinweise": "Hier sind die Wörter aus den Lücken: \n",
		"Rätselwörter": "Hier ein paar Rätselwörter aus dem Text: \n",
	}
	doc = docx.Document()# initializing python-docx
	save_path = docxprint.docx_print(Doc= doc, save= 'sylshuffle')
	print("some_nouns", some_nouns)

	some_nouns = list(set(some_nouns))
	#list(dict.fromkeys(some_nouns)) #erase duplicates
	random.shuffle(some_nouns) #shuffle für Rätselwörter
	docxprint.docx_print(printText=Aufgabe["Rätselwörter"], Bold=True, Doc=doc)
	print("some_nouns", some_nouns)


	for word in some_nouns:
		#hyph = de_DE.syllables(word.text)
		hyph = de_DE.syllables(word)
		random.shuffle(hyph)
		if hyph != []:
			shuffled = ' '.join(hyph)
			#print(hyph)
		if word == some_nouns[-1]:
			break
		word = str(word)
		#shuffled = list(word)
		#random.shuffle(shuffled)
		shuffled = ''.join(shuffled)
		#print(shuffled + ' ______________________________')
		#docxprint.docx_print(printText=shuffled + ' ______________________________', Doc=doc)
		print(shuffled)

	#doc.save(save_path)

if __name__ == "__main__":
	import clozetest, createListOfVerbs
	language = "Sprache: Deutsch"

	input= """
	Der Komiker heißt Chris Rock. Er hat auf der Bühne gesprochen und Witze gemacht. Er hat auch einen Witz gemacht über die Frau von Will Smith. Sie heißt Jada Pinkett Smith. Chris Rock hat sich darüber lustig gemacht, dass sie kaum noch Haare hat. Das fanden viele Leute nicht so lustig. Denn Jada Pinkett Smith hat eine Krankheit. Deswegen fallen ihre Haare aus.
Will Smith hat erst noch gelacht über den Witz, dann ist er aber auf die Bühne gelaufen und hat Chris Rock ins Gesicht geschlagen. Und er hat gerufen: Sprich nicht über meine Frau. Chris Rock hat einfach weiter geredet. Die Zeremonie lief auch weiter. Kurz danach hat Will Smith einen Oscar als bester Schauspieler bekommen. In seiner Dankes-Rede hat er gesagt: Ich wollte meine Familie verteidigen. Später hat er sich noch bei Chris Rock entschuldigt und bei den Veranstaltern. Es gibt viel Kritik an Will Smith. Viele andere Schauspielerinnen und Schauspieler sagen: Gewalt ist niemals richtig. Manche finden aber auch: Er hat nur seine Frau gegen eine Beleidigung verteidigt.
Es ging bei der Verleihung aber auch noch um Filme. Der Film „CODA“ hat den Preis als bester Film bekommen. Es geht um ein Mädchen, das bei einer gehör-losen Familie aufwächst. Beste Schauspielerin ist Jessica Chastain. Auch 2 Deutsche haben einen Oscar bekommen: Der Komponist Hans Zimmer und der Experte für spezielle Film-Effekte, Gerd Nefzer.
	"""
	#someNouns, noun_list = clozetest.cloze_test(input, language)
	textverb, infinit_verb_list = createListOfVerbs.infinitive(input, language)
	#syl_shuffle(some_nouns= noun_list)
	syl_shuffle(some_nouns=infinit_verb_list)
