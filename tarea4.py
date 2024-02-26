import psutil
import logging

#Esto es la configuracion del logging
logging.basicConfig(filename='/home/dheyna/logs/espacio.log', level=logging.INFO,
		format='%(asctime)s - %(levelname)s - %(message)s')

#Creación funcion para analizar el espacio disponible en la particion raiz
def analizar_espacio():
	espacio_usado_percent = psutil.disk_usage('/').percent
	if espacio_usado_percent > 80:
		logging.error("Espacio ocupado es mayor que 80%")
	elif espacio_usado_percent > 60:
		logging.warning("Espacio ocupado es mayor que 60% pero menor que 80%")
	else:
		logging.info("Espacio ocupado es menor que 60%")

# Función para Tarea5.py que obtiene y registra información sobre el uso de la CPU
def analizar_cpu():
    uso_cpu_percent = psutil.cpu_percent(interval=1)
    if uso_cpu_percent > 80:
        logging.error("Uso de CPU es mayor que 80%")
    elif uso_cpu_percent > 60:
        logging.warning("Uso de CPU es mayor que 60% pero menor que 80%")
    else:
        logging.info("Uso de CPU es menor que 60%")

if __name__ == "__main__":
    analizar_espacio()
    analizar_cpu()
