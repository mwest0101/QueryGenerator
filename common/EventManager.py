from common.SnakeToCamel import SnakeToCamel
import tkinter as tk

class EventManager:
    def __init__(self, text_box1, text_box2):
        self.text_box1 = text_box1
        self.text_box2 = text_box2

    def convertText(self):
        stc = SnakeToCamel()
        
        inText = self.text_box1.get("1.0", tk.END)            
        self.text_box2.delete("1.0", tk.END)          
        
        arrResult=stc.convert(inText)#     
        print(arrResult)
        
        inText=stc.getOutStr()   
        print(inText)
        
        self.text_box2.insert(tk.END, inText)           
        
    def copiar_texto(self):
        inText = self.text_box1.get("1.0", tk.END)       # Obtener todo el texto del primer Text box
        self.text_box2.delete("1.0", tk.END)            # Limpiar el segundo Text box
        self.text_box2.insert(tk.END, inText) 