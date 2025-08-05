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
            
main()
