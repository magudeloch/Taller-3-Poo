# Actividad - Interfaces Gráficas y Gestión de Eventos en Python
## 📚 Información académica

- **Universidad:** Universidad Nacional de Colombia
- **Actividad:** Desarrollo de GUIs y Eventos en Python (Adaptación de Swing)
- **Estudiante:** Mateo Agudelo Chica
- **Docente:** Walter Hugo Arboleda Mazo
- **Asignatura:** Programación Orientada a Objetos
- **Semestre:** 2026-2S

---

## 📝 Ejercicios

| # | Descripción |
|---|-------------|
| **Ejercicio 8.2** | **Componentes gráficos:** Desarrollo de un programa con interfaz de usuario (Tkinter) que solicita el ingreso de cinco notas para calcular y mostrar el promedio, la desviación estándar, la mayor y la menor nota. |
| **Ejercicio 8.3** | **Gestión de eventos:** Creación de una jerarquía de clases geométricas (Cilindro, Esfera, Pirámide) y desarrollo de una interfaz gráfica estructurada en pestañas para calcular el volumen y la superficie de cada figura basándose en los eventos de interacción del usuario. |



%%{init: {'theme': 'base', 'themeVariables': { 'background': '#ffffff', 'primaryTextColor': '#000000', 'primaryColor': '#f0f0f0', 'lineColor': '#000000'}}}%%
classDiagram
    class Notas {
        -lista_notas : list~float~
        +calcular_promedio() float
        +calcular_desviacion() float
        +calcular_mayor() float
        +calcular_menor() float
    }

    class VentanaPrincipal {
        -campos_notas : list
        +crear_componentes()
        +realizar_calculos()
        +limpiar_campos()
    }

    VentanaPrincipal ..> Notas : Instancia
