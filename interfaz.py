import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time


class BibliotecaApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Sistema de Biblioteca")
        self.root.geometry("1000x750")
        self.root.configure(bg="#f2f2f2")

        self.fecha_actual = time.strftime("%d/%m/%Y")
        self.datos = []

        self.root.bind("<Escape>", self.salir)

        self.interfaz()

    # ---------------- INTERFAZ ----------------

    def interfaz(self):

        header = tk.Frame(self.root, bg="#f2f2f2")
        header.pack(fill="x", pady=10, padx=10)

        tk.Label(
            header,
            text="SISTEMA DE GESTIÓN DE BIBLIOTECA UDI",
            font=("Arial", 20, "bold"),
            bg="#f2f2f2"
        ).pack(side="left")

        # LOGO (opcional)
        try:
            self.logo = tk.PhotoImage(file="logo.png")
            self.logo = self.logo.subsample(2, 2)
            tk.Label(header, image=self.logo, bg="#f2f2f2").pack(side="right")
        except:
            pass

        self.contenedor = tk.Frame(self.root, bg="#f2f2f2")
        self.contenedor.pack(fill="both", expand=True, padx=30, pady=10)

        self.formulario()
        self.botones_superiores()
        self.tabla()
        self.botones_inferiores()

    # ---------------- FORMULARIO ----------------

    def formulario(self):

        frame = tk.Frame(self.contenedor, bg="#f2f2f2")
        frame.pack(anchor="w", pady=15, padx=10)

        tk.Label(frame, text="FECHA", bg="#f2f2f2").grid(row=0, column=0, sticky="w", pady=8)
        tk.Label(frame, text=self.fecha_actual, bg="white", width=18, relief="solid")\
            .grid(row=0, column=1, pady=8, padx=10)

        tk.Label(frame, text="ID", bg="#f2f2f2").grid(row=1, column=0, sticky="w", pady=8)
        self.entry_id = tk.Entry(frame, width=45)
        self.entry_id.grid(row=1, column=1, pady=8, padx=10)

        tk.Label(frame, text="NOMBRE", bg="#f2f2f2").grid(row=2, column=0, sticky="w", pady=8)
        self.entry_nombre = tk.Entry(frame, width=45)
        self.entry_nombre.grid(row=2, column=1, pady=8, padx=10)

        tk.Label(frame, text="EDITORIAL", bg="#f2f2f2").grid(row=3, column=0, sticky="w", pady=8)
        self.entry_editorial = tk.Entry(frame, width=45)
        self.entry_editorial.grid(row=3, column=1, pady=8, padx=10)

        tk.Label(frame, text="AUTOR", bg="#f2f2f2").grid(row=4, column=0, sticky="w", pady=8)
        self.entry_autor = tk.Entry(frame, width=45)
        self.entry_autor.grid(row=4, column=1, pady=8, padx=10)

        tk.Label(frame, text="COPIAS", bg="#f2f2f2").grid(row=5, column=0, sticky="w", pady=8)
        self.entry_copias = tk.Entry(frame, width=15)
        self.entry_copias.grid(row=5, column=1, sticky="w", pady=8, padx=10)

    # ---------------- BOTONES ----------------

    def botones_superiores(self):

        frame = tk.Frame(self.contenedor, bg="#f2f2f2")
        frame.pack(anchor="w", pady=10, padx=10)

        tk.Button(frame, text="Nuevo", width=14, command=self.nuevo).grid(row=0, column=0, padx=8)
        tk.Button(frame, text="Guardar", width=14, command=self.guardar).grid(row=0, column=1, padx=8)
        tk.Button(frame, text="Editar", width=14, command=self.editar).grid(row=0, column=2, padx=8)
        tk.Button(frame, text="Eliminar", width=14, command=self.eliminar).grid(row=0, column=3, padx=8)

    # ---------------- TABLA ----------------

    def tabla(self):

        self.frame_tabla = tk.Frame(self.contenedor)
        self.frame_tabla.pack(anchor="w", pady=10, padx=10)

        columnas = ("id", "nombre", "editorial", "autor", "copias", "fecha")

        self.tree = ttk.Treeview(self.frame_tabla, columns=columnas, show="headings", height=10)

        for col in columnas:
            self.tree.heading(col, text=col.upper())
            self.tree.column(col, width=140)

        self.tree.pack()

        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_registro)

    # ---------------- BLOQUEO FORMULARIO ----------------

    def bloquear_formulario(self, estado=True):

        estado_widget = "disabled" if estado else "normal"

        self.entry_nombre.config(state=estado_widget)
        self.entry_editorial.config(state=estado_widget)
        self.entry_autor.config(state=estado_widget)
        self.entry_copias.config(state=estado_widget)

    # ---------------- SELECCIÓN ----------------

    def seleccionar_registro(self, event):

        sel = self.tree.focus()
        if not sel:
            return

        v = self.tree.item(sel, "values")

        self.entry_id.config(state="normal")
        self.entry_id.delete(0, tk.END)
        self.entry_id.insert(0, v[0])
        self.entry_id.config(state="readonly")

        self.entry_nombre.delete(0, tk.END)
        self.entry_nombre.insert(0, v[1])

        self.entry_editorial.delete(0, tk.END)
        self.entry_editorial.insert(0, v[2])

        self.entry_autor.delete(0, tk.END)
        self.entry_autor.insert(0, v[3])

        self.entry_copias.delete(0, tk.END)
        self.entry_copias.insert(0, v[4])

        self.bloquear_formulario(True)

    # ---------------- LIMPIAR ----------------

    def limpiar_formulario(self):

        self.entry_id.config(state="normal")

        for e in [
            self.entry_id,
            self.entry_nombre,
            self.entry_editorial,
            self.entry_autor,
            self.entry_copias
        ]:
            e.delete(0, tk.END)

        self.bloquear_formulario(False)

    # ---------------- NUEVO ----------------

    def nuevo(self):
        self.limpiar_formulario()
        self.entry_id.focus()

    # ---------------- GUARDAR ----------------

    def guardar(self):

        if any(e.get().strip() == "" for e in
               [self.entry_id, self.entry_nombre, self.entry_editorial,
                self.entry_autor, self.entry_copias]):
            messagebox.showwarning("Campos vacíos", "Complete todos los campos")
            return

        datos = (
            self.entry_id.get(),
            self.entry_nombre.get(),
            self.entry_editorial.get(),
            self.entry_autor.get(),
            self.entry_copias.get(),
            self.fecha_actual
        )

        # actualizar si existe ID
        for i, d in enumerate(self.datos):
            if d[0] == datos[0]:
                self.datos[i] = datos
                break
        else:
            self.datos.append(datos)

        self.refrescar_tabla()
        self.limpiar_formulario()

    # ---------------- REFRESCAR TABLA ----------------

    def refrescar_tabla(self):

        self.tree.delete(*self.tree.get_children())

        for d in self.datos:
            self.tree.insert("", "end", values=d)

    # ---------------- EDITAR ----------------

    def editar(self):

        sel = self.tree.focus()
        if not sel:
            return

        self.bloquear_formulario(False)
        self.entry_id.config(state="readonly")

    # ---------------- ELIMINAR ----------------

    def eliminar(self):

        sel = self.tree.focus()
        if not sel:
            return

        v = self.tree.item(sel, "values")

        if not messagebox.askyesno("Confirmar", "¿Eliminar este registro?"):
            return

        if not messagebox.askyesno("Confirmación final", "¿Seguro seguro?"):
            return

        self.datos = [d for d in self.datos if d[0] != v[0]]

        self.refrescar_tabla()
        self.limpiar_formulario()

    # ---------------- MOSTRAR DATOS ----------------

    def mostrar_datos(self):

        self.limpiar_formulario()
        self.tree.delete(*self.tree.get_children())

        for d in self.datos:
            self.tree.insert("", "end", values=d)

    # ---------------- BOTONES INFERIORES ----------------

    def botones_inferiores(self):

        frame = tk.Frame(self.contenedor, bg="#f2f2f2")
        frame.pack(fill="x", pady=25)

        tk.Button(frame, text="Cancelar", width=18, height=2,
                  command=self.limpiar_formulario).pack(side="left", padx=30)

        tk.Button(frame, text="Mostrar datos", width=18, height=2,
                  command=self.mostrar_datos).pack(side="left", expand=True)

        tk.Button(frame, text="Salir", width=18, height=2,
                  command=self.salir).pack(side="right", padx=30)

    # ---------------- SALIR ----------------

    def salir(self, event=None):

        if messagebox.askyesno("Salir", "¿Desea salir?"):
            self.root.destroy()


# ---------------- EJECUTAR ----------------

root = tk.Tk()
app = BibliotecaApp(root)
root.mainloop()
