from tkinter import *
import tkinter.ttk as ttk


class MainGUI:
    def __init__(self):
        # window
        self.master = Tk()
        self.master.title("Monitorizare parametri")
        self.master.geometry("800x480+400+100")
        self.master.iconbitmap("icon.ico")
        self.s = ttk.Style()
        self.s.configure('.', font=('Helvetica', 12), foreground='white', background='gray')
        self.s.configure('Selected.TLabel', background='#4d4d4d')
        self.labels = ('General', 'Detalii', 'Istoric')
        # box generator
        self.boxes = list()
        for line in range(3):
            self.master.grid_rowconfigure(2 * line, minsize=20)
            for pos in range(3):
                self.master.grid_columnconfigure(2 * pos, minsize=20, weight=1)
                self.boxes.append(self.Box(self.master, 2 * line + 1, 2 * pos + 1, 'w',
                                           'Denumire camp{}'.format(pos), 'unit{}'.format(pos)))

        # panel generator
        self.panel_frame = ttk.Frame(self.master)
        self.master.grid_columnconfigure(6, minsize=10, weight=1)
        self.master.grid_columnconfigure(7, weight=1)
        self.master.grid_columnconfigure(8, minsize=5)
        self.panel_frame.grid(row=1, column=7, rowspan=5, sticky='ewns')
        self.buttons = list()
        for k in range(3):
            self.buttons.append(ttk.Label(self.panel_frame, text=self.labels[k]))
            self.buttons[k].grid(row=k, sticky='ns')
            self.buttons[k].bind('<Button-1>', lambda event, k=k: self.change_interface(event, k))
            self.panel_frame.grid_rowconfigure(k, weight=1)
        self.panel_frame.grid_columnconfigure(0, weight=1)

        # interface mainloop
        self.master.mainloop()

    def change_interface(self, event, k):
        print(k)
        # for i in range(3):
        #     if i == k:
        #         self.buttons[i]['style'] = 'Selected.Tlabel'
        #     else:
        #         self.buttons[i]['style'] = 'Tlabel'



    def update_values(self, values):
        for box in self.boxes:
            box.update(values)
        # update interface
        self.master.update_idletasks()

    class Box:

        def __init__(self, root, rows, columns, stick, tag, unit):
            self.box_frame = ttk.Frame(root)
            self.box_frame.grid(row=rows, column=columns, sticky=stick)
            self.box_frame.grid_columnconfigure(0, minsize=200, weight=2)
            self.label = ttk.Label(self.box_frame, text=tag)
            self.label.grid(row=0, sticky='w', padx=10, pady=10)
            self.unit = unit
            self.val_string = StringVar()
            self.val_string.set('--,-- {}'.format(self.unit))
            self.val = ttk.Label(self.box_frame, textvariable=self.val_string)
            self.val.grid(row=1, sticky='e', padx=10, pady=10)

        def update(self, value):
            self.val_string.set('{} {}'.format(value, self.unit))
