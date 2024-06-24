import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

from utils import center_window
from conexion import log_in

class Login:
    def __init__(self, panel, home_navigate):
        self.panel = panel
        self.home_navigate = home_navigate
        self.init_ventana()
        self.definir_formulario()
    
    def init_ventana(self):
        self.panel.geometry("980x600")
        imagen = Image.open("score2.jpg")
        imagen = imagen.resize((980, 620)) 
        imagen_tk = ImageTk.PhotoImage(imagen)
        center_window(self.panel, 980, 600)

        label_imagen = tk.Label(self.panel, image=imagen_tk)
        label_imagen.image = imagen_tk
        label_imagen.pack()
        
    #FORMULARIOS DEL LOGIN
    def definir_formulario(self):
        self.label_title = tk.Label(self.panel, text="LOGIN-TBD", width=10, font=("Arial", 25)) 
        
        self.label_username = tk.Label(self.panel, text="Usuario:", width=10,font=("Arial", 15)) 
        self.entry_username = tk.Entry(self.panel, width=40, font=("Arial", 15))

        self.label_password = tk.Label(self.panel, text="Contraseña:", width=10, font=("Arial", 15))
        self.entry_password = tk.Entry(self.panel, show="*", width=40, font=("Arial", 15)) 

        self.btn_login = tk.Button(self.panel, text="Iniciar sesión", command=self.login_home, width=35)
        
        self.label_title.place(x=390, y=50)
        self.label_username.place(x=260, y=150)
        self.label_password.place(x=260, y=300)
        self.entry_username.place(x=260, y=200)
        self.entry_password.place(x=260, y=350)
        self.btn_login.place(x = 350, y=450)

    def login_home(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        document_user = log_in(username, password)

        if len(document_user) != 0:
            messagebox.showinfo("Login", "Inicio de sesión exitoso")
            self.home_navigate(document_user)
        else:
            messagebox.showerror("Login", "Credenciales incorrectas")
                  
            
def show_login(main_panel, home_navigate):
    
    Login(main_panel, home_navigate)