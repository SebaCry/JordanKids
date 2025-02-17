
import customtkinter as ctk

# Configuración principal de CTK
ctk.set_appearance_mode("dark")  # "light", "dark", "system"
ctk.set_default_color_theme("blue")  # También puedes usar "green" o "dark-blue"

# Diccionario que asocia botones con su contenido
contenido_diccionario = {
    "Perfiles": "Aquí están los Perfiles",
    "Calendario": "Vista del Calendario",
    "Podio": "Ranking del Podio",
    "Salir": "Salir de la aplicación"
}

def mostrar_contenido(contenido):
    """Cambia dinámicamente el contenido del espacio derecho."""
    for widget in espacio.winfo_children():
        widget.destroy()  # Limpia el contenido actual del frame

    if contenido == "Salir":
        app.destroy()  # Cierra la aplicación
        return
    
    # Obtiene el texto correspondiente al botón desde el diccionario
    texto = contenido_diccionario.get(contenido, "Contenido no definido")
    
    label = ctk.CTkLabel(espacio, text=texto, font=("Arial", 18))
    label.pack(expand=True, fill="both")

# Configuración de la ventana principal
app = ctk.CTk()
app.title("JordanKids")
app.geometry("800x500")  # Tamaño de la ventana

# Frame lateral para los botones
menu = ctk.CTkFrame(app, width=200, corner_radius=0)
menu.pack(side="left", fill="y")

# Línea divisoria (simulada con un Frame delgado)
separator = ctk.CTkFrame(app, width=2, fg_color="gray")
separator.pack(side="left", fill="y")

# Frame derecho para el contenido dinámico
espacio = ctk.CTkFrame(app, corner_radius=10)
espacio.pack(side="right", expand=True, fill="both")

# Lista de botones y creación dinámica
botones = contenido_diccionario.keys()
for boton in botones:
    btn = ctk.CTkButton(menu, text=boton, height=40, 
                        command=lambda b=boton: mostrar_contenido(b))
    btn.pack(pady=10, padx=10)

# Inicializa con contenido vacío
mostrar_contenido("Perfiles")

# Ejecuta la aplicación
app.mainloop()
