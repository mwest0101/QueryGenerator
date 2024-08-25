
import tkinter as tk
import json
class SnakeToCamel():
    def __init__(self):
        self.inStr=""
        self.inArray=[]
        self.outArray=[]
        
    def snakeToCamelCase(self,snake_str):
        self.inStr = snake_str    
        components = snake_str.split('_')
        self.inArray = components
        return components[0] + ''.join(x.capitalize() for x in components[1:])

    def convert(self,inStr):
        self.inStr = inStr
        self.inArray = inStr.split(',')
        self.outArray=[self.snakeToCamelCase(snake_str) for snake_str in self.inArray]
        return self.outArray
    
    
    def getInStr(self):
        return self.inStr
    
    def getInArray(self):
        return self.inArray
    
    def getOutArray(self):
        return self.outArray
    
    def getOutStr(self):
        return ', '.join(self.outArray)
        





