
#sudo apt-get install libcurl4-gnutls-dev
#pip install pycurl
#pip install wptools


def download_images(searchquery):
	import pycurl
	import wptools
	#https://github.com/siznax/wptools/wiki/Examples#get-a-representative-image
	import requests
	import os


	page = wptools.page(searchquery, lang="de")
	print(page.get_query())
	result = page.images(['url', 'file'])
	print(result[0]['url'], "Dateiname: ", result[0]['file'])

	url = result[0]['url']
	file = result[0]['file']
	print(file)
	r = requests.get(url)
	save_path = os.path.join(os.path.expanduser('~'),'learny', 'learny', f"{searchquery }-{file[5:]}")

	with open(save_path, 'wb') as f:
#	with open(f'/home/alex/Downloads/{searchquery }-{file[5:]}', 'wb') as f:
	    f.write(r.content)

	# Retrieve HTTP meta-data
	print(r.status_code)
	print(r.headers['content-type'])
	print(r.encoding)

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

	download_images("Bus")
