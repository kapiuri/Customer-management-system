# Clase para los datos de un cliente
class Cliente:
    def __init__(self, nombre, correo, telefono):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    # Mostrar los datos pon pantalla
    def __str__(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo}, Teléfono: {self.telefono}"


# Clase para gestionar clientes
class GestionCliente:
    # Inicializa la lista de clientes vacía
    def __init__(self):
        self.clientes = []

    # Agrega un cliente a la lista
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nombre} agregado al sistema.")

    # Elimina un cliente por nombre
    def borrar_cliente(self, nombre):
        for i, cliente in enumerate(self.clientes):
            if cliente.nombre == nombre:
                del self.clientes[i]
                print(f"Cliente {nombre} eliminado del sistema.")
                return
        print(f"Cliente {nombre} no encontrado.")

    # Busca un cliente por nombre
    def buscar_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                return cliente
        print(f"Cliente {nombre} no encontrado.")
        return None

    # Listar todos los clientes
    def listar_clientes(self):
        if self.clientes:
            for cliente in self.clientes:
                print(cliente)

    # Mensaje al salir del sistema
    def salir(self):
        print("Saliendo del sistema de gestión de clientes.")

    # Menu de opciones
    def menu(self):
        while True:
            print("-------------------------------")
            print("Sistema de Gestión de Clientes")
            print("-------------------------------")
            print("1. Agregar un cliente")
            print("2. Eliminar un cliente")
            print("3. Buscar un cliente")
            print("4. Listar todos los clientes")
            print("5. Salir")
            print("-------------------------------")
            opcion = input("Seleccione una opción: ")

            # Opcion 1 para agregar clientes
            if opcion == "1":
                nombre = input("Ingrese el nombre del cliente: ")
                correo = input("Ingrese el email del cliente: ")
                telefono = input("Ingrese el teléfono del cliente: ")
                cliente = Cliente(nombre, correo, telefono)
                self.agregar_cliente(cliente)

            # Opcion 2 para borrar clientes
            elif opcion == "2":
                nombre = input("Ingrese el nombre del cliente a eliminar: ")
                self.borrar_cliente(nombre)

            # Opcion 3 para buscar clientes
            elif opcion == "3":
                nombre = input("Ingrese el nombre del cliente a buscar: ")
                cliente = self.buscar_cliente(nombre)
                if cliente:
                    print("Cliente encontrado:")
                    print(cliente)

            # Opcion 4 para listar clientes
            elif opcion == "4":
                self.listar_clientes()

            # Opcion 5 para salir del sistema
            elif opcion == "5":
                self.salir()
                break

# Ejercutar el script
if __name__ == "__main__":
    sistema = GestionCliente()
    sistema.menu()
