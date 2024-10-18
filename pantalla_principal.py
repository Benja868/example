import tkinter as tk
from PIL import Image, ImageTk
import login
import ventana1
import ventana2
import ventana3

print("chupalo")

def cerrar_sesion(pantalla_principal):
    pantalla_principal.destroy()  # Cierra la pantalla principal
    login.mostrar_pantalla_login()  # Vuelve a mostrar la pantalla de login

def salir_aplicacion(pantalla_principal):
    pantalla_principal.quit()  # Sale del bucle principal de Tkinter
    pantalla_principal.destroy()  # Destruye todas las ventanas abiertas y cierra la aplicación

def mostrar_pantalla_principal():
    pantalla_principal = tk.Tk()
    pantalla_principal.title("Pantalla Principal")
    pantalla_principal.geometry("800x600")
    pantalla_principal.config(bg="#34495e")
    pantalla_principal.iconbitmap('img/logo.ico')

    # Cargar imagen de fondo
    imagen_fondo = Image.open("img/fotito.jpg")
    imagen_fondo = imagen_fondo.resize((800, 600))
    imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

    etiqueta_fondo = tk.Label(pantalla_principal, image=imagen_fondo_tk)
    etiqueta_fondo.place(x=0, y=0, relwidth=1, relheight=1)

    # Crear barra de menú
    menu_barra = tk.Menu(pantalla_principal)
    pantalla_principal.config(menu=menu_barra)

    # Menú de opciones
    menu_opciones = tk.Menu(menu_barra, tearoff=0)
    menu_opciones.add_command(label="Ingreso datos del Usuario", command=ventana1.mostrar_ventana1)
    menu_opciones.add_command(label="Mostrar datos del Usuario", command=ventana2.mostrar_ventana2)
    menu_opciones.add_command(label="Ir a Ventana 3", command=ventana3.mostrar_ventana3)
    menu_barra.add_cascade(label="Opciones", menu=menu_opciones)

    # Menú de sesión
    menu_sesion = tk.Menu(menu_barra, tearoff=0)
    menu_sesion.add_command(label="Cerrar Sesión", command=lambda: cerrar_sesion(pantalla_principal))
    menu_sesion.add_command(label="Salir", command=lambda: salir_aplicacion(pantalla_principal))
    menu_barra.add_cascade(label="Sesión", menu=menu_sesion)

    etiqueta_bienvenida = tk.Label(pantalla_principal, text="¡Bienvenido a la pantalla principal!",
                                   font=("Arial", 16, "bold"), bg="#34495e", fg="white")
    etiqueta_bienvenida.pack(pady=10)

    pantalla_principal.mainloop()
