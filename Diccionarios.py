# Crear un diccionario llamado informacion_personal con datos ficticios
informacion_personal = {
    "nombre": "Cristiano Ronaldo",  # Nombre de la persona
    "edad": 39,                     # Edad de la persona
    "ciudad": "Funchal",            # Ciudad de residencia
    "profesion": "Futbolista"       # Profesión de la persona
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
print("Ciudad antes de la modificación:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Turín"  # Modificando la ciudad
print("Ciudad después de la modificación:", informacion_personal["ciudad"])

# Agregar una nueva clave-valor para la "profesion" de la persona
# (En este caso se modificará el valor existente)
informacion_personal["profesion"] = "Delantero"  # Actualizando la profesión

# Verificar existencia de la clave "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "987-654-321"  # Agregando un número de teléfono ficticio

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminando la edad

# Imprimir el diccionario resultante
print("Diccionario final:", informacion_personal)
