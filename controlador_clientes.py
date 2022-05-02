from bd import obtener_conexion


def insertar_cliente(nombre, cantidad, precio, descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO cliente(nombre, cantidad, precio, descripcion) VALUES (%s, %s, %s, %s)",
                       (nombre, cantidad, precio, descripcion))
    conexion.commit()
    conexion.close()


def obtener_clientes():
    conexion = obtener_conexion()
    clientes = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, cantidad, precio, descripcion FROM cliente")
        clientes = cursor.fetchall()
    conexion.close()
    return clientes


def eliminar_cliente(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM cliente WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_cliente_por_id(id):
    conexion = obtener_conexion()
    cliente = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, nombre, cantidad, precio, descripcion FROM cliente WHERE id = %s", (id,))
        cliente = cursor.fetchone()
    conexion.close()
    return cliente


def actualizar_cliente(nombre, cantidad, precio, descripcion, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE cliente SET nombre = %s, cantidad = %s, precio = %s, descripcion = %s WHERE id = %s",
                       (nombre, cantidad, precio, descripcion, id))
    conexion.commit()
    conexion.close()