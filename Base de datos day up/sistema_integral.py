import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import sqlite3
import os
import shutil
import time

# --- CONFIGURACIÓN INICIAL Y BASE DE DATOS ---
CARPETA_ARCHIVOS = "archivos_clientes"
if not os.path.exists(CARPETA_ARCHIVOS):
    os.makedirs(CARPETA_ARCHIVOS)

# Esto crea la base de datos automáticamente con las nuevas reglas (permite campos vacíos)
def inicializar_bd():
    conn = sqlite3.connect("datos_impresiones.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        cedula TEXT,
                        telefono TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventario (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        producto TEXT,
                        precio REAL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS trabajos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_cliente INTEGER,
                        servicio TEXT,
                        ruta_archivo TEXT,
                        estado TEXT)''')
    conn.commit()
    conn.close()

inicializar_bd()
ruta_archivo_seleccionado = ""

# --- FUNCIONES: PESTAÑA INVENTARIO ---
def cargar_inventario():
    for fila in tabla_inventario.get_children():
        tabla_inventario.delete(fila)
    conn = sqlite3.connect("datos_impresiones.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, producto, precio FROM inventario")
    productos = cursor.fetchall()
    conn.close()

    lista_nombres = []
    for prod in productos:
        tabla_inventario.insert("", "end", values=(prod[0], prod[1], f"${prod[2]:.2f}"))
        lista_nombres.append(prod[1])
    
    combo_productos['values'] = lista_nombres
    if lista_nombres: combo_productos.current(0)

def guardar_o_modificar_producto():
    nombre_prod = entrada_nombre_prod.get()
    precio_prod = entrada_precio_prod.get()
    item_seleccionado = tabla_inventario.selection()

    if not nombre_prod or not precio_prod:
        messagebox.showwarning("Atención", "El nombre y precio son obligatorios.")
        return

    try:
        # CORRECCIÓN DE ERROR: Cambiamos comas por puntos por si el usuario escribe "15,50"
        precio_float = float(precio_prod.replace(",", ".")) 
        
        conn = sqlite3.connect("datos_impresiones.db")
        cursor = conn.cursor()

        if item_seleccionado: # MODO MODIFICAR
            id_prod = tabla_inventario.item(item_seleccionado[0])['values'][0]
            cursor.execute("UPDATE inventario SET producto=?, precio=? WHERE id=?", (nombre_prod, precio_float, id_prod))
            messagebox.showinfo("Éxito", "Producto actualizado.")
        else: # MODO AGREGAR
            cursor.execute("INSERT INTO inventario (producto, precio) VALUES (?, ?)", (nombre_prod, precio_float))
            messagebox.showinfo("Éxito", "Nuevo producto agregado.")
        
        conn.commit()
        conn.close()
        entrada_nombre_prod.delete(0, tk.END)
        entrada_precio_prod.delete(0, tk.END)
        tabla_inventario.selection_remove(item_seleccionado)
        cargar_inventario()
    except ValueError:
        messagebox.showerror("Error", "El precio debe ser un número (Ej. 15.50)")

def seleccionar_producto_tabla(event):
    item = tabla_inventario.selection()
    if item:
        valores = tabla_inventario.item(item[0])['values']
        entrada_nombre_prod.delete(0, tk.END)
        entrada_nombre_prod.insert(0, valores[1])
        entrada_precio_prod.delete(0, tk.END)
        entrada_precio_prod.insert(0, str(valores[2]).replace("$", ""))

def limpiar_seleccion_producto():
    tabla_inventario.selection_remove(tabla_inventario.selection())
    entrada_nombre_prod.delete(0, tk.END)
    entrada_precio_prod.delete(0, tk.END)

# --- FUNCIONES: PESTAÑA REGISTRO ---
def seleccionar_imagen():
    global ruta_archivo_seleccionado
    ruta = filedialog.askopenfilename(title="Seleccionar documento/imagen", filetypes=[("Archivos", "*.jpg *.png *.jpeg *.pdf"), ("Todos", "*.*")])
    if ruta:
        ruta_archivo_seleccionado = ruta
        label_archivo.config(text=f"Archivo: {os.path.basename(ruta)}", fg="blue")

def guardar_registro():
    nombre = entrada_nombre.get()
    cedula = entrada_cedula.get()
    telefono = entrada_telefono.get()
    producto = combo_productos.get()
    estado = combo_estado.get()
    
    # Permitimos campos vacíos, pero al menos debe haber algo en nombre o cédula para identificar
    if not nombre and not cedula:
        nombre = "Cliente Anónimo"

    conn = sqlite3.connect("datos_impresiones.db")
    cursor = conn.cursor()
    
    # 1. Guardar o encontrar cliente
    cursor.execute("INSERT INTO clientes (nombre, cedula, telefono) VALUES (?, ?, ?)", (nombre, cedula, telefono))
    id_cliente = cursor.lastrowid # Obtenemos el ID interno invisible

    # 2. Manejar el archivo
    nombre_final_archivo = "Sin archivo"
    if ruta_archivo_seleccionado:
        ext = os.path.splitext(ruta_archivo_seleccionado)[1]
        # Guardamos el archivo con el ID del cliente y la hora exacta para que no choque con otros
        nombre_final_archivo = f"doc_cli{id_cliente}_{int(time.time())}{ext}"
        shutil.copy(ruta_archivo_seleccionado, f"{CARPETA_ARCHIVOS}/{nombre_final_archivo}")

    # 3. Guardar el trabajo/servicio
    cursor.execute("INSERT INTO trabajos (id_cliente, servicio, ruta_archivo, estado) VALUES (?, ?, ?, ?)",
                   (id_cliente, producto, nombre_final_archivo, estado))
    
    conn.commit()
    conn.close()
    messagebox.showinfo("Éxito", "Registro guardado correctamente.")
    limpiar_campos_registro()
    cargar_directorio() # Actualizamos la lista de clientes

def limpiar_campos_registro():
    global ruta_archivo_seleccionado
    entrada_nombre.delete(0, tk.END)
    entrada_cedula.delete(0, tk.END)
    entrada_telefono.delete(0, tk.END)
    ruta_archivo_seleccionado = ""
    label_archivo.config(text="Ningún archivo seleccionado", fg="black")

# --- FUNCIONES: PESTAÑA DIRECTORIO (LISTA DE CLIENTES) ---
def cargar_directorio():
    for fila in tabla_clientes.get_children():
        tabla_clientes.delete(fila)
    conn = sqlite3.connect("datos_impresiones.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, cedula, telefono FROM clientes ORDER BY id DESC")
    clientes = cursor.fetchall()
    conn.close()
    for cli in clientes:
        tabla_clientes.insert("", "end", values=(cli[0], cli[1], cli[2], cli[3]))

def seleccionar_cliente_tabla(event):
    item = tabla_clientes.selection()
    if not item: return
    
    id_cliente = tabla_clientes.item(item[0])['values'][0]
    
    # Limpiamos la lista de archivos
    lista_archivos.delete(0, tk.END)
    
    conn = sqlite3.connect("datos_impresiones.db")
    cursor = conn.cursor()
    cursor.execute("SELECT servicio, estado, ruta_archivo FROM trabajos WHERE id_cliente=?", (id_cliente,))
    trabajos = cursor.fetchall()
    conn.close()

    if trabajos:
        for t in trabajos:
            etiqueta = f"[{t[1]}] {t[0]}"
            # Guardamos la ruta del archivo oculta en el listbox
            lista_archivos.insert(tk.END, etiqueta)
            # Asociamos la ruta al índice
            lista_archivos.archivos_ocultos = getattr(lista_archivos, 'archivos_ocultos', {})
            lista_archivos.archivos_ocultos[lista_archivos.size()-1] = t[2]
            
            btn_abrir_archivo.config(state="normal")
    else:
        lista_archivos.insert(tk.END, "Sin servicios registrados.")
        btn_abrir_archivo.config(state="disabled")

def abrir_archivo_seleccionado():
    seleccion = lista_archivos.curselection()
    if seleccion:
        indice = seleccion[0]
        ruta = lista_archivos.archivos_ocultos.get(indice)
        if ruta and ruta != "Sin archivo":
            os.startfile(f"{CARPETA_ARCHIVOS}\\{ruta}")
        else:
            messagebox.showinfo("Aviso", "Este registro no tiene un archivo adjunto.")

def modificar_cliente():
    item = tabla_clientes.selection()
    if not item:
        messagebox.showwarning("Atención", "Selecciona un cliente de la lista primero.")
        return
    
    valores = tabla_clientes.item(item[0])['values']
    id_cli = valores[0]

    # Crear ventana emergente
    ven_mod = tk.Toplevel(ventana)
    ven_mod.title("Modificar Cliente")
    ven_mod.geometry("300x250")

    tk.Label(ven_mod, text="Nombre:").pack(pady=2)
    ent_nom = tk.Entry(ven_mod, width=30)
    ent_nom.insert(0, valores[1] if valores[1] != "None" else "")
    ent_nom.pack()

    tk.Label(ven_mod, text="Cédula:").pack(pady=2)
    ent_ced = tk.Entry(ven_mod, width=30)
    ent_ced.insert(0, valores[2] if valores[2] != "None" else "")
    ent_ced.pack()

    tk.Label(ven_mod, text="Teléfono:").pack(pady=2)
    ent_tel = tk.Entry(ven_mod, width=30)
    ent_tel.insert(0, valores[3] if valores[3] != "None" else "")
    ent_tel.pack()

    def guardar_cambios():
        conn = sqlite3.connect("datos_impresiones.db")
        conn.execute("UPDATE clientes SET nombre=?, cedula=?, telefono=? WHERE id=?", 
                     (ent_nom.get(), ent_ced.get(), ent_tel.get(), id_cli))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Cliente actualizado.")
        ven_mod.destroy()
        cargar_directorio()

    tk.Button(ven_mod, text="Guardar Cambios", command=guardar_cambios, bg="#4CAF50", fg="white").pack(pady=15)


# --- INTERFAZ GRÁFICA PRINCIPAL ---
ventana = tk.Tk()
ventana.title("Base de datos day-up") # NUEVO NOMBRE
ventana.geometry("700x550")

notebook = ttk.Notebook(ventana)
notebook.pack(pady=10, expand=True, fill="both")

# --- PESTAÑA 1: NUEVO REGISTRO ---
frame_registro = tk.Frame(notebook)
notebook.add(frame_registro, text=" 📝 Nuevo Registro ")

tk.Label(frame_registro, text="(Puedes dejar campos vacíos si el cliente no los da)", fg="gray").pack(pady=5)

tk.Label(frame_registro, text="Nombre completo:").pack()
entrada_nombre = tk.Entry(frame_registro, width=40)
entrada_nombre.pack(pady=2)

tk.Label(frame_registro, text="Cédula:").pack()
entrada_cedula = tk.Entry(frame_registro, width=40)
entrada_cedula.pack(pady=2)

tk.Label(frame_registro, text="Teléfono:").pack()
entrada_telefono = tk.Entry(frame_registro, width=40)
entrada_telefono.pack(pady=2)

tk.Label(frame_registro, text="Servicio / Producto:").pack(pady=(10,0))
combo_productos = ttk.Combobox(frame_registro, width=37, state="readonly")
combo_productos.pack(pady=2)

# Nueva opción de estado opcional
tk.Label(frame_registro, text="Estado del Trabajo:").pack(pady=(10,0))
combo_estado = ttk.Combobox(frame_registro, width=37, state="readonly", values=["Completado / Entregado", "Pendiente"])
combo_estado.current(0)
combo_estado.pack(pady=2)

tk.Button(frame_registro, text="📎 Adjuntar Documento/Copia (Opcional)", command=seleccionar_imagen).pack(pady=10)
label_archivo = tk.Label(frame_registro, text="Ningún archivo seleccionado")
label_archivo.pack()

tk.Button(frame_registro, text="💾 GUARDAR EN BASE DE DATOS", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=guardar_registro).pack(pady=15)

# --- PESTAÑA 2: DIRECTORIO DE CLIENTES (NUEVA) ---
frame_directorio = tk.Frame(notebook)
notebook.add(frame_directorio, text=" 👥 Directorio de Clientes ")

# Dividimos la pantalla en Izquierda (Lista de clientes) y Derecha (Archivos)
frame_izq = tk.Frame(frame_directorio)
frame_izq.pack(side="left", fill="both", expand=True, padx=10, pady=10)

frame_der = tk.LabelFrame(frame_directorio, text=" Archivos / Servicios del Cliente ")
frame_der.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Tabla de clientes
columnas_cli = ("ID", "Nombre", "Cédula", "Teléfono")
tabla_clientes = ttk.Treeview(frame_izq, columns=columnas_cli, show="headings")
tabla_clientes.heading("ID", text="ID")
tabla_clientes.heading("Nombre", text="Nombre")
tabla_clientes.heading("Cédula", text="Cédula")
tabla_clientes.heading("Teléfono", text="Teléfono")
tabla_clientes.column("ID", width=30)
tabla_clientes.column("Nombre", width=120)
tabla_clientes.column("Cédula", width=80)
tabla_clientes.column("Teléfono", width=80)
tabla_clientes.pack(fill="both", expand=True)
tabla_clientes.bind("<<TreeviewSelect>>", seleccionar_cliente_tabla)

tk.Button(frame_izq, text="✏️ Modificar Cliente Seleccionado", command=modificar_cliente).pack(pady=5)

# Lista de archivos en el panel derecho
lista_archivos = tk.Listbox(frame_der, width=40, height=15)
lista_archivos.pack(pady=10, padx=10)

btn_abrir_archivo = tk.Button(frame_der, text="🖼️ ABRIR ARCHIVO SELECCIONADO", state="disabled", bg="#2196F3", fg="white", command=abrir_archivo_seleccionado)
btn_abrir_archivo.pack(pady=10)

# --- PESTAÑA 3: INVENTARIO ---
frame_inventario = tk.Frame(notebook)
notebook.add(frame_inventario, text=" 📦 Precios y Servicios ")

frame_agregar_prod = tk.Frame(frame_inventario)
frame_agregar_prod.pack(pady=10)

tk.Label(frame_agregar_prod, text="Servicio/Producto:").grid(row=0, column=0, padx=5)
entrada_nombre_prod = tk.Entry(frame_agregar_prod, width=25)
entrada_nombre_prod.grid(row=1, column=0, padx=5)

tk.Label(frame_agregar_prod, text="Precio ($):").grid(row=0, column=1, padx=5)
entrada_precio_prod = tk.Entry(frame_agregar_prod, width=10)
entrada_precio_prod.grid(row=1, column=1, padx=5)

tk.Button(frame_agregar_prod, text="💾 Guardar / Actualizar", bg="#2196F3", fg="white", command=guardar_o_modificar_producto).grid(row=1, column=2, padx=5)
tk.Button(frame_agregar_prod, text="Desmarcar", command=limpiar_seleccion_producto).grid(row=1, column=3, padx=5)

columnas_inv = ("ID", "Producto", "Precio")
tabla_inventario = ttk.Treeview(frame_inventario, columns=columnas_inv, show="headings", height=12)
tabla_inventario.heading("ID", text="ID")
tabla_inventario.heading("Producto", text="Producto / Servicio")
tabla_inventario.heading("Precio", text="Precio")
tabla_inventario.column("ID", width=30)
tabla_inventario.column("Producto", width=300)
tabla_inventario.column("Precio", width=100)
tabla_inventario.pack(pady=10)
tabla_inventario.bind("<<TreeviewSelect>>", seleccionar_producto_tabla)

# Iniciar cargando datos
cargar_inventario()
cargar_directorio()

ventana.mainloop()