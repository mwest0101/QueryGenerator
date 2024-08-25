
import json
import tkinter as tk
from common.JsonReader import JsonReader
from common.SnakeToCamel import SnakeToCamel
from common.EventManager import EventManager
from gui.CGuiMenu import CGuiMenu


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
        print(f"Ruta: {path}, Valor: {data}")

# Llamar a la función con tu diccionario JSON

# Clase principal que inicializa y coordina las otras clases
class mainApp:
    def __init__(self, template_file='template.json'):
        jr=JsonReader('config.json')
        tp=JsonReader(template_file)
        
        
        self.config=jr.getStr()
        self.tp=tp.getStr()
        # print(self.tp)
        recorrer_json(self.tp)
        print(self.tp["global"]["sets"]["key"])
        
        # for item in self.tp:
        #     if isinstance(item, dict):
        #         for key, value in item.items():
        #             print(f'Clave: {key}, Valor: {value}')
        #     else:
        #         print(f'El item no es un diccionario, es de tipo {type(item)}: {item}')
        # Recorrer cada clave y valor en el diccionario
        
        
        
        self.interfaz = CGuiMenu(self.config)
        self.eventos = EventManager(self.interfaz.text_box1, self.interfaz.text_box2)
        self.interfaz.boton_copiar.config(command=self.eventos.convertText)

    def ejecutar(self):
        self.interfaz.ejecutar()


# Ejecutar la aplicación
if __name__ == "__main__":
    app = mainApp()    
    app.ejecutar()
    stc = SnakeToCamel()
    
    # input_list = ['package_data_name','package_data_description','package_data_short_descript','package_data_pvp',
    # 'package_data_ean_code','package_data_external_code','package_data_pax','web_data_permalink','web_data_virtual',
    # 'web_data_nights','web_data_residences','audit_trial_user_id','audit_trial_created_at','audit_trial_updated_at',
    # 'audit_trial_deleted','audit_trial_deleted_at','audit_trial_active']

    # output_list = stc.convert(input_list)
    # print(output_list)