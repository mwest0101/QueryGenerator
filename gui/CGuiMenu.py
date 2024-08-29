import tkinter as tk
from tkinter import ttk

class CGuiMenu:
    def __init__(self, config,gc):
        # self.root = tk.Tk()
        # self.root.title(config["window_title"])

		# self.text_box1 = tk.Text(self.root, height=config["textbox_height"], width=config["textbox_width"])
		# self.text_box1 = tk.Text(self.root, height=config["textbox_height"], width=config["textbox_width"])
        # self.text_box1 = tk.Text(self.root, height=config["textbox_height"], width=config["textbox_width"])
        # self.text_box2 = tk.Text(self.root, height=config["textbox_height"], width=config["textbox_width"])

        # self.text_box1.grid(row=0, column=0, padx=10, pady=10)
        # self.text_box2.grid(row=0, column=1, padx=10, pady=10)


        # self.boton_copiar = tk.Button(self.root, text=config["button_text"])

        # # Ubicar el botón en la ventana
        # self.boton_copiar.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.root = tk.Tk()
        self.root.title(config["window_title"])

        # Configuración del grid para que se expanda y ocupe todo el ancho
        for i in range(7):
            self.root.grid_columnconfigure(i, weight=1)

        # Labels y TextBoxes para tableName, shortTableName y separator
        self.label_tablename = tk.Label(self.root, text="Table Name")
        self.text_tablename = tk.Text(self.root, height=1, width=20)

        self.label_shorttablename = tk.Label(self.root, text="Short Table Name")
        self.text_shorttablename = tk.Text(self.root, height=1, width=20)

        self.label_separator = tk.Label(self.root, text="Separator")
        self.text_separator = tk.Text(self.root, height=1, width=20)
        self.text_separator.insert("1.0", ",")  # Valor por defecto "," para separator

        # Colocar los elementos en la grid
        self.label_tablename.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.text_tablename.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

        self.label_shorttablename.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        self.text_shorttablename.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

        self.label_separator.grid(row=0, column=4, padx=5, pady=5, sticky="ew")
        self.text_separator.grid(row=0, column=5, padx=5, pady=10, sticky="ew")

        # TextBoxes adicionales
        self.text_box1 = tk.Text(self.root, height=20, width=50)
        self.text_box2 = tk.Text(self.root, height=20, width=50)

        self.text_box1.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
        self.text_box2.grid(row=1, column=4, columnspan=4, padx=10, pady=10, sticky="ew")

        # Combobox para seleccionar el lenguaje de programación
        self.label_language = tk.Label(self.root, text="Language")
        aLangaujes = gc.loadLangaujes()
        self.combobox_language = ttk.Combobox(self.root, values=aLangaujes)
        self.combobox_language.current(0)  # Seleccionar por defecto el primer elemento

        # Combobox para seleccionar la base de datos
        self.label_database = tk.Label(self.root, text="Database")
        aDatabases = gc.loadDatabases(aLangaujes[0])
        self.combobox_database = ttk.Combobox(self.root, values=aDatabases)
        self.combobox_database.current(0)  # Seleccionar por defecto el primer elemento

        # Combobox para seleccionar la función
        self.label_function = tk.Label(self.root, text="Function")
        aFunctions = gc.loadFunctions(aLangaujes[0], aDatabases[0])
        self.combobox_function = ttk.Combobox(self.root, values=aFunctions)
        self.combobox_function.current(0)  # Seleccionar por defecto el primer elemento

        # Colocar los combobox en la grid
        self.label_language.grid(row=2, column=0, padx=0, pady=5, sticky="ew")
        self.combobox_language.grid(row=2, column=1, padx=2, pady=5, sticky="ew")

        self.label_database.grid(row=2, column=2, padx=0, pady=5, sticky="ew")
        self.combobox_database.grid(row=2, column=3, padx=2, pady=5, sticky="ew")
        
        self.label_function.grid(row=2, column=4, padx=0, pady=5, sticky="ew")
        self.combobox_function.grid(row=2, column=5, padx=2, pady=5, sticky="ew")

        # Botón de copiar
        self.boton_copiar = tk.Button(self.root, text=config["button_text"])

        # Ubicar el botón en la ventana
        self.boton_copiar.grid(row=2, column=6, padx=10, pady=5, sticky="ew")

        
        

    def ejecutar(self):
        # Ejecutar el bucle principal de la ventana
        self.root.mainloop()