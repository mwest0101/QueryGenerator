import tkinter as tk


class CGuiMenu:
    def __init__(self, config):
        self.root = tk.Tk()
        self.root.title(config["window_title"])

        self.text_box1 = tk.Text(self.root, height=config["textbox_height"], width=config["textbox_width"])
        self.text_box2 = tk.Text(self.root, height=config["textbox_height"], width=config["textbox_width"])

        self.text_box1.grid(row=0, column=0, padx=10, pady=10)
        self.text_box2.grid(row=0, column=1, padx=10, pady=10)


        self.boton_copiar = tk.Button(self.root, text=config["button_text"])

        # Ubicar el botón en la ventana
        self.boton_copiar.grid(row=1, column=0, columnspan=2, pady=10)

    def ejecutar(self):
        # Ejecutar el bucle principal de la ventana
        self.root.mainloop()