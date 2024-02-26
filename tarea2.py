import psutil

def obtener_porcentaje_espacio(particion):
	disco = psutil.disk_usage(particion)
	porcentaje_ocupado = disco.percent
	return porcentaje_ocupado

def mostrar_porcentaje_espacio(particiones):
	for particion in particiones:
	    porcentaje = obtener_porcentaje_espacio(particion)
	    print(f"{particion}{porcentaje:.1f}%")

particiones = ['/dev/sda1','/dev/sda2','/dev/sda3']
mostrar_porcentaje_espacio(particiones)
