# Definir un diccionario con las extensiones de archivo y sus tipos MIME correspondientes
tipos_mimetype = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

# Solicitar al usuario que ingrese el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Obtener la extensión del archivo
extension = nombre_archivo.lower().split(".")[-1]

# Obtener el tipo MIME correspondiente o "application/octet-stream" si no se encuentra en el diccionario
tipo_mimetype = tipos_mimetype.get(extension, "application/octet-stream")

# Mostrar el tipo MIME correspondiente
print("Tipo MIME:", tipo_mimetype)