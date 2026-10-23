import tkinter as tk
from tkinter import ttk, messagebox
import math
import os

class FiguraGeometrica:
    def calcular_volumen(self):
        raise NotImplementedError
    
    def calcular_superficie(self):
        raise NotImplementedError

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
        
    def calcular_volumen(self):
        return math.pi * math.pow(self.radio, 2) * self.altura
        
    def calcular_superficie(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_volumen(self):
        return (4/3) * math.pi * math.pow(self.radio, 3)
        
    def calcular_superficie(self):
        return 4 * math.pi * math.pow(self.radio, 2)

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        self.base = base 
        self.altura = altura
        self.apotema = apotema 
        
    def calcular_volumen(self):
        return (1/3) * math.pow(self.base, 2) * self.altura
        
    def calcular_superficie(self):
        area_base = math.pow(self.base, 2)
        area_lateral = 4 * ((self.base * self.apotema) / 2) 
        return area_base + area_lateral

class Cubo(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado
        
    def calcular_volumen(self):
        return math.pow(self.lado, 3)
        
    def calcular_superficie(self):
        return 6 * math.pow(self.lado, 2)

class Prisma(FiguraGeometrica):
    def __init__(self, largo, ancho, altura):
        self.largo = largo
        self.ancho = ancho
        self.altura = altura
        
    def calcular_volumen(self):
        return self.largo * self.ancho * self.altura
        
    def calcular_superficie(self):
        return 2 * (self.largo * self.ancho + self.largo * self.altura + self.ancho * self.altura)


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Figuras Geométricas - Ejercicio 8.3")
        self.geometry("650x400")
        self.resizable(False, False)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True, fill="both", padx=10)

        self.crear_pestana_cilindro()
        self.crear_pestana_esfera()
        self.crear_pestana_piramide()
        self.crear_pestana_cubo()
        self.crear_pestana_prisma()

    def cargar_imagen(self, frame, filename):
        if os.path.exists(filename):
            img = tk.PhotoImage(file=filename).subsample(2, 2)
            lbl = ttk.Label(frame, image=img)
            lbl.image = img 
            lbl.grid(row=0, column=2, rowspan=6, padx=20)
        else:
            ttk.Label(frame, text="[Sin Imagen]").grid(row=0, column=2, rowspan=6, padx=20)

    def crear_pestana_cilindro(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Cilindro")
        self.cil_radio = tk.StringVar()
        self.cil_altura = tk.StringVar()
        self.cil_res_vol = tk.StringVar(value="---")
        self.cil_res_sup = tk.StringVar(value="---")

        ttk.Label(frame, text="Radio (cm):").grid(row=0, column=0, pady=10, padx=10, sticky="e")
        ttk.Entry(frame, textvariable=self.cil_radio).grid(row=0, column=1, pady=10)
        ttk.Label(frame, text="Altura (cm):").grid(row=1, column=0, pady=10, padx=10, sticky="e")
        ttk.Entry(frame, textvariable=self.cil_altura).grid(row=1, column=1, pady=10)
        ttk.Button(frame, text="Calcular", command=self.calcular_cilindro).grid(row=2, column=0, columnspan=2, pady=15)
        ttk.Label(frame, text="Volumen:").grid(row=3, column=0, sticky="e")
        ttk.Label(frame, textvariable=self.cil_res_vol, font=("Arial", 10, "bold")).grid(row=3, column=1, sticky="w")
        ttk.Label(frame, text="Superficie:").grid(row=4, column=0, sticky="e")
        ttk.Label(frame, textvariable=self.cil_res_sup, font=("Arial", 10, "bold")).grid(row=4, column=1, sticky="w")
        
        self.cargar_imagen(frame, "cilindro.png")

    def calcular_cilindro(self):
        try:
            figura = Cilindro(float(self.cil_radio.get()), float(self.cil_altura.get()))
            self.cil_res_vol.set(f"{figura.calcular_volumen():.2f} cm³")
            self.cil_res_sup.set(f"{figura.calcular_superficie():.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

    def crear_pestana_esfera(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Esfera")
        self.esf_radio = tk.StringVar()
        self.esf_res_vol = tk.StringVar(value="---")
        self.esf_res_sup = tk.StringVar(value="---")

        ttk.Label(frame, text="Radio (cm):").grid(row=0, column=0, pady=10, padx=10, sticky="e")
        ttk.Entry(frame, textvariable=self.esf_radio).grid(row=0, column=1, pady=10)
        ttk.Button(frame, text="Calcular", command=self.calcular_esfera).grid(row=1, column=0, columnspan=2, pady=15)
        ttk.Label(frame, text="Volumen:").grid(row=2, column=0, sticky="e")
        ttk.Label(frame, textvariable=self.esf_res_vol, font=("Arial", 10, "bold")).grid(row=2, column=1, sticky="w")
        ttk.Label(frame, text="Superficie:").grid(row=3, column=0, sticky="e")
        ttk.Label(frame, textvariable=self.esf_res_sup, font=("Arial", 10, "bold")).grid(row=3, column=1, sticky="w")
        
        self.cargar_imagen(frame, "esfera.png")

    def calcular_esfera(self):
        try:
            figura = Esfera(float(self.esf_radio.get()))
            self.esf_res_vol.set(f"{figura.calcular_volumen():.2f} cm³")
            self.esf_res_sup.set(f"{figura.calcular_superficie():.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

    def crear_pestana_piramide(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Pirámide")
        self.pir_base = tk.StringVar()
        self.pir_altura = tk.StringVar()
        self.pir_apotema = tk.StringVar()
        self.pir_res_vol = tk.StringVar(value="---")
        self.pir_res_sup = tk.StringVar(value="---")

        ttk.Label(frame, text="Base (cm):").grid(row=0, column=0, pady=5, padx=10, sticky="e")
        ttk.Entry(frame, textvariable=self.pir_base).grid(row=0, column=1, pady=5)
        ttk.Label(frame, text="Altura (cm):").grid(row=1, column=0, pady=5, padx=10, sticky="e")
        ttk.Entry(frame, textvariable=self.pir_altura).grid(row=1, column=1, pady=5)
        ttk.Label(frame, text="Apotema (cm):").grid(row=2, column=0, pady=5, padx=10, sticky="e")
        ttk.Entry(frame, textvariable=self.pir_apotema).grid(row=2, column=1, pady=5)
        ttk.Button(frame, text="Calcular", command=self.calcular_piramide).grid(row=3, column=0, columnspan=2, pady=15)
        ttk.Label(frame, text="Volumen:").grid(row=4, column=0, sticky="e")
        ttk.Label(frame, textvariable=self.pir_res_vol, font=("Arial", 10, "bold")).grid(row=4, column=1, sticky="w")
        ttk.Label(frame, text="Superficie:").grid(row=5, column=0, sticky="e")
        ttk.Label(frame, textvariable=self.pir_res_sup, font=("Arial", 10, "bold")).grid(row=5, column=1, sticky="w")
        
        self.cargar_imagen(frame, "piramide.png")

    def calcular_piramide(self):
        try:
            figura = Piramide(float(self.pir_base.get()), float(self.pir_altura.get()), float(self.pir_apotema.get()))
            self.pir_res_vol.set(f"{figura.calcular_volumen():.2f} cm³")
            self.pir_res_sup.set(f"{figura.calcular_superficie():.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

    def crear_pestana_cubo(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Cubo")
        self.cub_lado = tk.StringVar()
        self.cub_res_vol = tk.StringVar(value="---")
        self.cub_res_sup = tk.StringVar(value="---")

        ttk.Label(frame, text="Lado (cm):").grid(row=0, column=0, pady=10, padx=10, sticky="e")
        ttk.Entry(frame, textvariable=self.cub_lado).grid(row=0, column=1, pady=10)
        ttk.Button(frame, text="Calcular", command=self.calcular_cubo).grid(row=1, column=0, columnspan=2, pady=15)
        ttk.Label(frame, text="Volumen:").grid(row=2, column=0, sticky="e")
        ttk.Label(frame, textvariable=self.cub_res_vol, font=("Arial", 10, "bold")).grid(row=2, column=1, sticky="w")
        ttk.Label(frame, text="Superficie:").grid(row=3, column=0, sticky="e")
        ttk.Label(frame, textvariable=self.cub_res_sup, font=("Arial", 10, "bold")).grid(row=3, column=1, sticky="w")
        
        self.cargar_imagen(frame, "cubo.png")

    def calcular_cubo(self):
        try:
            figura = Cubo(float(self.cub_lado.get()))
            self.cub_res_vol.set(f"{figura.calcular_volumen():.2f} cm³")
            self.cub_res_sup.set(f"{figura.calcular_superficie():.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

    def crear_pestana_prisma(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Prisma")
        self.pris_largo = tk.StringVar()
        self.pris_ancho = tk.StringVar()
        self.pris_altura = tk.StringVar()
        self.pris_res_vol = tk.StringVar(value="---")
        self.pris_res_sup = tk.StringVar(value="---")

        ttk.Label(frame, text="Largo (cm):").grid(row=0, column=0, pady=5, padx=10, sticky="e")
        ttk.Entry(frame, textvariable=self.pris_largo).grid(row=0, column=1, pady=5)
        ttk.Label(frame, text="Ancho (cm):").grid(row=1, column=0, pady=5, padx=10, sticky="e")
        ttk.Entry(frame, textvariable=self.pris_ancho).grid(row=1, column=1, pady=5)
        ttk.Label(frame, text="Altura (cm):").grid(row=2, column=0, pady=5, padx=10, sticky="e")
        ttk.Entry(frame, textvariable=self.pris_altura).grid(row=2, column=1, pady=5)
        ttk.Button(frame, text="Calcular", command=self.calcular_prisma).grid(row=3, column=0, columnspan=2, pady=15)
        ttk.Label(frame, text="Volumen:").grid(row=4, column=0, sticky="e")
        ttk.Label(frame, textvariable=self.pris_res_vol, font=("Arial", 10, "bold")).grid(row=4, column=1, sticky="w")
        ttk.Label(frame, text="Superficie:").grid(row=5, column=0, sticky="e")
        ttk.Label(frame, textvariable=self.pris_res_sup, font=("Arial", 10, "bold")).grid(row=5, column=1, sticky="w")
        
        self.cargar_imagen(frame, "prisma.png")

    def calcular_prisma(self):
        try:
            figura = Prisma(float(self.pris_largo.get()), float(self.pris_ancho.get()), float(self.pris_altura.get()))
            self.pris_res_vol.set(f"{figura.calcular_volumen():.2f} cm³")
            self.pris_res_sup.set(f"{figura.calcular_superficie():.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
