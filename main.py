
import json
import tkinter as tk
from common.JsonReader import JsonReader
from common.SnakeToCamel import SnakeToCamel
from common.EventManager import EventManager
from common.GetConfiguration import GetConfiguration
from gui.CGuiMenu import CGuiMenu



# Llamar a la función con tu diccionario JSON

# Clase principal que inicializa y coordina las otras clases
class mainApp:
    def __init__(self, template_file='template.json'):
        self.jr=JsonReader('config.json')
        self.tp=JsonReader(template_file)
        self.gc=GetConfiguration(self.tp)
        dictTp=self.tp.getStr()
        # self.gc.showConfiguration()

        self.config=self.jr.getStr()

        # self.gc.loadLangaujes()
        
        self.gui = CGuiMenu(self.config,self.gc)
        self.eventos = EventManager(self.gui,self.gc)
        self.gui.boton_copiar.config(command=self.eventos.convertText)
        

    def ejecutar(self):
        self.gui.ejecutar()


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