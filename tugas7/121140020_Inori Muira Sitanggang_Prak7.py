import tkinter as tk
from tkinter import messagebox

def Kilometer():
    try:
        check = entry.get()
        if not check:
            raise ValueError("Masukkan Nilai Jarak")
        cm = (float(entry.get()) * 100000)
        m = (float(entry.get()) * 1000)
        mm = (float(entry.get()) * 1000000)
        result.config(text="Centimeter : " + str(cm) + "\nMeter : " + str(m) + "\nMilimeter : " + str(mm))
    except ValueError as err:
        messagebox.showerror("Error",str(err))

def Centimeter():
    try:
        check = entry.get()
        if not check:
            raise ValueError("Masukkan Nilai Jarak")
        km = (float(entry.get()) / 100000)
        m = (float(entry.get()) * 0.01)
        mm = (float(entry.get()) * 10)
        result.config(text="Kilometer : " + str(km) + "\nMeter : " + str(m) + "\nMilimeter : " + str(mm))
    except ValueError as err:
        messagebox.showerror("Error",str(err))

def Meter():
    try:
        check = entry.get()
        if not check:
            raise ValueError("Masukkan Nilai Jarak")
        km = (float(entry.get()) * 0.001)
        cm = (float(entry.get()) * 100)
        mm = (float(entry.get()) * 1000)
        result.config(text="Kilometer : " + str(km) + "\nCentimeter : " + str(cm) + "\nMilimeter : " + str(mm))
    except ValueError as err:
        messagebox.showerror("Error",str(err))
    
def Milimeter():
    try:
        check = entry.get()
        if not check:
            raise ValueError("Masukkan Nilai Jarak")
        km = (float(entry.get()) / 1000000)
        m = (float(entry.get()) * 0.001)
        cm = (float(entry.get()) * 0.1)
        result.config(text="Kilometer : " + str(km) + "\nMeter : " + str(m) + "\nCentimeter : " + str(cm))
    except ValueError as err:
        messagebox.showerror("Error",str(err))
    

root = tk.Tk()
root.title("Konversi Jarak")
root.geometry("300x200")

label1 = tk.Label(root, text="Masukkan nilai jarak:", font=("Arial", 10))
label1.pack()
entry = tk.Entry(root)
entry.pack()
label2 = tk.Label(root, text="Satuan asal jarak:", font=("Arial", 10))
label2.pack()
buttonframe  = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

button1 = tk.Button(buttonframe, text="Kilometer", font=("Calibri", 10), bg="silver", command=Kilometer)
button1.grid(row=1, column=0, sticky='we')
button2 = tk.Button(buttonframe, text="Centimeter", font=("Calibri", 10), bg="silver", command=Centimeter)
button2.grid(row=1, column=1, sticky='we')
button3 = tk.Button(buttonframe, text="Meter", font=("Calibri", 10), bg="silver", command=Meter)
button3.grid(row=1, column=2, sticky='we')
button4 = tk.Button(buttonframe, text="Milimeter", font=("Calibri", 10), bg="silver", command=Milimeter)
button4.grid(row=1, column=3, sticky='we')
buttonframe.pack()

label3 = tk.Label(root, text="Hasil", font=("Calibri", 10))
label3.pack()
result = tk.Label(root, font=("Calibri", 10))
result.pack()

root.mainloop()
