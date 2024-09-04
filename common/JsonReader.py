
import tkinter as tk
import json


class JsonReader():
    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            self.config = json.load(f)
        

    def getStr(self):
        # print (self.config)
        return self.config

    def recorrer_json(self,data, path=""):
        if isinstance(data, dict):
            
            for key, value in data.items():
                new_path = f"{path}.{key}" if path else key
                self.recorrer_json(value, new_path)
                
        elif isinstance(data, list):
            
            for index, item in enumerate(data):
                new_path = f"{path}[{index}]"
                self.recorrer_json(item, new_path)
        else:
            #print(f"Ruta: {path}, Valor: {data}")
            pass

	