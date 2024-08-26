import tkinter as tk


class CGuiMenu:
    def __init__(self, config):
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

        # Labels y TextBoxes para tableName, shortTableName y separator
        self.label_tablename = tk.Label(self.root, text="Table Name")
        self.text_tablename = tk.Text(self.root, height=1, width=str(int(int(config["textbox_width"])/5))

        self.label_shorttablename = tk.Label(self.root, text="Short Table Name")
        self.text_shorttablename = tk.Text(self.root, height=1, width=str(int(int(config["textbox_width"])/5)))

        self.label_separator = tk.Label(self.root, text="Separator")
        self.text_separator = tk.Text(self.root, height=1, width=str(int(int(config["textbox_width"])/5)))
        self.text_separator.insert("1.0", ",")  # Valor por defecto "," para separator

        # Colocar los elementos en la grid
        self.label_tablename.grid(row=0, column=0, padx=5, pady=5)
        self.text_tablename.grid(row=0, column=1, padx=5, pady=5)

        self.label_shorttablename.grid(row=0, column=2, padx=5, pady=5)
        self.text_shorttablename.grid(row=0, column=3, padx=5, pady=5)

        self.label_separator.grid(row=0, column=4, padx=5, pady=5)
        self.text_separator.grid(row=0, column=5, padx=5, pady=5)

        # TextBoxes adicionales
        self.text_box1 = tk.Text(self.root, height=config["textbox_height"], width=config["textbox_width"])
        self.text_box2 = tk.Text(self.root, height=config["textbox_height"], width=config["textbox_width"])

        self.text_box1.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.text_box2.grid(row=1, column=3, columnspan=3, padx=10, pady=10)

        # Botón de copiar
        self.boton_copiar = tk.Button(self.root, text=config["button_text"])

        # Ubicar el botón en la ventana
        self.boton_copiar.grid(row=2, column=0, columnspan=6, pady=10)
        

    def ejecutar(self):
        # Ejecutar el bucle principal de la ventana
        self.root.mainloop()