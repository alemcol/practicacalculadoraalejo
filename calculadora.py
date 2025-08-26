import tkinter as tk

# Variables globales para el cálculo
expresion_actual = ""
resultado_final = ""

def manejar_clic(valor):
    """
    Función que se ejecuta cuando se presiona un botón de la calculadora.
    """
    global expresion_actual
    global resultado_final

    # Si se presiona el botón "C" (Clear), limpia todo
    if valor == "C":
        expresion_actual = ""
        resultado_final = ""
        campo_texto.delete(0, tk.END)
        campo_texto.insert(0, "")

    # Si se presiona el botón "="
    elif valor == "=":
        try:
            resultado_final = str(eval(expresion_actual))
            campo_texto.delete(0, tk.END)
            campo_texto.insert(0, resultado_final)
            expresion_actual = resultado_final
        except Exception:
            campo_texto.delete(0, tk.END)
            campo_texto.insert(0, "Error")
            expresion_actual = ""

    # Si se presiona un número u operador (+, -, *, /)
    else:
        expresion_actual += valor
        campo_texto.delete(0, tk.END)
        campo_texto.insert(0, expresion_actual)

# ----------------- Configuración de la Ventana Principal -----------------
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x350")
ventana.resizable(False, False)

# ----------------- Crear la Pantalla de la Calculadora -----------------
campo_texto = tk.Entry(ventana, width=20, borderwidth=5, font=("Arial", 16))
campo_texto.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# ----------------- Crear los Botones de la Calculadora -----------------
# Lista de los botones a crear, en un orden para el teclado
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Crea los botones en un bucle y los coloca en la ventana
fila = 1
columna = 0
for boton_valor in botones:
    # Crea un botón
    boton = tk.Button(ventana, text=boton_valor, padx=20, pady=20, font=("Arial", 12),
                      command=lambda valor=boton_valor: manejar_clic(valor))
    
    # Coloca el botón en la cuadrícula
    boton.grid(row=fila, column=columna, padx=5, pady=5)
    
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# ----------------- Iniciar la Aplicación -----------------
ventana.mainloop()