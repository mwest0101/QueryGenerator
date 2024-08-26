from common.SnakeToCamel import SnakeToCamel
import tkinter as tk

class EventManager:
    def __init__(self, gui,gc):
        self.gui = gui
        # self.text_box2 = text_box2
        self.inText=""
        self.outText=""
        self.gc=gc

    def convertText(self):
        stc = SnakeToCamel()
        self.inText = self.gui.text_box1.get("1.0", tk.END)          
        self.outText=""          
        self.gui.text_box2.delete("1.0", tk.END)       
        self.inArray = self.inText.split(',')                   
        self.outArray=stc.convert(self.inArray)#             
        
        # print(self.outArray)        
        self.outText=stc.getOutStr()   
        # print(inText)/
        self.gc.getConfAndParams(self.gui,self.inArray,self.outArray)

        
        
        self.gc.showConfiguration()
            
        # self.dictTp["global"]["sets"]["keys"]="test"                        
        self.gui.text_box2.insert(tk.END, self.outText)     
              
   
        
        
    def copiar_texto(self):
        inText = self.text_box1.get("1.0", tk.END)       # Obtener todo el texto del primer Text box
        self.text_box2.delete("1.0", tk.END)            # Limpiar el segundo Text box
        self.text_box2.insert(tk.END, inText) 