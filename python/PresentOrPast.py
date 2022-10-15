#! python3
# -*- coding: utf-8 -*-


def textblobmorph(found_verb):
	from textblob_de.packages import pattern_de as pd
	from _pattern.de import conjugate
	from _pattern.de import INFINITIVE, PRESENT, SG, SUBJUNCTIVE, INDICATIVE, PAST, PARTICIPLE
	printString = {}

	print('1 person present tense:  ', conjugate(	found_verb.lemma_,
	 												PRESENT,
													1,
													SG,
													mood=INDICATIVE
												)
		)

	print('1 person past tense: ', conjugate(		found_verb.lemma_,
	 												PAST,
													1,
													SG,
													mood=INDICATIVE
												)
		)

	pres1 = 'ich ' + conjugate(found_verb.lemma_, PRESENT, 1, SG, mood=INDICATIVE)
	past1 = 'ich ' + conjugate(found_verb.lemma_, PAST, 1, SG, mood=INDICATIVE)
	perf1 = 'ich habe/bin ' + conjugate(found_verb.lemma_, PAST, 1, SG, mood=INDICATIVE, aspect=PARTICIPLE)
	print(perf1)

	printString['pres1'] = pres1
	printString['past1'] = past1
	printString['perf1'] = perf1


	return printString

def present_or_past(inputtext, language):
	import subprocess
	import spacy
	#from spacy.lang.de.examples import sentences
	try:
		import docxprint, languageload
	except ImportError:
		import docxprint, languageload


	print('Starting Program: Present or Past or Participle'+ "\n"*5)

	# variables and lists used
	i = 0
	found_verbs_list = []
	looked_up_verbs_list = []
	mix_list = []

	nlp = languageload.language_load(language) #load language to spacy

	# load text from kivy to spacy
	docnlp = nlp(inputtext)
	print(docnlp.text)

	#creating list of found  verbs
	for token in docnlp:
		if 'AUX' in token.pos_:
			found_verbs_list.append(token)
		if 'VERB' in token.pos_:
			found_verbs_list.append(token)
	print('I found the following verbs: ', found_verbs_list)

	#look up 1person present tense and past tense of a word in the given text
	for found_verb in found_verbs_list[0:-1]:
		print(	"\n"*5 + '\033[31mbeginning\033[0m with look up of this word: '
				+ str(found_verb)+ "\n"*2)

		#looked_up_verbs_dictionary = lookupDEMorphy(found_verb)
		looked_up_verbs_dictionary = textblobmorph(found_verb)
		looked_up_verbs_list.append(list(looked_up_verbs_dictionary.values()))

		print("\n"*2 + 'result from look up: ')
		for result in looked_up_verbs_list:
			print(result)
		print("\n"*5)
		print('ready with look up'+ '\n'*2)

	#create worksheet .doc file
	docxprint.print_present_or_past(	looked_up_verbs_list=looked_up_verbs_list,
										found_verbs_list=found_verbs_list)

	return
if __name__ == "__main__":

	input= """
	Pascal sitzt im Bus in der zweitletzten Reihe .
	 Ein großer Junge mit einer Wasserflasche
	 setzt sich hinter ihn , nimmt einen Schluck
	 Wasser aus der Flasche und spuckt es ihm auf
	 den Kopf . Haare und Klamotten sind nass .

	 Der 14-jährige Kevin sitzt im Rollstuhl . Jeden
	 Morgen wartet er auf das Taxi und wird von
	 einigen Jugendlichen gemobbt . Sie stellen sich
	 in den Weg , sodass er auf dem Bürgersteig
	 nicht mehr weiter kann . „ Hast du ein Problem ? ” ,
	 fragt ihn einer . Die anderen lachen .

	"""
	present_or_past(inputtext=input, language="Sprache: Deutsch")
