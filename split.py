import os
import shutil
from datetime import datetime

def organizar_archivos(ruta):
    # Obtener la lista de archivos
    archivos = [archivo for archivo in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, archivo))]
    total_archivos = len(archivos)
    
    # Procesar cada archivo
    for i, archivo in enumerate(archivos, start=1):
        archivo_path = os.path.join(ruta, archivo)

        # Obtener la fecha de modificación
        fecha_mod = datetime.fromtimestamp(os.path.getmtime(archivo_path))
        # Crear el nombre de la carpeta en formato "MesAño" (por ejemplo, "Noviembre22")
        nombre_carpeta = f"{fecha_mod.strftime('%B')}{fecha_mod.strftime('%y')}"
        carpeta_destino = os.path.join(ruta, nombre_carpeta)

        # Crear la carpeta si no existe
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        # Mover el archivo a la carpeta correspondiente
        shutil.move(archivo_path, carpeta_destino)
        
        # Mostrar progreso
        print(f"Organizando archivo {i} de {total_archivos}...")

    print("Organización de archivos completada con éxito.")

if __name__ == "__main__":
    ruta = input("Ingresa la ruta de la carpeta a organizar: ")
    if os.path.isdir(ruta):
        organizar_archivos(ruta)
    else:
        print("La ruta especificada no es válida.")
