
import tkinter as tk
import json


class JsonReader():
    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            self.config = json.load(f)
    
    def getStr(self):
        # print (self.config)
        return self.config


        	
	