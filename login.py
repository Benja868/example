import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pantalla_principal

def verificar_login(txtUsuario, txtContrasenia, pantalla_inicial):
    usuario = txtUsuario.get()
    contrasenia = txtContrasenia.get()
    
    if usuario == "admin" and contrasenia == "123":
        pantalla_inicial.destroy()
        pantalla_principal.mostrar_pantalla_principal()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def mostrar_pantalla_login():
    pantalla_inicial = tk.Tk()
    pantalla_inicial.title("Inicio de Sesión")
    pantalla_inicial.geometry("300x400") 
    pantalla_inicial.config(bg="#2c3e50")  # Color de fondo

    # Establece un ícono personalizado
    pantalla_inicial.iconbitmap('img/logo.ico') 

    # Cargar y mostrar imagen
    imagen = Image.open("img/logo.png") 
    imagen = imagen.resize((150, 150))  # Ajusta el tamaño de la imagen
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta_imagen = tk.Label(pantalla_inicial, image=imagen_tk, bg="#2c3e50")
    etiqueta_imagen.pack(pady=10)

    # Formulario de usuario y contraseña
    tk.Label(pantalla_inicial, text="Usuario", bg="#2c3e50", fg="white").pack(pady=5)
    txtUsuario = tk.Entry(pantalla_inicial)
    txtUsuario.pack(pady=5)

    tk.Label(pantalla_inicial, text="Contraseña", bg="#2c3e50", fg="white").pack(pady=5)
    txtContrasenia = tk.Entry(pantalla_inicial, show="*")
    txtContrasenia.pack(pady=5)

    # Botón de login
    boton_login = tk.Button(pantalla_inicial, text="Iniciar Sesión", font=("Arial", 10, "bold"), 
                            bg="#f4d03f", fg="blue", activebackground="#1a5276", 
                            activeforeground="yellow",width=15, height=1,borderwidth=2, relief="flat", 
                            command=lambda: verificar_login(txtUsuario, txtContrasenia, pantalla_inicial))
    boton_login.pack(pady=20)
    

    pantalla_inicial.mainloop()
