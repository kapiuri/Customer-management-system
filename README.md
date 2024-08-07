# Sistema de Gestión de Clientes

Este proyecto es un sistema simple de gestión de clientes en Python que permite agregar, eliminar, buscar y listar clientes. El sistema se basa en dos clases principales: `Cliente` y `GestionCliente`, y se ejecuta a través de un menú interactivo en la línea de comandos.

## Clases

### `Cliente`

La clase `Cliente` representa a un cliente con los siguientes atributos:

- `nombre`: El nombre del cliente.
- `correo`: El correo electrónico del cliente.
- `telefono`: El número de teléfono del cliente.

### `GestionCliente`

La clase `GestionCliente` gestiona una lista de clientes y proporciona métodos para realizar operaciones sobre esta lista.

## Uso

1. **Ejecuta el script** principal:

    ```bash
    python main.py
    ```

2. **Interfaz del Usuario**:
   - El menú principal ofrece las siguientes opciones:
     1. **Agregar un cliente**: Ingresa el nombre, correo y teléfono del cliente para agregarlo a la lista.
     2. **Eliminar un cliente**: Ingresa el nombre del cliente que deseas eliminar.
     3. **Buscar un cliente**: Ingresa el nombre del cliente que deseas buscar.
     4. **Listar todos los clientes**: Muestra una lista de todos los clientes en el sistema.
     5. **Salir**: Sale del sistema de gestión de clientes.

3. **Interacción**:
   - Después de seleccionar una opción del menú, sigue las instrucciones en pantalla para ingresar los datos necesarios o visualizar la información.

## Ejemplo

Al ejecutar el script, se presentará el menú interactivo. Puedes agregar un cliente con la opción 1, eliminar un cliente con la opción 2, buscar un cliente con la opción 3, listar todos los clientes con la opción 4 y salir del sistema con la opción 5.
