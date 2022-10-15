
import cairo


with cairo.SVGSurface("Zahlenstrahl.svg", 800, 800) as surface:
	context = cairo.Context(surface)
	x, y, x1, y1 = 0.1, 1.0, 1.9, 1.0
	x2, y2, x3, y3 = 0.6, 0.1, 0.9, 0.5
	context.scale(400, 400)
	context.set_line_width(0.01)
	context.move_to(x, y)
	#schritt= 0.015
	# Creating shape
	#context.rectangle(25, 50, 50, 120)
	number = 0
	context.set_line_width(0.005)
	import random
	#schritt= random.randint(15,90)/1000
	"zwischen startpunkt und endpunkt die länge = Differenz von Startzahl und Endzahl * schritt"
	"schritt = zwischen startpunkt und endpunkt die länge / Differenz von Startzahl und Endzahl "
	"schritt = (x1-x)) / Differenz von Startzahl und Endzahl "
	zahlenraum = 100 # 5, 10, 100,1000, Benutzerdefiniert
	start = random.randrange(0,zahlenraum-20,10)
	print("start", start)
	end = random.randrange(start+10, zahlenraum, 10)
	print("end", end)
	print("differnce", end - start)
	schritt = (x1-x)/(end - start)
	laenge= 0.05 # length of big line

	#draw horizontal line
	context.line_to(x1, y1)
	context.stroke()

	#draw vertical line
	for number in range(start,end+1):
		print('x:', x)
		context.move_to(x, y)

		if number%10==0:
			#ctx.show_text(str(number))
			context.line_to(x, y-(laenge+0.05))
			print("print big line", number)
		else:
			context.line_to(x, y-laenge)
		context.stroke()
		number = number +1
		x = x+ schritt

		#if (x-0.5)>=x1:
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

	x,y = 0.1, 0.85
	number= 0
	schrittweite= 10

	for number in range(start, 100):
		if x-0.1>=x1:
			break
		ctx.move_to(x, y)
		x = x + schritt
		if number%schrittweite==0:
			ctx.show_text(str(number))
