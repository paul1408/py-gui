from tkinter import *
import tkinter.ttk as ttk


class MyGUI:
    def __init__(self):
        self.master = Tk()
        self.master.title("Monitorizare parametri")
        self.master.geometry("800x480+400+100")
        self.master.iconbitmap("icon.ico")

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(0, minsize=20)
        self.master.grid_columnconfigure(0, minsize=20)
        self.master.grid_columnconfigure(2, minsize=20)
        self.master.grid_columnconfigure(4, minsize=20)
        self.master.grid_columnconfigure(6, minsize=20)

        s = ttk.Style()
        s.configure('.', font=('Helvetica', 12), foreground='white', background='gray')

        #frames
        self.frame_1 = ttk.Frame(self.master)
        self.frame_1.grid(row=1, column=1, sticky='w')
        self.frame_1.grid_columnconfigure(0, minsize=200)
        self.frame_2 = ttk.Frame(self.master)
        self.frame_2.grid(row=1, column=3, sticky='ew')
        self.frame_2.grid_columnconfigure(0, minsize=200)
        self.frame_3 = ttk.Frame(self.master)
        self.frame_3.grid(row=1, column=5, sticky='e')
        self.frame_3.grid_columnconfigure(0, minsize=200)
        #frame1
        self.label_speed = ttk.Label(self.frame_1, text='Viteza deplasare')
        self.label_speed.grid(row=0, sticky='w', padx=10, pady=10)
        self.label_speed_val = ttk.Label(self.frame_1, text='--,-- km/h')
        self.label_speed_val.grid(row=1, sticky='e', padx=10, pady=10)

        #frame_2
        self.label_volt = ttk.Label(self.frame_2, text='Voltaj baterie')
        self.label_volt.grid(row=0, sticky='w', padx=(20,10), pady=10)
        self.label_volt_val = ttk.Label(self.frame_2, text='--,-- V')
        self.label_volt_val.grid(row=1, sticky='e', padx=10, pady=10)

        #frame 3
        self.label_temp = ttk.Label(self.frame_3, text='Temperatura baterie')
        self.label_temp.grid(row=0, sticky='w', padx=(20, 10), pady=10)
        self.label_temp_val = ttk.Label(self.frame_3, text='--,-- grdC')
        self.label_temp_val.grid(row=1, sticky='e', padx=10, pady=10)

        self.master.mainloop()

        class Box:

            def __init__(self, root, rows, columns, stick):
                ttk.Frame.__init__(root)
                self.grid(row=rows, column=columns, sticky=stick)
                self.grid_columnconfigure(0, minsize=200)
