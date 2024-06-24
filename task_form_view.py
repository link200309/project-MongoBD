import tkinter as tk
from tkinter import messagebox

from conexion import obtener_cursos, crear_tarea
from utils import center_window

class TaskForm:
    def __init__(self, main_panel, nodo_user, home_navigate):
        self.panel = main_panel
        self.nodo_user = nodo_user
        self.home_navigate = home_navigate
        self.init_ventana()
        self.mostrar_formulario()
        
    def init_ventana(self):
        self.panel.geometry("980x600")
        self.panel.configure(bg="gray10")
        center_window(self.panel, 980, 600)
    
    def mostrar_formulario(self):
        cursos = obtener_cursos(self.nodo_user)
        
        #Home back
        self.btn_back_home = tk.Button(self.panel, text="Regresar", width=10, font=("Arial", 10), bd=2, relief=tk.GROOVE)
        self.btn_back_home.configure(command=lambda: self.home_navigate(self.nodo_user))
        self.btn_back_home.place(x = 50, y=10)
           
        self.label_dar_tarea = tk.Label(self.panel, text="Publicar tarea", width=15,font=("Arial", 20)) 
        self.label_dar_tarea.pack()
        
        #Formulario para el titulo
        self.label_titulo = tk.Label(self.panel, text="Titulo:", width=10,font=("Arial", 10)) 
        self.label_titulo.place(x=260, y=50)
        self.entry_titulo = tk.Entry(self.panel, width=40, font=("Arial", 10))
        self.entry_titulo.place(x=260, y=100)

        #formulario para la descripcion
        self.label_descripcion = tk.Label(self.panel, text="Descripcion:", width=10, font=("Arial", 10))
        self.label_descripcion.place(x=260, y=150)
        self.entry_descripcion = tk.Text(self.panel, width=40, height=5, font=("Arial", 10))
        self.entry_descripcion.place(x=260, y=200)
        
        #fecha limite
        self.label_fecha = tk.Label(self.panel, text="Fecha limite (AAAA-MM-DD):", width=22, font=("Arial", 10))
        self.label_fecha.place(x=260, y=300)
        self.entry_fecha = tk.Entry(self.panel, width=40, font=("Arial", 10))
        self.entry_fecha.place(x=260, y=350)
        
        #Cursos
        self.valor = tk.StringVar(self.panel)
        self.valor.set(cursos[0])
        
        self.label_cursos = tk.Label(self.panel, text="Curso:", width=10, font=("Arial", 10))
        self.label_cursos.place(x=260, y=400)
        
        self.options_cursos = tk.OptionMenu(self.panel, self.valor, *cursos)
        self.options_cursos.place(x=260, y=450)
        
        #Boton para mandar
        self.btn_mandar_tarea = tk.Button(self.panel, text="Mandar tarea", width=15, font=("Arial", 10), bd=2, relief=tk.GROOVE)
        self.btn_mandar_tarea.configure(command=self.registrarTarea)
        self.btn_mandar_tarea.place(x = 350, y=500)
        
        
    def registrarTarea(self):
       datos_tarea = {
       'titulo': self.entry_titulo.get(),
       'descripcion': self.entry_descripcion.get("1.0", "end-1c"),
       'fecha_limite': self.entry_fecha.get(),
       'nombre_curso': self.valor.get()
       }
       crear_tarea(self.nodo_user, datos_tarea)
       messagebox.showinfo("Login", "Registro exitoso")
       
def show_task_form(main_panel, nodo_user, home_navigate):
    TaskForm(main_panel, nodo_user, home_navigate)