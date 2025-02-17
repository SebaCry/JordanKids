from customtkinter import *
import customtkinter as ctk



def content_diff(content):

    space = ctk.CTkFrame(app, corner_radius=0)
    space.pack(side="right", expand=True, fill="both")
    
    for widget in space.winfo_children():
        widget.destroy()

    if content == 'Perfiles':
        label = ctk.CTkLabel(space, test='Perfiles de los chicos', font=('Arial', 18))
    elif content == 'Calendario':
        label = ctk.CTkLabel(space, test='Calendario de actividades', font=('Arial', 18))
    elif content == 'Podio':
        label = ctk.CTkLabel(space, test='Podio por la cantidad de puntos', font=('Arial', 18))
    elif content == 'Salir':
        app.destroy()
        return
    else:
        label = ctk.CTkLabel(space, text="Contenido no definido", font=("Arial", 18))
    
    label.pack(expand=True, fill="both")


app = ctk.CTk()
app.title('JordanKids')
app.geometry('700x600')
set_appearance_mode('dark')

menu = ctk.CTkFrame(app, width=200, corner_radius=0)
menu.pack(side='left', fill='y')

separator = ctk.CTkFrame(app, width=2,fg_color='gray')
separator.pack(side='left', fill='y')



nombres = ['Perfiles', 'Calendario', 'Podio', 'Salir']

for nom in nombres:
    button = ctk.CTkButton(menu,text=nom,height=40,
                           command=lambda btn=nom: content_diff(btn))
    button.pack(pady=10, padx=10)



content_diff('')


app.mainloop()
