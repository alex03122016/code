#! python3
# -*- coding: utf-8 -*-


def infinitive(inputtext, language):
	import docx
	from docx.shared import RGBColor
	from docx.shared import Pt
	import os
	import random
	import spacy
	try:
		import docxprint, languageload
	except ImportError:
		from learny import docxprint, languageload
	print('-------------------GENERATE infinit form of verbs: ')



	# variables and lists used
	i = 0
	verb_list = []
	some_verbs = []
	new_text = []
	infinit_verb_list = []
	textverb = []
	keptinfinitive = []
	non_infinit_verbs = []
	new_infinit_verbs = []

	nlp = languageload.language_load(language)
	docnlp = nlp(inputtext) #load to spacy
	print(docnlp.text)

	for token in docnlp:
		if 'AUX' in token.pos_:
			#print(token.lemma_)
			infinit_verb_list.append(token.lemma_)
			textverb.append(token.text)

		if 'VERB' in token.pos_:
			print(token.lemma_)
			infinit_verb_list.append(token.lemma_)

		elif 'AUX' in token.pos_:
			#paragraph.add_run('')
			pass
		else:
			pass
			#print(token)
			#docxprint.docx_print(printText=str(token) + ' ', Paragraph=paragraph, Doc=doc)

	infinit_verb_list = list(set(infinit_verb_list))
	textverb = list(set(textverb))
	print('infinit_verb_list: ', infinit_verb_list)

	#random.shuffle(mix_list)
	for word in textverb:
		if word not in infinit_verb_list:
			non_infinit_verbs.append(word)
			if word == textverb[-1]:
				print(word)
				break
			print(word)

	print("keptinfinitive:", keptinfinitive )

	random.shuffle(non_infinit_verbs)
	docnlp = nlp(" ".join(non_infinit_verbs)) #load to spacy
	for token in docnlp:

		print(token.lemma_ + '_'*31+"\n")

	print('done')
	return textverb, infinit_verb_list
