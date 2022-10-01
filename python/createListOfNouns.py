#-*- coding: UTF-8 -*-
def createListOfNouns(inputtext, language):
    """returns list of nouns in given input text.requires spacy, default german"""
    import spacy #code: pip install spacy
    try:
    	import languageload
    except ImportError:
    	from learny import languageload

    # variables and lists used
    noun_list = []

    nlp = languageload.language_load(language)
    docnlp = nlp(inputtext) #load to spacy

    for token in docnlp:
    	if 'NOUN' in token.pos_:
    		noun_list.append(str(token.lemma_))# complete list of nouns
    print("returning this noun list:", noun_list)
    return noun_list



if __name__ == "__main__":
    input="""In vielen Getränken in Deutschland ist zu viel Zucker. Das hat die Organisation „Foodwatch“ festgestellt. Wenn man zu viel Zucker isst, kann man zu dick und krank werden.

    Die Organisation „Foodwatch“ hat 463 Limonaden, Energy Drinks, Saft-Schorlen und Eis-Tees untersucht. „Foodwatch“ ist ein englisches Wort und heißt Lebens-Mittel-Überwachung. Nur sechs Getränke waren nicht gezuckert. Das süßeste Getränk – ein Energy-Drink – hatte in einer halben Liter Dose 78 Gramm Zucker. Das sind 26 Stück Würfel-Zucker.
    Die Welt-Gesundheits-Organisation hat empfohlen: Ein Mensch sollte nicht mehr als sechs Tee-Löffel Zucker am Tag essen. Wenn man mehr Zucker isst, können die Zähne krank werden oder man wird zu dick. Eine große Gefahr ist auch die Zucker-Krankheit. Sie wird Diabetes genannt. Daran kann der Mensch sterben.
    In dem Land Groß-Britannien soll es deshalb ab 2018 eine Zucker-Steuer geben, damit die Hersteller weniger süße Getränke verkaufen.
    „Foodwatch“ fordert: Auch in Deutschland soll es eine Zucker-Steuer geben. Die Bundes-Regierung lehnt das ab. Der Minister für Ernährung, Christian Schmidt, sagt: Straf-Steuern auf Lebens-Mittel sind der falsche Weg. Die Menschen sollen besser über gesunde Lebens-Mittel informiert werden. Am besten schon in der Schule. """
    list = createListOfNouns(inputtext= input, language="")
    import duden
    for word in list:
        #print(word)
        #word = "Getränk"
        aeWord = word.replace("ä", "ae")
        ueWord = aeWord.replace("ü", "ue")
        oeWord = ueWord.replace("ö", "oe")
        try:
            w = duden.get(oeWord)
            print(w.article, word)

        except AttributeError:
            print("didnt find result")
            continue
