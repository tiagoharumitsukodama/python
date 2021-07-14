from PIL import Image

im = Image.open('labenu.png')
pix = im.load()

(xMax, yMax) = im.size
matriz = ''


for i in range(xMax):
	linha = ''

	for j in range(yMax):

		(r,g,b) = pix[j,i]
		escala = (r+g+b)

		if escala == 765:
			linha = linha + ' '

		elif escala <= 394:
			linha = linha + 'a'

		elif escala > 394 and escala <= 534:
			linha = linha + 'A'

		elif escala > 534 and escala <= 631:
			linha = linha + 'a'

		elif escala > 631 and escala <= 743:
			linha = linha + 'A'

		else:
			linha = linha + ' '

	linha = linha + '\n'
	matriz = matriz + linha

print (matriz)
