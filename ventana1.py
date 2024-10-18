import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import ventana2
import os

# Variables globales para almacenar los datos del usuario
nombre_usuario = ""
correo_usuario = ""
ruta_foto_usuario = ""
imagen_tk = None  # Variable global para mantener la referencia de la imagen

# Carpeta para almacenar fotos
CARPETA_IMAGENES = "img/fotos"

# Crear la carpeta para las imágenes si no existe
if not os.path.exists(CARPETA_IMAGENES):
    os.makedirs(CARPETA_IMAGENES)

def cargar_foto():
    global ruta_foto_usuario,nombre_usuario, imagen_tk, ventana1
    # Permitir al usuario seleccionar una imagen
    ruta_foto_usuario = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if ruta_foto_usuario:
        pass
    else:
        btn_guardar.pack_forget()
        messagebox.showerror("Error", "Debe seleccionar una imagen")
        
        # Mostrar la foto seleccionada
        #imagen = Image.open(ruta_foto_usuario)
        #imagen = imagen.resize((100, 100))  # Redimensionar la imagen
        #imagen_tk = ImageTk.PhotoImage(imagen)
        #etiqueta_foto.config(image=imagen_tk)
        #etiqueta_foto.image = imagen_tk  # Para evitar que la imagen sea recolectada por el recolector de basura
    
def guardar_datos():
    global nombre_usuario, correo_usuario, entry_nombre, entry_correo, ruta_foto_usuario
    # Obtener los datos del formulario
    nombre_usuario = entry_nombre.get()
    correo_usuario = entry_correo.get()
    
    if not nombre_usuario or not correo_usuario or not ruta_foto_usuario:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return
    
    # Crear un nombre de archivo para la foto usando el nombre del usuario
    nombre_archivo_foto = f"{nombre_usuario}.png"  # Guardar como PNG
    nueva_ruta_foto = os.path.join(CARPETA_IMAGENES, nombre_archivo_foto)  # Ruta completa en la carpeta

    # Guardar la imagen en la nueva ubicación
    try:
        imagen_original = Image.open(ruta_foto_usuario)
        imagen_original.save(nueva_ruta_foto, format='PNG')  # Guardar la imagen en formato PNG
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar la imagen: {e}")
        return


    # Abrir la ventana2 y pasar los datos
    #ventana2.mostrar_ventana2(nombre_usuario, correo_usuario, ruta_foto_usuario)

def mostrar_ventana1():
    global entry_nombre, entry_correo, etiqueta_foto  # Hacerlas globales para acceder en otras funciones

    ventana1 = tk.Tk()
    ventana1.title("Ventana 1 - Datos de Usuario")
    ventana1.geometry("400x400")
    ventana1.config(bg="#ecf0f1")

    # Etiqueta de título
    etiqueta_titulo = tk.Label(ventana1, text="Formulario de Usuario", font=("Arial", 16, "bold"), bg="#ecf0f1", fg="#34495e")
    etiqueta_titulo.pack(pady=10)

    # Formulario
    tk.Label(ventana1, text="Nombre:", bg="#ecf0f1", fg="#34495e").pack(pady=5)
    entry_nombre = tk.Entry(ventana1)
    entry_nombre.pack(pady=5)

    tk.Label(ventana1, text="Correo Electrónico:", bg="#ecf0f1", fg="#34495e").pack(pady=5)
    entry_correo = tk.Entry(ventana1)
    entry_correo.pack(pady=5)

    # Sección para cargar foto
    etiqueta_foto = tk.Label(ventana1, bg="#ecf0f1")
    etiqueta_foto.pack(pady=10)

    btn_cargar_foto = tk.Button(ventana1, text="Cargar Foto", command=cargar_foto, bg="#3498db", fg="white", width=15)
    btn_cargar_foto.pack(pady=5)

    # Botón Guardar
    btn_guardar = tk.Button(ventana1, text="Guardar", command=guardar_datos, bg="#2ecc71", fg="white", width=15)
    btn_guardar.pack(pady=20)
    
    ventana1.mainloop()

# Llamar a la función para mostrar la ventana 1 al iniciar el programa
#mostrar_ventana1()
