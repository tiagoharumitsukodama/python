import csv

hiraganas = []
legendas = []

with open('hiraganaList.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=" ", quotechar='|')


	for row in spamreader:
		tudoJunto =  (', '.join(row))
		separado = tudoJunto.split()

		hiraganas.append(separado[0])
		legendas.append(separado[1])



with open('result.csv','a') as f:
	writer = csv.writer(f)

	for i in range(len(hiraganas)):
		writer.writerow((hiraganas[i], legendas[i]))
