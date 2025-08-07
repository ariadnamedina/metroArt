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
            

class Departamento:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f"Id: {self.id} - nombre departamento: {self.nombre}"
    
    

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
        
class Apiconexion:
    url = "https://collectionapi.metmuseum.org/public/collection/v1"

    def conexion_api(self, endpoint, params=None):
        url = f"{self.url}{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"No se conecto a la api {url}: {e}")
            return None

    def apartamentos_por_id(self, department_id):
        params = {"departmentId": department_id, "hasImages": "true"}
        datos = self.conexion_api("/objects", params=params)
        if datos and "objectIDs" in datos:
            return datos["objectIDs"]
        return []
    
    
    def apartamentos(self):
        departamento = self.conexion_api("/departments")
        if departamento and "departments" in departamento:
            lista_departamentos = []
            for dat in departamento["departments"]:
                nuevo_departamento = Departamento(
                    id=dat["departmentId"],
                    nombre=dat["displayName"]
                )
                lista_departamentos.append(nuevo_departamento)
            return lista_departamentos
        return []
    
    def detalle_obra(self, object_id):
        data = self.conexion_api(f"/objects/{object_id}")
        if data and data.get("objectID"):
            obra_de_arte = Obra(
                id=data["objectID"],
                titulo=data["title"],
                nombre_artista=data["artistDisplayName"],
                nacionalidad_artista=data["artistNationality"],
                fecha_nacimiento_artista=data["artistBeginDate"],
                fecha_muerte_artista=data["artistEndDate"],
                tipo=data["classification"],
                anio_creacion=data["objectDate"],
                departamento=data["department"],
                url_imagen=data["primaryImage"]
            )
            return obra_de_arte
        return None

    def objetos_id(self, query):
        params = {"q": query, "hasImages": "true"}
        dato = self.conexion_api("/search", params=params)
        if dato and "objectIDs" in dato:
            return dato["objectIDs"]
        return []

    


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
    api = Apiconexion()
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
        
class Apiconexion:
    url = "https://collectionapi.metmuseum.org/public/collection/v1"

    def conexion_api(self, endpoint, params=None):
        url = f"{self.url}{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"No se conecto a la api {url}: {e}")
            return None

    def apartamentos_por_id(self, department_id):
        params = {"departmentId": department_id, "hasImages": "true"}
        datos = self.conexion_api("/objects", params=params)
        if datos and "objectIDs" in datos:
            return datos["objectIDs"]
        return []
    
    
    def apartamentos(self):
        departamento = self.conexion_api("/departments")
        if departamento and "departments" in departamento:
            lista_departamentos = []
            for dat in departamento["departments"]:
                nuevo_departamento = Departamento(
                    id=dat["departmentId"],
                    nombre=dat["displayName"]
                )
                lista_departamentos.append(nuevo_departamento)
            return lista_departamentos
        return []
    
    def detalle_obra(self, object_id):
        data = self.conexion_api(f"/objects/{object_id}")
        if data and data.get("objectID"):
            obra_de_arte = Obra(
                id=data["objectID"],
                titulo=data["title"],
                nombre_artista=data["artistDisplayName"],
                nacionalidad_artista=data["artistNationality"],
                fecha_nacimiento_artista=data["artistBeginDate"],
                fecha_muerte_artista=data["artistEndDate"],
                tipo=data["classification"],
                anio_creacion=data["objectDate"],
                departamento=data["department"],
                url_imagen=data["primaryImage"]
            )
            return obra_de_arte
        return None

    def objetos_id(self, query):
        params = {"q": query, "hasImages": "true"}
        dato = self.conexion_api("/search", params=params)
        if dato and "objectIDs" in dato:
            return dato["objectIDs"]
        return []

    
        
        
def detalles_obra(dato):

    id_obra = int(input("por favor introduzca el id correspondiente "))
    
    print(f"\nEspere mientras busacamos la obra con id: {id_obra}")
    print("No apague ni desconecte el equipo")
    
    obra = dato.detalle_obra(id_obra)
    
    if obra:
        obra.mostrar_detalles()
        if obra.url_imagen:
            opcion_imagen = input("quiere ver la imagen: si/no ").lower()
            if opcion_imagen == 'si':
                nombre_archivo = guardar_imagen_desde_url(obra.url_imagen, f"obra_{id_obra}")
                if nombre_archivo:
                    abrir_imagen(nombre_archivo)
        else:
            print("No hay imagen para esta obra")
    else:
        print(f"No hay informacion para la obra con id:  {id_obra}.")

        
        
def mostrar_menu():
    print("--- MetroArt ---")
    print("1 Ver lista de obras")
    print("2 Mostrar detalles de una obra por ID")
    print("3. Salir")
    
def main():
    api = Apiconexion()
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
            detalles_obra(api)
        elif opcion == '3':
            print("Cerrando Programa")
            break
        else:
            print("Seleccione un valor del menu")
            
main()
