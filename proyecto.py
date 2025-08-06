import requests
from PIL import Image
class Departamento:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f"Id: {self.id} - nombre departamento: {self.nombre}"
    
    
def guardar_imagen_desde_url(url, nombre_archivo):
    """
    Descarga una imagen desde una URL y la guarda en un archivo.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Lanza una excepción para códigos de estado de error (4xx o 5xx)
        
        content_type = response.headers.get('Content-Type')
        extension = '.png'  # Valor por defecto
        if content_type:
            if 'image/png' in content_type:
                extension = '.png'
            elif 'image/jpeg' in content_type:
                extension = '.jpg'
            elif 'image/svg+xml' in content_type:
                extension = '.svg'
        
        nombre_archivo_final = f"{nombre_archivo}{extension}"
        with open(nombre_archivo_final, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"Imagen guardada exitosamente como '{nombre_archivo_final}'")
        return nombre_archivo_final
    
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer el request: {e}")
    except IOError as e:
        print(f"Error al escribir el archivo: {e}")
    return None

def abrir_imagen(archivo):

    img = Image.open(archivo)
    img.show()

class Obra:
    def __init__(self, id, titulo, nombre_artista, nacionalidad_artista,
                 fecha_nacimiento_artista, fecha_muerte_artista,
                 tipo, anio_creacion, departamento,url_imagen):
        self.id = id
        self.titulo = titulo
        self.nombre_artista = nombre_artista
        self.nacionalidad_artista = nacionalidad_artista
        self.fecha_nacimiento_artista = fecha_nacimiento_artista
        self.fecha_muerte_artista = fecha_muerte_artista
        self.tipo = tipo
        self.anio_creacion = anio_creacion
        self.departamento = departamento
        self.url_imagen = url_imagen
        

    def __str__(self):
        return (f"Id: {self.id}\n"
                f"Título de obra: {self.titulo}\n"
                f"Artista de la obra: {self.nombre_artista}\n"
                f"Departamento: {self.departamento}")

    def mostrar_detalles(self):
        print("\n------ Detalles de la Obra de arte  -------")
        print(f"Id: {self.id}")
        print(f"Título: {self.titulo}")
        print(f"Artista: {self.nombre_artista}")
        print(f"Nacionalidad: {self.nacionalidad_artista}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento_artista}")
        print(f"Fecha de muerte: {self.fecha_muerte_artista}")
        print(f"Departamento: {self.departamento}")
        print(f"Tipo: {self.tipo}")
        print(f"Año de creación: {self.anio_creacion}")
        print(f"URL de la imagen: {self.url_imagen}")
        
        
def mostrar_menu():
    print("--- MetroArt ---")
    print("1 Ver lista de obras")
    print("2 Mostrar detalles de una obra por ID")
    print("3. Salir")
    
def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            print("1. Ver lista de obras por Departamento")
            print("2. Ver lista de obras por Nacionalidad del Autor")
            print("3. Ver lista de obras por Nombre del Autor")
            print("4. Regresar menu anterior")
            
            opcion2 = input("Ingrese una opción: ")
            if opcion2 == '1':
                print("")
            elif opcion2 == '2':
                print("")
            elif opcion2 == '3':
                print("")
            elif opcion2 == '4':
                mostrar_menu()
            else:
                print("Seleccione un valor del menu")   
        elif opcion == '2':
            print("")
        elif opcion == '3':
            print("Cerrando Programa")
            break
        else:
            print("Seleccione un valor del menu")
            
main()
