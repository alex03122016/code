
import cairo


with cairo.SVGSurface("Zahlenstrahl.svg", 800, 800) as surface:
	context = cairo.Context(surface)
	leftBorder, y, rightBorder, y1 = 0.1, 1.0, 1.9, 1.0
	x2, y2, x3, y3 = 0.6, 0.1, 0.9, 0.5
	context.scale(400, 400)
	context.set_line_width(0.01)
	context.move_to(leftBorder, y)
	#schritt= 0.015
	number = 0
	context.set_line_width(0.005)
	import random
	#schritt= random.randint(15,90)/1000
	"zwischen startpunkt und endpunkt die länge = Differenz von Startzahl und Endzahl * schritt"
	"schritt = zwischen startpunkt und endpunkt die länge / Differenz von Startzahl und Endzahl "
	"schritt = (rightBorder-x)) / Differenz von Startzahl und Endzahl "
	zahlenraum = 100 # 5, 10, 100,1000, Benutzerdefiniert
	startNumber = random.randrange(0,zahlenraum-20,10)
	print("startNumber", startNumber)
	end = random.randrange(startNumber+10, zahlenraum, 10)
	print("end", end)
	print("differnce", end - startNumber)
	schritt = (rightBorder-leftBorder)/(end - startNumber)
	laenge= 0.05 # length of big line

	#draw horizontal line
	context.line_to(rightBorder, y1)

	context.stroke()

	#draw vertical line
	for number in range(startNumber,end+1):
		print('leftBorder:', leftBorder)
		context.move_to(leftBorder, y)

		if number%10==0:
			#ctx.show_text(str(number))
			context.line_to(leftBorder, y-(laenge+0.05))
			print("print big line", number)
		else:
			context.line_to(leftBorder, y-laenge)
		context.stroke()
		number = number +1
		leftBorder = leftBorder+ schritt

		#if (x-0.5)>=rightBorder:
		#	print("x bigger than endpoint", x)
		#	break



#draw numbers
	WIDTH = 3
	HEIGHT = 2
	PIXEL_SCALE = 400

	ctx = cairo.Context(surface)
	ctx.set_source_rgb(0, 0, 0)
	ctx.set_font_size(0.10)
	ctx.select_font_face("Arial",
	                     cairo.FONT_SLANT_NORMAL,
	                     cairo.FONT_WEIGHT_NORMAL)
	ctx = cairo.Context(surface)
	ctx.scale(PIXEL_SCALE, PIXEL_SCALE)

	ctx.set_source_rgb(0, 0, 0)
	ctx.set_font_size(0.08)
	ctx.select_font_face("Arial",
	             cairo.FONT_SLANT_NORMAL,
	             cairo.FONT_WEIGHT_NORMAL)

	leftBorder,y = 0.1, 0.85
	number= 0
	schrittweite= 10

	for number in range(startNumber, 100):
		if leftBorder-0.1>=rightBorder:
			break
		ctx.move_to(leftBorder, y)
		leftBorder = leftBorder + schritt
		if number%schrittweite==0:
			ctx.show_text(str(number))

	allsearchedNumbers = []
	for n in range (0,4):
		allsearchedNumbers.append(random.randint(startNumber, end))
	allsearchedNumbers.sort()

	def createRectangle(searchedNumber, startNumber, schritt):
		#Creating rectangle
		leftBorder = 0.1
		pos = leftBorder+ ((searchedNumber - startNumber) * schritt)
		print("pos:", pos, searchedNumber)
		xlength= 0.2

		context.rectangle(pos, 0.6, xlength, 0.1)#(x pos of upper left corner, y position of upper left corner, x length, y length)
		context.stroke()
		ctx.move_to(pos+0.05, 0.6+0.075)
		ctx.show_text(str(searchedNumber))
		return

	for n in allsearchedNumbers:
		createRectangle(n, startNumber, schritt)
