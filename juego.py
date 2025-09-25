import tkinter as tk
import random

# Variables globales
ingreso = 1500000
deuda_total = 0
ronda = 0
credito_actual = {}

# Función para generar un crédito aleatorio
def generar_credito():
    global credito_actual, ronda
    ronda += 1
    monto = random.randint(500000, 2000000)
    tasa = random.choice([0.02, 0.03, 0.05])  # 2%, 3% o 5% mensual
    meses = random.choice([6, 12, 24])
    cuota = (monto * (1 + tasa * meses)) / meses

    credito_actual = {
        "monto": monto,
        "tasa": tasa,
        "meses": meses,
        "cuota": cuota
    }

    texto = (
        f"📌 Ronda {ronda}\n\n"
        f"💰 Crédito ofrecido: ${monto:,} COP\n"
        f"📊 Tasa: {tasa*100}% mensual\n"
        f"⏳ Plazo: {meses} meses\n"
        f"➡️ Cuota mensual: ${int(cuota):,} COP\n\n"
        "¿Aceptas este crédito?"
    )
    etiqueta.config(text=texto)

# Función cuando el jugador acepta un crédito
def aceptar():
    global deuda_total
    deuda_total += credito_actual["cuota"]
    if deuda_total > ingreso * 0.4:
        etiqueta.config(text="⚠️ Estás sobreendeudado (más del 40% de tu ingreso en deudas).\n\nJuego terminado.")
        boton_aceptar.config(state="disabled")
        boton_rechazar.config(state="disabled")
    else:
        generar_credito()

# Función cuando el jugador rechaza un crédito
def rechazar():
    if ronda >= 3:
        fin_del_juego()
    else:
        generar_credito()

# Función para finalizar el juego
def fin_del_juego():
    resultado = (
        f"🎯 Juego terminado.\n\n"
        f"Deuda mensual total: ${int(deuda_total):,} COP\n"
        f"Ingreso mensual: ${ingreso:,} COP\n\n"
    )
    if deuda_total <= ingreso * 0.4:
        resultado += "👏 ¡Felicitaciones! Has manejado bien tus finanzas."
    else:
        resultado += "😢 Te sobreendeudaste. Necesitas mejorar tu educación financiera."

    etiqueta.config(text=resultado)
    boton_aceptar.config(state="disabled")
    boton_rechazar.config(state="disabled")

# Interfaz gráfica con Tkinter
ventana = tk.Tk()
ventana.title("Juego: ¿Puedes evitar el sobreendeudamiento?")
ventana.geometry("500x400")

etiqueta = tk.Label(ventana, text="", font=("Arial", 12), wraplength=450, justify="left")
etiqueta.pack(pady=20)

boton_aceptar = tk.Button(ventana, text="✅ Aceptar crédito", command=aceptar, font=("Arial", 12))
boton_aceptar.pack(side="left", padx=50)

boton_rechazar = tk.Button(ventana, text="❌ Rechazar crédito", command=rechazar, font=("Arial", 12))
boton_rechazar.pack(side="right", padx=50)

# Iniciar primera ronda
generar_credito()

ventana.mainloop()
