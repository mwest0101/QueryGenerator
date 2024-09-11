import tkinter as tk
from tkinter import *
from tkinter import ttk
from common.SnakeToCamel import SnakeToCamel

class CGuiMenu:
	def __init__(self, gc):
		self.root = tk.Tk()
		self.root.title("QueryGenerator")
		self.selected_templates_value=""
		self.selected_databases_value=""
		self.selected_functions_value=""
		self.field1=""
		self.gc=gc
		self.stc = SnakeToCamel()
		self.scroll = Scrollbar(self.root, orient=HORIZONTAL)
		# Configuración del grid para que se expanda y ocupe todo el ancho
		for i in range(7):
			self.root.grid_columnconfigure(i, weight=1)

		# Labels y TextBoxes para tableName, shortTableName y separator
		self.state_isFieldId = tk.BooleanVar(value=True)
		
		# self.check_isFieldId = tk.Checkbutton(self.root, text = "Music", variable = self.estado_checkbox, onvalue = 1, offvalue = 0, height=5, width = 20, command=self.leer_estado_checkbox)
		self.check_isFieldId=tk.Checkbutton(self.root,text="Is first id?", variable=self.state_isFieldId)
  
		self.label_fieldId = tk.Label(self.root, text="id")
		self.text_fieldId = tk.Text(self.root, height=1, width=15)
		self.text_fieldId.insert(1.0, self.gc.dictTp["global"]["ifNoDefinedId"]["id"]) 

		self.label_fieldVid = tk.Label(self.root, text="vId")
		self.text_fieldVid = tk.Text(self.root, height=1, width=15)
		self.text_fieldVid.insert(1.0, self.gc.dictTp["global"]["ifNoDefinedId"]["vId"]) 
  
		self.label_tablename = tk.Label(self.root, text="Table Name")
		self.text_tablename = tk.Text(self.root, height=1, width=15)
		self.text_tablename.insert(1.0, self.gc.dictTp["global"]["defaults"]["defaultBigTableName"]) 

		self.label_shorttablename = tk.Label(self.root, text="Short Table Name")
		self.text_shorttablename = tk.Text(self.root, height=1, width=15)
		self.text_shorttablename.insert(1.0, self.gc.dictTp["global"]["defaults"]["defaultSmaTableName"])

		self.label_separator = tk.Label(self.root, text="Separator")
		self.text_separator = tk.Text(self.root, height=1, width=10)
		self.text_separator.insert("1.0", self.gc.dictTp["global"]["defaults"]["sep"])  # Valor por defecto "," para separator
  
		self.boton_salir = tk.Button(self.root, text="Salir")
		# Ubicar el botón en la ventana
		

		# Colocar los elementos en la grid
		# self.label_isFieldId.grid		(row=0, 	column=0, 	padx=1, 	pady=5, 	sticky="ew")
		self.check_isFieldId.grid		(row=1, 	column=0, 	padx=1, 	pady=0, 	sticky="ew")		
  
		self.label_fieldId.grid			(row=0, 	column=1, 	padx=1, 	pady=5, 	sticky="ew")
		self.text_fieldId.grid			(row=1, 	column=1, 	padx=1, 	pady=0, 	sticky="ew")

		self.label_fieldVid.grid		(row=0, 	column=2, 	padx=1, 	pady=5, 	sticky="ew")
		self.text_fieldVid.grid			(row=1, 	column=2, 	padx=1, 	pady=0, 	sticky="ew")

		self.label_tablename.grid		(row=0, 	column=3, 	padx=1, 	pady=5, 	sticky="ew")
		self.text_tablename.grid		(row=1, 	column=3, 	padx=1, 	pady=0, 	sticky="ew")

		self.label_shorttablename.grid	(row=0, 	column=4, 	padx=1, 	pady=5, 	sticky="ew")
		self.text_shorttablename.grid	(row=1, 	column=4, 	padx=1, 	pady=0, 	sticky="ew")

		self.label_separator.grid		(row=0, 	column=5, 	padx=1, 	pady=5, 	sticky="ew")
		self.text_separator.grid		(row=1, 	column=5, 	padx=1, 	pady=0,		sticky="ew")

		self.boton_salir.grid			(row=0, 	column=6, 	padx=1, 	pady=0, 	sticky="ew")
		# TextBoxes adicionales
		self.text_box1 = tk.Text(self.root, height=20, width=40, yscrollcommand=self.scroll.set)
		self.loadTextBox1()
		self.text_box1.bind('<KeyRelease>', self.on_text_box1_change)
  
		self.text_box2 = tk.Text(self.root, height=20, width=60, yscrollcommand=self.scroll.set)		
  
		self.text_box1.grid(row=2, column=0, columnspan=2, padx=10, pady=30, sticky="ew")  		  
		self.text_box2.grid(row=2, column=2, columnspan=6, padx=10, pady=30, sticky="ew")

		# Combobox para seleccionar el lenguaje de programación
		self.label_templates = tk.Label(self.root, text="templates")
		aTemplates = self.gc.loadLangaujes()
		self.combobox_templates = ttk.Combobox(self.root, values=aTemplates)
		self.combobox_templates.current(0)  # Seleccionar por defecto el primer elemento
		self.selected_templates_value=aTemplates[0] 
  
		self.combobox_templates.bind('<<ComboboxSelected>>', self.on_combobox_templates_change)


		# Combobox para seleccionar la base de datos
		self.label_databases = tk.Label(self.root, text="Database")
		aDatabases = self.gc.loadDatabases(aTemplates[0])
		self.combobox_databases = ttk.Combobox(self.root, values=aDatabases)
		self.combobox_databases.current(0)  # Seleccionar por defecto el primer elemento
		self.selected_databases_value=aDatabases[0]
  
    
		self.combobox_databases.bind('<<ComboboxSelected>>', self.on_combobox_databases_change)

		# Combobox para seleccionar la función
		self.label_function = tk.Label(self.root, text="Function")
		aFunctions = self.gc.loadFunctions(aTemplates[0], aDatabases[0])
		self.combobox_functions = ttk.Combobox(self.root, values=aFunctions)
		self.combobox_functions.current(0)  # Seleccionar por defecto el primer elemento
		self.selected_functions_value=aFunctions[0]
  
		self.combobox_functions.bind('<<ComboboxSelected>>', self.on_combobox_functions_change)
  
		# Colocar los combobox en la grid
		self.label_templates.grid(row=3, column=0, padx=0, pady=5, sticky="es")
		self.combobox_templates.grid(row=3, column=1, padx=2, pady=5, sticky="es")

		self.label_databases.grid(row=3, column=2, padx=0, pady=5, sticky="es")
		self.combobox_databases.grid(row=3, column=3, padx=2, pady=5, sticky="es")
		        
		self.label_function.grid(row=3, column=4, padx=0, pady=5, sticky="es")
		self.combobox_functions.grid(row=3, column=5, padx=2, pady=5, sticky="es")

		# Botón de copiar
		self.boton_copiar = tk.Button(self.root, text="Convert")

		# Ubicar el botón en la ventana
		self.boton_copiar.grid(row=3, column=6, padx=10, pady=5, sticky="es")

	# def leer_estado_checkbox(self):
	# 	estado = self.estado_checkbox.get()  # Obtiene el valor de la variable de control
	# 	if estado:
	# 		print("El checkbox está activo.")
	# 	else:
	# 		print("El checkbox está deshabilitado.")
          
	def loadTextBox1(self):
		text=self.gc.dictTp["global"]["defaults"]["defaultFields"]
		# print("[["+text+"]]")
		strResult=""
		cont=0
		self.field1=""
		
		if "," in text:
			array=text.split(",")
		if "\n" in text:
			array=text.split("\n")
			
		if "," in text or "\n" in text:
			for value in array:
				if(cont==0):
					self.field1=value
				tempText=value+"\n"
				strResult+=tempText
				cont+=1
			strResult=strResult[:-1]
		else:
			strResult+=value
		if(self.state_isFieldId.get()==True):
			self.text_fieldId.delete("1.0", tk.END)
			self.text_fieldId.insert('end',self.field1)
			
  
		self.text_box1.insert('end',strResult)
		return strResult


        
	def loadTextBox2(self):
		text=self.text_box1.get("1.0", tk.END)
    
		strResult=""
		cont=0
		self.field1=""
		if "," in text:
			array=text.split(",")
		if "\n" in text:
			array=text.split("\n")
			
		if "," in text or "\n" in text:

			for value in array:
				if(cont==0):
					self.field1=value
				tempText=value+"\n"
				strResult+=tempText
				cont+=1
			strResult=strResult[:-1]
		else:
			strResult+=value
		if(self.state_isFieldId.get()==True):
			self.text_fieldId.delete("1.0", tk.END)
			self.text_fieldId.insert('end',self.field1)
			self.text_fieldVid.delete("1.0", tk.END)
			self.text_fieldVid.insert('end',self.stc.snakeToCamelCase(self.field1))
			
			
  
		# self.text_box1.insert('end',strResult)
		return strResult

	def on_combobox_templates_change(self,event):
		self.selected_templates_value = self.combobox_templates.get()
		# print(self.selected_templates_value," - ",self.selected_databases_value)
		self.combobox_databases['values']=self.gc.loadDatabases(self.selected_templates_value) # asigna valores a combobox
		self.combobox_databases.current(0)
  
		self.selected_databases_value = self.combobox_databases.get()
		self.combobox_functions['values']=self.gc.loadFunctions(self.selected_templates_value,self.selected_databases_value)
		
		self.combobox_functions.current(0)
		# print(f"Has seleccionado: {selected_value}")
	
	def on_combobox_databases_change(self,event):
		self.selected_databases_value = self.combobox_databases.get()
		self.combobox_functions['values']=self.gc.loadFunctions(self.selected_templates_value,self.selected_databases_value)
		self.combobox_functions.current(0)
		# print(f"Has seleccionado: {selected_value}")	
 
	def on_combobox_functions_change(self,event):
		self.selected_functions_value = self.combobox_functions.get()
		# print(f"Has seleccionado: {self.selected_functions_value}")	
	
	def on_text_box1_change(self,event):
		
		# print("pase")
		self.loadTextBox2()
  
	def ejecutar(self):
		# Ejecutar el bucle principal de la ventana
		self.root.mainloop()