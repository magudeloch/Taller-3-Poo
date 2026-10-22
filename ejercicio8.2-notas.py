import tkinter as tk
from tkinter import messagebox
import math

class Notas:
    def __init__(self, lista_notas=None):
        if lista_notas is None:
            self.listaNotas = []
        else:
            self.listaNotas = lista_notas

    def calcular_promedio(self):
        if not self.listaNotas: return 0
        suma = sum(self.listaNotas)
        return suma / len(self.listaNotas)

    def calcular_desviacion(self):
        if not self.listaNotas: return 0
        prom = self.calcular_promedio()
        suma = 0
        for nota in self.listaNotas:
            suma += math.pow(nota - prom, 2)
        return math.sqrt(suma / len(self.listaNotas))

    def calcular_menor(self):
        if not self.listaNotas: return 0
        return min(self.listaNotas)

    def calcular_mayor(self):
        if not self.listaNotas: return 0
        return max(self.listaNotas)

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Ejercicio 8.2 - Componentes Swing en Python")
        self.geometry("400x550")
        self.resizable(False, False)
        
        self.campos_notas = []
        
        self.crear_componentes()

    def crear_componentes(self):
        tk.Label(self, text="Ingrese las 5 notas del estudiante:", font=("Arial", 12, "bold")).pack(pady=10)
        
        frame_inputs = tk.Frame(self)
        frame_inputs.pack(pady=10)
        
        for i in range(5):
            lbl = tk.Label(frame_inputs, text=f"Nota {i+1}: ")
            lbl.grid(row=i, column=0, pady=5, sticky="e")
            entry = tk.Entry(frame_inputs, width=15)
            entry.grid(row=i, column=1, pady=5)
            self.campos_notas.append(entry)
            
        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=15)
        
        btn_calcular = tk.Button(frame_botones, text="Calcular", command=self.realizar_calculos, bg="#a0e0a0")
        btn_calcular.grid(row=0, column=0, padx=10)
        
        btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=self.limpiar_campos, bg="#f0a0a0")
        btn_limpiar.grid(row=0, column=1, padx=10)
        
        tk.Frame(self, height=2, bd=1, relief="sunken").pack(fill="x", padx=20, pady=10)
        
        frame_resultados = tk.Frame(self)
        frame_resultados.pack(pady=10)
        
        self.var_promedio = tk.StringVar(value="---")
        self.var_desviacion = tk.StringVar(value="---")
        self.var_mayor = tk.StringVar(value="---")
        self.var_menor = tk.StringVar(value="---")
        
        tk.Label(frame_resultados, text="Promedio:").grid(row=0, column=0, sticky="e", pady=5)
        tk.Label(frame_resultados, textvariable=self.var_promedio, font=("Arial", 10, "bold")).grid(row=0, column=1, sticky="w", padx=10)
        
        tk.Label(frame_resultados, text="Desviación Estándar:").grid(row=1, column=0, sticky="e", pady=5)
        tk.Label(frame_resultados, textvariable=self.var_desviacion, font=("Arial", 10, "bold")).grid(row=1, column=1, sticky="w", padx=10)
        
        tk.Label(frame_resultados, text="Nota Mayor:").grid(row=2, column=0, sticky="e", pady=5)
        tk.Label(frame_resultados, textvariable=self.var_mayor, font=("Arial", 10, "bold")).grid(row=2, column=1, sticky="w", padx=10)
        
        tk.Label(frame_resultados, text="Nota Menor:").grid(row=3, column=0, sticky="e", pady=5)
        tk.Label(frame_resultados, textvariable=self.var_menor, font=("Arial", 10, "bold")).grid(row=3, column=1, sticky="w", padx=10)

    def realizar_calculos(self):
        lista_notas = []
        try:
            for entry in self.campos_notas:
                valor_texto = entry.get().strip()
                if valor_texto == "":
                    raise ValueError("Campo vacío")
                nota = float(valor_texto)
                lista_notas.append(nota)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos en todas las casillas.")
            return

        objeto_notas = Notas(lista_notas)
        
        prom = objeto_notas.calcular_promedio()
        desv = objeto_notas.calcular_desviacion()
        mayor = objeto_notas.calcular_mayor()
        menor = objeto_notas.calcular_menor()

        self.var_promedio.set(f"{prom:.2f}")
        self.var_desviacion.set(f"{desv:.2f}")
        self.var_mayor.set(f"{mayor:.2f}")
        self.var_menor.set(f"{menor:.2f}")

    def limpiar_campos(self):
        for entry in self.campos_notas:
            entry.delete(0, tk.END)
        
        self.var_promedio.set("---")
        self.var_desviacion.set("---")
        self.var_mayor.set("---")
        self.var_menor.set("---")

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()