import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from  ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.validation import add_regex_validation

class Gradebook(ttk.Frame):
    def __init__(self, master_window):
        super().__init__(master_window, padding=(20,10))
        self.pack(fill=BOTH, expand=YES)



app = ttk.Window("Gradebook", "superhero", resizable=(False, False))
Gradebook(app)
app.mainloop()





