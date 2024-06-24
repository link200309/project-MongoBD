import tkinter as tk

from utils import center_window
from conexion import obtener_interfaces

class Home:
    def __init__(self, panel, document_user, navigation):
        self.panel = panel
        self.document_user = document_user
        self.navigation = navigation
        self.init_ventana()
        self.mostrarInterfaces()
        
    def init_ventana(self):
        self.panel.geometry("980x600")
        self.panel.configure(bg="gray10")
        center_window(self.panel, 980, 600)
        
    def mostrarInterfaces(self):
        interfaces = obtener_interfaces(self.document_user)
        self.label_datos = tk.Label(self.panel, text=f"{self.document_user['nombre']}", width=30,font=("Arial", 20)) 
        self.label_datos.pack()
       
        for interfaz in interfaces:
            if interfaz == 'dar tarea':
                self.btn_dar_tarea = tk.Button(self.panel, text=interfaz, width=30,font=("Arial", 25), bd=2, relief=tk.GROOVE)
                self.btn_dar_tarea.configure(command=self.onclick_btn_dar_tarea)
                self.btn_dar_tarea.pack(pady=15, padx=20)
                continue
               
            if interfaz == 'ver entregas':
               self.btn_ver_entregas = tk.Button(self.panel, text=interfaz, width=30, font=("Arial", 25))
               self.btn_ver_entregas.configure()
               self.btn_ver_entregas.pack(pady=15, padx=20)
               continue
               
            if interfaz == 'ver planilla':
               self.btn_ver_planilla = tk.Button(self.panel, text=interfaz, width=30, font=("Arial", 25), bd=2, relief=tk.GROOVE, state=tk.DISABLED)
               self.btn_ver_planilla.configure()
               self.btn_ver_planilla.pack(pady=15, padx=20)
               continue
               
            if interfaz == 'subir tarea':
                self.btn_subir_tarea = tk.Button(self.panel, text=interfaz, width=30, font=("Arial", 25), bd=2, relief=tk.GROOVE)
                self.btn_subir_tarea.configure()
                self.btn_subir_tarea.pack(pady=15, padx=20)
                continue
            
            if interfaz == 'ver notas':
                self.btn_ver_notas = tk.Button(self.panel, text=interfaz, width=30, font=("Arial", 25), bd=2, relief=tk.GROOVE, state=tk.DISABLED)
                self.btn_ver_notas.configure()
                self.btn_ver_notas.pack(pady=15, padx=20)
                continue
            
            if interfaz == 'ver materias inscritas':
                self.btn_ver_materias_inscritas = tk.Button(self.panel, text=interfaz, width=30, font=("Arial", 25), bd=2, relief=tk.GROOVE, state=tk.DISABLED)
                self.btn_ver_materias_inscritas.configure()
                self.btn_ver_materias_inscritas.pack(pady=15, padx=20)
                continue
    
    def onclick_btn_dar_tarea(self):
        self.navigation.get('show_task_form_view')(self.document_user)
        
def show_home(main_panel, document_user, home_navigation):
    Home(main_panel, document_user, home_navigation)