"""
Hecho por
Simon Parra Arango
Cesar García Marín
Cindy Campuzano Montes
"""

import re # Importamos la libreria para expresiones regulares

class EmailManager:
    def __init__(self):
        self.emails = {} 

    def _validar_email(self, email):
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" #Expresion regular para validar los componentes del correo
        return re.match(patron, email) is not None
    

# Funcion para registrar correos
    def registrar_email(self, email):
        if not self._validar_email(email):
            print("Error: La dirección de correo electrónico no tiene un formato válido.")
            return False

# Se piden las validaciones para saber si estudiante o docente
        if email.endswith("@estudiante.utv.edu.co"):
            tipo = 'estudiante'
        elif email.endswith("@utv.edu.co"):
            tipo = 'docente'
        else:
            print("Error: El dominio del correo no corresponde a un estudiante ni a un docente.") 
            return False

        if email in self.emails:
            print(f"Advertencia: La dirección de correo electrónico '{email}' ya está registrada.")
            return False

        self.emails[email] = tipo
        print(f"Correo electrónico '{email}' registrado como {tipo}.")
        return True

# Funcion para poder listar
    def listar_emails(self, tipo=None):
        if not self.emails:
            print("No hay direcciones de correo electrónico registradas.")
            return

        if tipo:
            print(f"\n--- Correos electrónicos de {tipo.capitalize()} ---")
            encontrados = False
            for email, t in self.emails.items():
                if t == tipo.lower():
                    print(f"- {email}")
                    encontrados = True
            if not encontrados:
                print(f"No se encontraron direcciones de correo electrónico de {tipo.lower()}.")
        else:
            print("\n--- Todas las direcciones de correo electrónico ---")
            for email, tipo in self.emails.items():
                print(f"- {email} ({tipo.capitalize()})")

# Funcion para eliminar correos de la lista
    def eliminar_email(self, email):
        if email in self.emails:
            del self.emails[email]
            print(f"Correo electrónico '{email}' eliminado.")
            return True
        else:
            print(f"Error: La dirección de correo electrónico '{email}' no está registrada.")
            return False

# Busqueda de correo sin necesidad de completar todo el campo de correo
    def buscar_emails(self, nombre_parcial):
        resultados = []
        nombre_parcial_lower = nombre_parcial.lower()
        for email, tipo in self.emails.items():
            if nombre_parcial_lower in email.lower():
                resultados.append((email, tipo))

        if resultados:
            print(f"\n--- Resultados de la búsqueda para '{nombre_parcial}' ---")
            for email, tipo in resultados:
                print(f"- {email} ({tipo.capitalize()})")
        else:
            print(f"No se encontraron correos electrónicos que contengan '{nombre_parcial}'.")

# Menú amigable en consola
def mostrar_menu():
    
    print("")
    print("\n--- Administración de Correos Electrónicos ---")
    print("")
    print("      1. Registrar correo electrónico")
    print("      2. Listar correos electrónicos")
    print("      3. Eliminar correo electrónico")
    print("      4. Buscar correos electrónicos por nombre parcial")
    print("      5. Salir")
    print("")
    
# Funcion principal
def main():
    manager = EmailManager()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            email = input("Ingrese la dirección de correo electrónico: ")
            manager.registrar_email(email)
        elif opcion == '2':
            listar_por_tipo = input("¿Desea listar por tipo? (s/n): ").lower()
            if listar_por_tipo == 's':
                tipo_listar = input("Ingrese el tipo (estudiante/docente): ")
                manager.listar_emails(tipo_listar)
            else:
                manager.listar_emails()
        elif opcion == '3':
            email_eliminar = input("Ingrese la dirección de correo electrónico a eliminar: ")
            manager.eliminar_email(email_eliminar)
        elif opcion == '4':
            nombre_buscar = input("Ingrese el nombre parcial a buscar en los correos: ")
            manager.buscar_emails(nombre_buscar)
        elif opcion == '5':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
