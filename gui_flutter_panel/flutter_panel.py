
import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("flutter panel - by Edwin Saul")

# Crear el ntbook
ntbook = ttk.Notebook(ventana)

# ntbook 1
ntbook1 = ttk.Frame(ntbook)
ntbook.add(ntbook1, text="project code")

# Etiquetas en ntbook 1
label1_1 = tk.Label(ntbook1, text="Etiqueta 1")
label1_1.pack()

label1_2 = tk.Label(ntbook1, text="Etiqueta 2")
label1_2.pack()

label1_3 = tk.Label(ntbook1, text="Etiqueta 3")
label1_3.pack()

# ntbook 2
ntbook2 = ttk.Frame(ntbook)
ntbook.add(ntbook2, text="run debug")

# Etiquetas en ntbook 2
label2_1 = tk.Label(ntbook2, text="Etiqueta 4")
label2_1.pack()

label2_2 = tk.Label(ntbook2, text="Etiqueta 5")
label2_2.pack()

label2_3 = tk.Label(ntbook2, text="Etiqueta 6")
label2_3.pack()

# ntbook 3
ntbook3 = ttk.Frame(ntbook)
ntbook.add(ntbook3, text="export")

# Etiquetas en ntbook 3
label3_1 = tk.Label(ntbook3, text="Etiqueta 7")
label3_1.pack()

label3_2 = tk.Label(ntbook3, text="Etiqueta 8")
label3_2.pack()

label3_3 = tk.Label(ntbook3, text="Etiqueta 9")
label3_3.pack()

# Mostrar el ntbook
ntbook4 = ttk.Frame(ntbook)
ntbook.add(ntbook4, text="config panel")


ntbook.pack(expand=1, fill="both")

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
