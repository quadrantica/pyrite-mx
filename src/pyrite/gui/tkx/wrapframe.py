import tkinter as tk

class WrapFrame(tk.Frame):
    def __init__(self, master=None, padx=5, pady=5, **kwargs):
        super().__init__(master, **kwargs)
        self.padx = padx
        self.pady = pady
        self.bind("<Configure>", self._on_configure)

    def _on_configure(self, event):
        self._do_layout()

    def _do_layout(self):
        x, y, row_height = self.padx, self.pady, 0
        for widget in self.winfo_children():
            widget.update_idletasks()
            w, h = widget.winfo_reqwidth(), widget.winfo_reqheight()
            if x + w + self.padx > self.winfo_width():
                x = self.padx
                y += row_height + self.pady
                row_height = 0
            widget.pack_forget()
            widget.grid_forget()
            widget.place(x=x, y=y)
            x += w + self.padx
            row_height = max(row_height, h)
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.configure(height=y+row_height+self.pady)

        
