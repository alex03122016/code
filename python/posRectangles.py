import playground



def mittleresRechteck():
    allsearchedNumbers = playground.allsearchedNumbers
    middle = len(allsearchedNumbers)/2
    middleNumber= allsearchedNumbers[int(middle)]
    return print(middleNumber)

def idealposition(xlength= playground.xlength, searchedNumber=playground.searchedNumber, leftborder=playground.leftBorder):
	posOfNumber = x+ ((searchedNumber - start) * schritt)
	print("posOfNumber:", posOfNumber, searchedNumber)


    rectangle.leftx +(xlength/2) = number.pos
    rectangle.leftx = posOfNumber - (xlength/2)
    rectangle.rightx = rectangle.leftx + length

	#Creating rectangle

	context.rectangle(pos, 0.6, 0.2, 0.1)#(x pos of upper left corner, y position of upper left corner, x length, y length)
	context.stroke()
	ctx.move_to(pos+0.05, 0.6+0.075)
	ctx.show_text(str(searchedNumber))



    return rectangle.leftx, rightx

"""
Def überlappt:
Return true false

Def outOfLeftspace:
Return true false

Def outIfRightSpace:
returnTrue, false

def vorgänger:
Return true false


Def nachfolger:
Return true false




Ausgangsposition:
Alle in idealposition

Mittleres Rechteck überlappt? nein? Dann keep in place

Ja? Function

alle Vorgänger schritt nach links
Alle Nachfolger Schritt nach rechts

Vorgänger out of space? Ja/nein
Wenn ja, dann mittleres Rechteck schritt nach rechts
"""


if __name__ == '__main__':

    print("Hi")
    mittleresRechteck()
