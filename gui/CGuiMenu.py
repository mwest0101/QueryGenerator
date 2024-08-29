import tkinter as tk
from tkinter import ttk

class CGuiMenu:
	def __init__(self, config,gc):
		self.root = tk.Tk()
		self.root.title(config["window_title"])
		self.selected_templates_value=""
		self.selected_databases_value=""
		self.selected_function_value=""
  
		self.gc=gc
		# Configuración del grid para que se expanda y ocupe todo el ancho
		for i in range(7):
			self.root.grid_columnconfigure(i, weight=1)

		# Labels y TextBoxes para tableName, shortTableName y separator
		self.label_tablename = tk.Label(self.root, text="Table Name")
		self.text_tablename = tk.Text(self.root, height=1, width=15)

		self.label_shorttablename = tk.Label(self.root, text="Short Table Name")
		self.text_shorttablename = tk.Text(self.root, height=1, width=15)

		self.label_separator = tk.Label(self.root, text="Separator")
		self.text_separator = tk.Text(self.root, height=1, width=10)
		self.text_separator.insert("1.0", ",")  # Valor por defecto "," para separator
  
		self.boton_salir = tk.Button(self.root, text="Salir")
		# Ubicar el botón en la ventana
		

		# Colocar los elementos en la grid
		self.label_tablename.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
		self.text_tablename.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

		self.label_shorttablename.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
		self.text_shorttablename.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

		self.label_separator.grid(row=0, column=4, padx=5, pady=5, sticky="ew")
		self.text_separator.grid(row=0, column=5, padx=5, pady=10, sticky="ew")

		self.boton_salir.grid(row=0, column=6, padx=10, pady=5, sticky="ew")
		# TextBoxes adicionales
		self.text_box1 = tk.Text(self.root, height=20, width=50)
		self.text_box2 = tk.Text(self.root, height=20, width=50)

		self.text_box1.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
		self.text_box2.grid(row=1, column=3, columnspan=3, padx=10, pady=10, sticky="ew")

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
		self.selected_function_value=aFunctions[0]
		self.combobox_functions.bind('<<ComboboxSelected>>', self.on_combobox_functions_change)
  
		# Colocar los combobox en la grid
		self.label_templates.grid(row=2, column=0, padx=0, pady=5, sticky="ew")
		self.combobox_templates.grid(row=2, column=1, padx=2, pady=5, sticky="ew")

		self.label_databases.grid(row=2, column=2, padx=0, pady=5, sticky="ew")
		self.combobox_databases.grid(row=2, column=3, padx=2, pady=5, sticky="ew")
		        
		self.label_function.grid(row=2, column=4, padx=0, pady=5, sticky="ew")
		self.combobox_functions.grid(row=2, column=5, padx=2, pady=5, sticky="ew")

		# Botón de copiar
		self.boton_copiar = tk.Button(self.root, text=config["button_text"])

		# Ubicar el botón en la ventana
		self.boton_copiar.grid(row=2, column=6, padx=10, pady=5, sticky="ew")


	def on_combobox_templates_change(self,event):
		self.selected_templates_value = self.combobox_templates.get()
		# print(self.selected_templates_value," - ",self.selected_databases_value)
		self.combobox_databases['values']=self.gc.loadDatabases(self.selected_templates_value)
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
		selected_value = self.combobox_functions.get()
		# print(f"Has seleccionado: {selected_value}")	
	
	def ejecutar(self):
		# Ejecutar el bucle principal de la ventana
		self.root.mainloop()