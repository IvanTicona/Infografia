#Listas
lista_compras = ['papa', 'zanahoria', 'carne'] #mutable
lista_compras[-1] #Ultimo elemento
lista_compras[-2] #Penultimo elemento
#.append(item)
#.remove(item)
#.index(item)
#.pop()
#.insert(index,item)

#Tuplas
lista_compras = ('cebolla', 'choripan', 'cerveza') #inmutable

#Diccionarios
dic_estudiantes = {
  'sosa': 68,
  'choque': 78
}

dic_estudiantes["choque"]
dic_estudiantes["sosa"]
dic_estudiantes["perez"] = 50 #Crear nuevo

for k, v in dic_estudiantes.items():
  print(k, v)

#Conjuntos
conj_compras = set(lista_compras)
conj_alergias = set(["ajo", "mani"])

conj_compras.intersection(conj_alergias)

#PYTHON ARCADE