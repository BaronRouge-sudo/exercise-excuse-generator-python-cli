import random
import math


# array with the words

sustantivo = ['runner ','perro ','T-rex ', 'ladrón ', 'payaso ', 'niño ', 'tiburón ']
adjetivo = ['verde ', 'radioactivo ', 'rabioso ', 'loco ','tetrapléjico ','chillón ','sonriente ','desfigurado ','apestoso ' ]
verbo = ['babeó ', 'lanzó ', 'destrozó ' , 'mojó ', 'regaló ', 'sorteó ', 'robó ', 'quemó ']
objeto = ['libro ', 'paraguas ', 'cartera ', 'smartphone ', 'pantalón ', 'conida ', 'monóculo ', 'tablet ', 'llavero ']
lugar = ['la estación de tren','la oficina','el colegio', 'mi garaje', 'la plaza del pueblo', 'el ayuntamiento', 'una granja']

# declaring random variables

sustantivo_random = int(math.floor(random.randint(0, len(sustantivo)-1)))
adjetivo_random = int(math.floor(random.randint(0, len(adjetivo)-1)))
verbo_random = int(math.floor(random.randint(0, len(verbo)-1)))
objeto_random = int(math.floor(random.randint(0, len(objeto)-1)))
lugar_random = int(math.floor(random.randint(0, len(lugar)-1)))

# creating a sentence (the excuse)
print('Un '+ sustantivo[sustantivo_random]  + adjetivo[adjetivo_random] + verbo[verbo_random] + "mi " + objeto[objeto_random] + "en "+ lugar[lugar_random])
