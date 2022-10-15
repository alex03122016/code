#-*- coding: UTF-8 -*-

def getArticle(noun):
    """Argument is a noun returns article from duden.de requires internet acces"""
    import duden
    aeNoun = noun.replace("ä", "ae")
    ueNoun = aeNoun.replace("ü", "ue")
    oeNoun = ueNoun.replace("ö", "oe")
    try:
        w = duden.get(oeNoun)
        print(w.article, noun)
        return w.article


    except AttributeError:
        print("didnt find result for Noun:", noun)

if __name__ == "__main__":
    from createListOfNouns import createListOfNouns

    input="""In vielen Getränken in Deutschland ist zu viel Zucker. Das hat die Organisation „Foodwatch“ festgestellt. Wenn man zu viel Zucker isst, kann man zu dick und krank werden.

    Die Organisation „Foodwatch“ hat 463 Limonaden, Energy Drinks, Saft-Schorlen und Eis-Tees untersucht. „Foodwatch“ ist ein englisches Wort und heißt Lebens-Mittel-Überwachung. Nur sechs Getränke waren nicht gezuckert. Das süßeste Getränk – ein Energy-Drink – hatte in einer halben Liter Dose 78 Gramm Zucker. Das sind 26 Stück Würfel-Zucker.
    Die Welt-Gesundheits-Organisation hat empfohlen: Ein Mensch sollte nicht mehr als sechs Tee-Löffel Zucker am Tag essen. Wenn man mehr Zucker isst, können die Zähne krank werden oder man wird zu dick. Eine große Gefahr ist auch die Zucker-Krankheit. Sie wird Diabetes genannt. Daran kann der Mensch sterben.
    In dem Land Groß-Britannien soll es deshalb ab 2018 eine Zucker-Steuer geben, damit die Hersteller weniger süße Getränke verkaufen.
    „Foodwatch“ fordert: Auch in Deutschland soll es eine Zucker-Steuer geben. Die Bundes-Regierung lehnt das ab. Der Minister für Ernährung, Christian Schmidt, sagt: Straf-Steuern auf Lebens-Mittel sind der falsche Weg. Die Menschen sollen besser über gesunde Lebens-Mittel informiert werden. Am besten schon in der Schule. """
    list = createListOfNouns(inputtext= input, language="")
    for noun in list:
        getArticle(noun)
        continue
