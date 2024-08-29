import json
from common.JsonReader import JsonReader

data = json.loads("template.json")  # Cargar el JSON como un diccionario

# Función para recorrer el JSON y encontrar coincidencias

def recorrer_json(data, path=""):
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            recorrer_json(value, new_path)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            new_path = f"{path}[{index}]"
            recorrer_json(item, new_path)
    else:
        pass
        # print(f"Ruta: {path}, Valor: {data}")

# Llamar a la función con tu diccionario JSON

# Buscar todos los campos que contengan "((sourceValue))"
search_value = "((sourceValue))"
indices = recorrer_json(data, search_value)
# print(indices)

# print(f"Índices con valor '{search_value}': {indices}")