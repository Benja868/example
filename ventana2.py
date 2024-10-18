import tkinter as tk
from PIL import Image, ImageTk

def mostrar_ventana2(nombre_usuario, correo_usuario):
    ruta_foto_usuario = f"img/fotos/{nombre_usuario}.png"
    ventana2 = tk.Toplevel()  # Crear una nueva ventana
    ventana2.title("Ventana 2 - Detalles del Usuario")
    ventana2.geometry("400x400")
    ventana2.config(bg="#ecf0f1")

    # Etiqueta de título
    etiqueta_titulo = tk.Label(ventana2, text="Detalles del Usuario", font=("Arial", 16, "bold"), bg="#ecf0f1", fg="#34495e")
    etiqueta_titulo.pack(pady=10)

    # Mostrar nombre y correo
    tk.Label(ventana2, text=f"Nombre: {nombre_usuario}", bg="#ecf0f1", fg="#34495e").pack(pady=5)
    tk.Label(ventana2, text=f"Correo: {correo_usuario}", bg="#ecf0f1", fg="#34495e").pack(pady=5)

    # Mostrar la foto del usuario
    try:
        imagen = Image.open(ruta_foto_usuario)
        imagen = imagen.resize((100, 100))  # Redimensionar la imagen
        imagen_tk = ImageTk.PhotoImage(imagen)

        # Crear una etiqueta para mostrar la imagen
        etiqueta_foto = tk.Label(ventana2, image=imagen_tk, bg="#ecf0f1")
        etiqueta_foto.image = imagen_tk  # Mantener una referencia a la imagen
        etiqueta_foto.pack(pady=10)
    except Exception as e:
        tk.Label(ventana2, text="No se pudo cargar la imagen.", bg="#ecf0f1", fg="red").pack(pady=10)

    # Botón para cerrar la ventana
    btn_cerrar = tk.Button(ventana2, text="Cerrar", command=ventana2.destroy, bg="#e74c3c", fg="white")
    btn_cerrar.pack(pady=20)

    ventana2.mainloop()
