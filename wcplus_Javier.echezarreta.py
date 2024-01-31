from string import punctuation

print("< < < < < < < Bienvenido al Analizador TXT > > > > > > > ")

#Ingreso de datos que forman parte de la ruta del archivo txt que se analizará
while True:
      try:
        usuario_so = input("Ingrese el nombre de su usuario en Linux:")
        nombre_archivo = input("Ingrese el nombre del archivo de texto que quiere analizar (debe estar en el escritorio):")
        archivo_leido = "/home/" + usuario_so + "/Escritorio/" + nombre_archivo + ".txt"
        archivo = open(archivo_leido)
        break
      except FileNotFoundError:
        print("!!! Datos incorrectos ¡¡¡ Vuelva a ingresar sus datos por favor")

# Cantidad de lineas
archivo = open(archivo_leido)
total_lineas = sum(1 for line in archivo)
print("::: Total de lineas en el archivo de texto:", total_lineas,)

# Total de palabras
archivo = open("/home/javier/Escritorio/archivo.txt", "rt")
datos = archivo.read()
palabras = datos.split()
print("::: Total de palabras en el archivo de texto:", len(palabras))

# Cantidad de caracteres
archivo = open(archivo_leido)
caracteres = 0
for linea in archivo:
  caracteres += len(linea)
print("::: Total de caracteres en el archivo de texto:", caracteres)

# La palabra mas larga
archivo = open(archivo_leido)
texto = archivo.read()
# quita la puntuación ('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
texto = texto.translate(str.maketrans('', '', punctuation))  
lista_palabras = texto.split()
# Ordena la lista de palabras de acuerdo a su largo de manera descendente
lista_ordenada = sorted(lista_palabras, key=len, reverse=True)  
print("::: La Palabra mas larga del archivo de texto tiene", len(lista_ordenada[0]), "caracteres y es la siguiente:", lista_ordenada[0])
print("")

# La oracion mas larga
archivo = open(archivo_leido)
texto = archivo.read()
oracion = texto.split(".")
oracion_mas_larga = sorted(oracion, key=len, reverse=True)
print("::: La oracion mas larga", "tiene", len(oracion_mas_larga[0].split()), "palabras", "y es la siguiente:")
print(oracion_mas_larga[0])
print("")


archivo = open(archivo_leido)
lectura_parrafo = archivo.read()
parrafos = lectura_parrafo.split("." "\n" "\n") 
parrafo_mas_largo = sorted(parrafos, key=len, reverse=True)
cantidad_de_palabras = len(parrafo_mas_largo[0].split())
cantidad_de_caracteres = len(parrafo_mas_largo[0])
print("::: El parrafo mas largo tiene", cantidad_de_palabras, "palabras,", cantidad_de_caracteres, "caracteres", "y es el siguiente:") 
print("")
print(parrafo_mas_largo[0])