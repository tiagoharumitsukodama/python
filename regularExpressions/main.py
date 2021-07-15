# Regular expressions
### + e [ab]+ e "[^.?!]+"
### * e [ab]* zero ou mais
### [ab]{3}
### [a-z] e [A-Z]
### r'\d+' e r'\D+' e r'\s' e r'\S' e r'\w' r'\W'

import re

texto = '''E esse papo todo de melhorar é muito
importante agora porque passamos oficialmente da metade do ano.
E eu não sou vidente, mas eu tenho certeza de que algumas das
suas metas de ano novo precisam ser recalculadas, acertei?'''

palavras = re.split('[ ,.?!\n]', texto)
letrasProcuro = 'ce'
ocorrencias = 0

for palavra in palavras:
    if re.search(letrasProcuro, palavra) != None:
        print('A palavra "{}" contém "{}"'.format(palavra, letrasProcuro))
        ocorrencias = ocorrencias + 1

print("{} resultados".format(ocorrencias))
