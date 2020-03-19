import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename


class App(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Test GUI')

        self.pack(padx=5, pady=5)

        self.create_layout()

    def create_layout(self):
        a1 = ttk.Button()
        a13 = ttk.Checkbutton()
        a14 = ttk.Entry()
        a15 = ttk.Frame()
        a16 = ttk.Label()
        a17 = ttk.LabelFrame()
        a18 = ttk.Menubutton()
        a2 = ttk.PanedWindow()
        a3 = ttk.Radiobutton()
        a4 = ttk.Scale()
        a5 = ttk.Scrollbar()
        a6 = ttk.Spinbox()
        a7 = ttk.Combobox()
        a8 = ttk.Notebook()
        a9 = ttk.Progressbar(value=50)
        a10 = ttk.Separator()
        a11 = ttk.Sizegrip()
        a12 = ttk.Treeview()

        a1.pack()
        a13.pack()
        a14.pack()
        a15.pack()
        a16.pack()
        a17.pack()
        a18.pack()
        a2.pack()
        a3.pack()
        a4.pack()
        a5.pack()
        a6.pack()
        a7.pack()
        a8.pack()
        a9.pack()
        a10.pack()
        a11.pack()
        a12.pack()


def main():
    root = tk.Tk()
    app = App(root)
    app.mainloop()

if __name__ == '__main__':
    main()

