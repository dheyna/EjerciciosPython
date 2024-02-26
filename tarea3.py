import os

def crear_carpetas_y_ficheros(ruta_absoluta):
	for i in range(1, 6):
		carpeta = os.path.join(ruta_absoluta, f"folder{i}")
		os.makedirs(carpeta, exist_ok=True)
		for j in range(1, 11):
			nombre_fichero = os.path.join(carpeta, f"fichero{j}.txt")
			with open(nombre_fichero, 'w') as f:
				f.write("Este es el contenido del fichero 1\n")

ruta_absoluta = "/home/dheyna"

crear_carpetas_y_ficheros(ruta_absoluta)
