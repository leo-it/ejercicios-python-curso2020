frase = 'todos somos programadores'
palabra_t = []
palabras = frase.split()
frase_t = []
for palabra in palabras:
    if palabra[-1] == 'o':
        for p in palabra:
            palabra_t.append(p)
        palabra_t[-1] = 'e'
        palabra_t = ''.join(palabra_t)
    elif len(palabra) >1 and palabra[-2] == 'o'   :
        for p in palabra:
            palabra_t.append(p)
        palabra_t[-2] = 'e'
        palabra_t = ''.join(palabra_t)
    else:
        for p in palabra:
            palabra_t.append(p)
        palabra_t = ''.join(palabra_t)
    frase_t.append(palabra_t)
    palabra_t = []
frase_t = ' '.join(frase_t)
print( frase_t)