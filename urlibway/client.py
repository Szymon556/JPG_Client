import urllib.request

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')#otwieramy połączenie
fhand = open('pict.jpg','wb')#tworzymy uchwyt do pliku gdzie zapiszemy nasz obraz
size = 0
while True:
    chunk = img.read(100000)#odczytujemy po 10000 tys znaków 
    if len(chunk) < 1: break
    size = len(chunk) + size
    fhand.write(chunk)
print(f'Skopiowano: {size} znaków')
fhand.close()
