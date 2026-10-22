import tkinter as tk
from tkinter import ttk, messagebox
import math

class FiguraGeometrica:
    """Clase base abstracta para las figuras."""
    def calcular_volumen(self):
        raise NotImplementedError("Debe implementarse en la subclase")
    
    def calcular_superficie(self):
        raise NotImplementedError("Debe implementarse en la subclase")


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
        area_base = math.pow(self.base, 2)
        return (1/3) * area_base * self.altura
        
    def calcular_superficie(self):
        area_base = math.pow(self.base, 2)
        area_lateral = 4 * ((self.base * self.apotema) / 2) 
        return area_base + area_lateral



class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Figuras Geométricas - Ejercicio 8.3")
        self.geometry("450x400")
        self.resizable(False, False)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True, fill="both", padx=10)

        self.crear_pestana_cilindro()
        self.crear_pestana_esfera()
        self.crear_pestana_piramide()

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

        ttk.Button(frame, text="Calcular Cilindro", command=self.calcular_cilindro).grid(row=2, column=0, columnspan=2, pady=15)

        ttk.Label(frame, text="Volumen:").grid(row=3, column=0, sticky="e")
        ttk.Label(frame, textvariable=self.cil_res_vol, font=("Arial", 10, "bold")).grid(row=3, column=1, sticky="w")
        
        ttk.Label(frame, text="Superficie:").grid(row=4, column=0, sticky="e")
        ttk.Label(frame, textvariable=self.cil_res_sup, font=("Arial", 10, "bold")).grid(row=4, column=1, sticky="w")

    def calcular_cilindro(self):
        try:
            r = float(self.cil_radio.get())
            h = float(self.cil_altura.get())
            figura = Cilindro(r, h)
            
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

        ttk.Button(frame, text="Calcular Esfera", command=self.calcular_esfera).grid(row=1, column=0, columnspan=2, pady=15)

        ttk.Label(frame, text="Volumen:").grid(row=2, column=0, sticky="e")
        ttk.Label(frame, textvariable=self.esf_res_vol, font=("Arial", 10, "bold")).grid(row=2, column=1, sticky="w")
        
        ttk.Label(frame, text="Superficie:").grid(row=3, column=0, sticky="e")
        ttk.Label(frame, textvariable=self.esf_res_sup, font=("Arial", 10, "bold")).grid(row=3, column=1, sticky="w")

    def calcular_esfera(self):
        try:
            r = float(self.esf_radio.get())
            figura = Esfera(r)
            
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

        ttk.Label(frame, text="Lado de la base (cm):").grid(row=0, column=0, pady=5, padx=10, sticky="e")
        ttk.Entry(frame, textvariable=self.pir_base).grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Altura de la pirámide (cm):").grid(row=1, column=0, pady=5, padx=10, sticky="e")
        ttk.Entry(frame, textvariable=self.pir_altura).grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Apotema (cm):").grid(row=2, column=0, pady=5, padx=10, sticky="e")
        ttk.Entry(frame, textvariable=self.pir_apotema).grid(row=2, column=1, pady=5)

        ttk.Button(frame, text="Calcular Pirámide", command=self.calcular_piramide).grid(row=3, column=0, columnspan=2, pady=15)

        ttk.Label(frame, text="Volumen:").grid(row=4, column=0, sticky="e")
        ttk.Label(frame, textvariable=self.pir_res_vol, font=("Arial", 10, "bold")).grid(row=4, column=1, sticky="w")
        
        ttk.Label(frame, text="Superficie:").grid(row=5, column=0, sticky="e")
        ttk.Label(frame, textvariable=self.pir_res_sup, font=("Arial", 10, "bold")).grid(row=5, column=1, sticky="w")

    def calcular_piramide(self):
        try:
            b = float(self.pir_base.get())
            h = float(self.pir_altura.get())
            ap = float(self.pir_apotema.get())
            figura = Piramide(b, h, ap)
            
            self.pir_res_vol.set(f"{figura.calcular_volumen():.2f} cm³")
            self.pir_res_sup.set(f"{figura.calcular_superficie():.2f} cm²")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()