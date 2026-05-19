import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()

ventana.title("Mi primera ventana")

# Tamaño
ancho = 800
alto = 600

# Centrar
pantalla_ancho = ventana.winfo_screenwidth()
pantalla_alto = ventana.winfo_screenheight()

x = int((pantalla_ancho / 2) - (ancho / 2))
y = int((pantalla_alto / 2) - (alto / 2))

ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
ventana.configure(bg="gray")

# ---------------- VALIDACIÓN SOLO NÚMEROS ----------------
def solo_numeros(char):
    return char.isdigit() or char == ""

validacion = ventana.register(solo_numeros)

# ---------------- VERIFICAR SI HAY DATOS ----------------
def hay_datos():
    return (
        entry_nombre.get().strip() != "" or
        entry_telefono.get().strip() != "" or
        entry_direccion.get().strip() != "" or
        entry_edad.get().strip() != ""
    )

# ---------------- SALIR (ESC o botón) ----------------
def confirmar_salida(event=None):

    if hay_datos():
        aviso = messagebox.askyesno(
            "Advertencia",
            "Hay datos escritos. ¿Está a punto de salir y borrar la información. ¿Desea continuar?"
        )
        if not aviso:
            return

    if messagebox.askyesno("Confirmar salida", "¿Desea salir?"):
        ventana.destroy()

# ---------------- CANCELAR ----------------
def confirmar_cancelacion():
    if messagebox.askyesno("Cancelar proceso", "¿Desea cancelar el proceso?"):
        messagebox.showinfo("Cancelado", "El proceso fue cancelado correctamente.")

# ---------------- CONFIRMAR DATOS ----------------
def confirmar_datos():
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()
    direccion = entry_direccion.get()
    edad = entry_edad.get()

    info = f"""
DATOS DEL USUARIO

Nombre: {nombre}
Teléfono: {telefono}
Dirección: {direccion}
Edad: {edad}
"""

    messagebox.showinfo("Información del usuario", info)

    volver = messagebox.askyesno("Continuar", "¿Desea volver?")
    if not volver:
        ventana.destroy()

# ESC activa salida
ventana.bind("<Escape>", confirmar_salida)

# ---------------- CONTENEDOR ----------------
frame = tk.Frame(ventana, bg="white", bd=2, relief="solid")
frame.pack(fill="both", expand=True, padx=20, pady=20)

titulo = tk.Label(
    frame,
    text="Sistema de Información UDI",
    bg="white",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=(20, 5))

subtitulo = tk.Label(
    frame,
    text="Formulario de registro de usuarios",
    bg="white",
    fg="gray20",
    font=("Arial", 12)
)
subtitulo.pack(pady=(0, 20))

# ---------------- FORMULARIO ----------------
form = tk.Frame(frame, bg="white")
form.pack()

tk.Label(form, text="NOMBRE Y APELLIDO:", bg="white").grid(row=0, column=0, sticky="e", padx=10, pady=8)
entry_nombre = tk.Entry(form, width=35)
entry_nombre.grid(row=0, column=1)

tk.Label(form, text="TELÉFONO:", bg="white").grid(row=1, column=0, sticky="e", padx=10, pady=8)
entry_telefono = tk.Entry(form, width=35, validate="key", validatecommand=(validacion, "%S"))
entry_telefono.grid(row=1, column=1)

tk.Label(form, text="DIRECCIÓN:", bg="white").grid(row=2, column=0, sticky="e", padx=10, pady=8)
entry_direccion = tk.Entry(form, width=35)
entry_direccion.grid(row=2, column=1)

tk.Label(form, text="EDAD:", bg="white").grid(row=3, column=0, sticky="e", padx=10, pady=8)
entry_edad = tk.Entry(form, width=35, validate="key", validatecommand=(validacion, "%S"))
entry_edad.grid(row=3, column=1)

# ---------------- BOTÓN CONFIRMAR ----------------
btn_confirmar = tk.Button(
    frame,
    text="Confirmar datos",
    width=20,
    command=confirmar_datos
)
btn_confirmar.pack(pady=20)

# ---------------- BOTONES INFERIORES ----------------
btn_cancelar = tk.Button(frame, text="Cancelar", width=12, command=confirmar_cancelacion)
btn_cancelar.place(relx=0.02, rely=0.95, anchor="sw")

btn_salir = tk.Button(frame, text="Salir", width=12, command=confirmar_salida)
btn_salir.place(relx=0.98, rely=0.95, anchor="se")

ventana.mainloop()