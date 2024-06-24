import tkinter as tk

#modulos propios
from login_view import show_login
from home_view import show_home

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.show_login_view()
    
    #Vistas    
    def show_login_view(self):
        self.main_panel = tk.Toplevel(self.root)
        self.main_panel.protocol('WM_DELETE_WINDOW', self.on_closing)
        show_login(self.main_panel, self.show_home_view)
        
    def show_home_view(self, nodo_user):
        self.reset_panel()
        home_navigation = {
            "show_task_form_view":None,
        }
        show_home(self.main_panel, nodo_user, home_navigation)
        
    #Configuraciones     
    def reset_panel(self):
        if(self.main_panel): self.main_panel.destroy()
        self.main_panel = tk.Toplevel(self.root)
        self.main_panel.protocol('WM_DELETE_WINDOW', self.on_closing)
        
    def on_closing(self):
        if self.main_panel:
            self.main_panel.destroy()
        self.root.destroy()
        
if __name__ == "__main__":
    app = App()
    app.root.mainloop()
        
        
        
        
    